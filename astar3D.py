'''
Main running file
Date: 26/05/2016
Daniel Staal

In this file all the classes are controlled and the final result is written
to the .csv file. This file is called by chips_exe.py
'''

import math
import copy
import time
import visualization
import Position
import PathData
import Grid
import Extra
from random import randint
import sys
import csv

# main function, called by chips_exe.py with the starting variables
def executeAlgorithm(gridMeasures, netlist, gates, iterations, csvFileName, randomOrNeighbour, reMaking, shortFirst):

    for i in range(iterations): 
        print "iteration: ", i
        length = gridMeasures[0]
        width = gridMeasures[1]
        height = gridMeasures[2]

        # import connections from netlist
        connections = netlist
        
        # order the connections short to long
        if shortFirst:
            connections = orderConnections(connections);
        
        # create the grid
        newGrid = Grid.Grid(length,width,height)
        # put the gates in the grid
        newGrid.drawGates(connections, 4, 0)
        # random or neighbour
        newGrid.setRandomOrNeighbour(randomOrNeighbour)
        
        # make all connections
        time1 = time.time()
        
        # make the connections
        paths = []
        makeAllConnections(connections, newGrid, paths, shortFirst)
        
        # calculating total length of connections
        newTotalLength = calcTotalPathLength(paths)
        if reMaking == True:
            totalLength = 10000
            while newTotalLength < totalLength:
                # print paths
                totalLength = newTotalLength
                # print "newtotallength: ", newTotalLength
                paths = reMakeAllConnections(newGrid, paths)
                newTotalLength = calcTotalPathLength(paths)
                if newTotalLength == "break":
                    break
        time2 = time.time()
            
        totalTime = time2-time1
        
        # calculateOptimum(length, width, height, netlists.getNetlist3())
        
        fileName = csvFileName + ".csv"
        
        if newTotalLength != "break":
            writeToCSV(newTotalLength, totalTime, paths, fileName)
        
        visualization.plotAstar(length, width, height, paths, gates)
            
# order the connections from shortest to longest
def orderConnections(connections):
    distances = []
    for connection in connections:
        distances.append(Extra.calcDistance(connection[0], connection[1]))
    indexList = sorted(range(len(distances)), key=lambda k: distances[k])
    copyConnections = []
    for index in indexList:
        copyConnections.append(connections[index])
    return copyConnections
    
# making connections via the A* algorithm
def makeAllConnections(connections, newGrid, paths, shortFirst):
    extraConnections = []
    countAttemps = 0;
    while len(connections) != 0:
        for connection in connections:
            countAttemps += 1
            path = []

            # length of 3 is [x,y,z]
            while len(path) != 3:
                path = findPath(connection, newGrid, paths)
                
                # if returned extra connection
                if len(path) == 2:
                    extraConnections.append(path)
            paths.append(path)
        connections = copy.deepcopy(extraConnections)
        if shortFirst:
            connections = orderConnections(connections)
        extraConnections = []
        
# function to make a connection between two points using A*
def findPath(connection, grid, paths):
    
    # set the start and end in the grid
    grid.setStartEnd(connection[0], connection[1])
    #  create a object to hold the pathData
    pathData = PathData.PathData()
    # set up a new path
    currentPath = []
    currentPath.append(grid.getStart())
    endPos = grid.getEnd()
    
    while not(currentPath[-1].getX() == endPos.getX() and currentPath[-1].getY() == endPos.getY() and currentPath[-1].getZ() == endPos.getZ()):
        # add current location to the closedList and remove from openlist
        pathData.putInClosedList(currentPath[-1])
        
        # expand the openList
        posNextPaths = grid.getPossibleNextPaths(currentPath, pathData)
        expandOpenList(posNextPaths, endPos, pathData)
        
        # search the openlist for the path with the lowest F-score
        tempPath = pathData.getLowestFScore(currentPath[-1], endPos, paths, grid)
        
        # if the path is blocked delete a neighbouring path
        if(tempPath == "blocked"):
            return blockedExtraConnection(paths, grid, pathData, currentPath[-1])
            
        # if Astar takes too much time, delete a neighbour at the end
        elif(tempPath == "turnaround"):
            return blockedExtraConnection(paths, grid, pathData, endPos)

        else:
            currentPath = copy.deepcopy(tempPath);
            grid.setPointToValue(currentPath[-1], 1)

    return grid.drawPath(currentPath, pathData.closedList)

# function called when connection is blocked
def blockedExtraConnection(paths, grid, pathData, pos):
    # search random path
    if(len(paths) == 0):
        print "no paths left error"
        sys.exit()
    
    # in case no neighbour is found but connection can't be made
    neighbouringPaths = None
    if not grid.random:
        neighbouringPaths = grid.getNeighbourPaths(pos, paths)
    if neighbouringPaths is None:
        return deleteRandomPath(paths, grid, pathData)
        
    ###############################################
    #
    # part for deleting a neighbouring path
    #
    ###############################################
    else:
        neighbouringPath = neighbouringPaths[randint(0,len(neighbouringPaths)-1)]
        [neighbourPath, index] = neighbouringPath
        start = Position.Position(neighbourPath[0][0], neighbourPath[1][0], neighbourPath[2][0])
        end = Position.Position(neighbourPath[0][-1], neighbourPath[1][-1], neighbourPath[2][-1])
        extraConnection = [start, end]
        
        # delete random path
        grid.deletePath(neighbourPath)
        del paths[index]
        
        # draw gates back
        grid.drawGates([[grid.getStart(), grid.getEnd()]], 4, 0)
        
        # delete 1's from grid (visited positions)    
        grid.deleteVisitedFromGrid(pathData.closedList)
        return extraConnection

def deleteRandomPath(paths, grid, pathData):
    # print "error: blocked path has no neighbours"
    randomNum = randint(0,len(paths)-1)
    randomPath = paths[randomNum]
    start = Position.Position(randomPath[0][0], randomPath[1][0], randomPath[2][0])
    end = Position.Position(randomPath[0][-1], randomPath[1][-1], randomPath[2][-1])
    extraConnection = [start, end]

    # delete random path
    grid.deletePath(randomPath)
    del paths[randomNum]
    
    # draw gates back
    grid.drawGates([[grid.getStart(), grid.getEnd()]], 4, 0)
    # delete 1's from grid (visited positions)    
    grid.deleteVisitedFromGrid(pathData.closedList)
    return extraConnection

    
# expand the open list with possible continuations
def expandOpenList(continuationList, endPos, pathData):
    for possiblePath in continuationList:
        
        # calculate cost and heuristic
        G = len(possiblePath) - 1
        H = Extra.calcDistance(possiblePath[-1], endPos)
        F = G + H
        
        # put path,cost and heuristic in the openList like [[path], F-score]
        pathData.putInOpenList(possiblePath, F)
    
# for all paths: delete the paths and reconnect it
def reMakeAllConnections(grid, paths):
    newPaths = []
    for path in paths:
        start = Position.Position(path[0][0], path[1][0], path[2][0])
        end = Position.Position(path[0][-1], path[1][-1], path[2][-1])
        grid.setStartEnd(start, end)
        grid.deletePath(path)
        
        path = findPath([start, end], grid, paths)
        if len(path) != 3:
            print "error: remaking failed to find path"
        newPaths.append(path)

    return newPaths
    
# sum up all the path lengths
def calcTotalPathLength(paths):
    length = 0
    for path in paths:
        if len(path) != 3:
            return "break"
        length += len(path[0])
    return length

# function to calculate an optimum total path length 
def calculateOptimum(length, width, height, connections):
    newTotalLength = 0
    for connection in connections:
        # create the grid
        newGrid = Grid.Grid(length,width,height)
        
        # put the gates in the grid
        newGrid.drawGates(connections, 4, 0)
        
        path = findPath(connection, newGrid, [])
        
        newTotalLength += len(path[0])
        
    # print result
    print "optimum length of paths: ", newTotalLength

def writeToCSV(totalLength, time, paths, fileName):
    with open(fileName, 'a') as csvfile:

        csvwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow([totalLength] + [time] + [paths])

