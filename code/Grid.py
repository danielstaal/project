'''
3-dimensional grid
Date: 26/05/2016
Daniel Staal

This class keeps track of the 3-dimensional grid and computes all actions that
have anything to do or need information from the current grid. One grid is used
to find a solution for all the connections.

class variables:
    grid (3D list)
        length
        width
        height
'''

import copy
import Position
from random import randint


class Grid:
    # dus dit is voor het maken van het grid van 17 bij 12
    def __init__(self, length, width, height):
        self.grid = [[[0 for x in range(height)] for x in range(width)] for x in range(length)]
        self.length = length
        self.width = width
        self.height = height
        self.reMaking = False
    
    def setReMaking(self, flag):
        self.reMaking = flag
        
    def getReMaking(self):
        return self.reMaking
    
    def setPointToValue(self, position, value):
        self.grid[position.getX()][position.getY()][position.getZ()] = value
      
    def setStartEnd(self, startPos, endPos):
        self.start = startPos
        self.end = endPos
        self.drawGates([[startPos, endPos]], 0, 0)
        
        
    # draw the gates in the grid    
    def drawGates(self, connections, gateValue, gateAdjacentValue):
        for connection in connections:
            for gate in connection:
                self.setPointToValue(gate, gateValue)
                        
    def getStart(self):
        return self.start
    
    def getEnd(self):
        return self.end
    
    # find all possible next paths in the grid
    def getPossibleNextPaths(self, currentPath, pathData):
        nextPaths = []
        x = currentPath[-1].getX()
        y = currentPath[-1].getY()
        z = currentPath[-1].getZ()
        
        options = [[x + 1, y, z], [x - 1, y, z], [x, y + 1, z], [x, y - 1, z], [x, y, z + 1], [x, y, z - 1]]
        for option in options:
            x = option[0]
            y = option[1]
            z = option[2]

            if x <= self.length-1 and y <= self.width-1 and z <= self.height-1 and x >= 0 and y >= 0 and z >= 0 and \
            self.grid[x][y][z] == 0 and not (pathData.inClosedList(Position.Position(x, y, z))):
                possiblePath = copy.deepcopy(currentPath)
                possiblePath.append(Position.Position(x, y, z))
                nextPaths.append(possiblePath)
          
        return nextPaths
        
    def drawPath(self, path, closedList):
        x = []
        y = []
        z = []
        self.deleteVisitedFromGrid(closedList)
        
        for step in path:
            self.grid[step.getX()][step.getY()][step.getZ()] = 2
            x.append(step.getX())
            y.append(step.getY())
            z.append(step.getZ())
        self.drawGates([[path[0], path[-1]]], 4, 0)
        return [x,y,z]
        
    def deleteVisitedFromGrid(self, closedList):
        for pos in closedList:
            if self.grid[pos.getX()][pos.getY()][pos.getZ()] == 1:
                self.setPointToValue(pos, 0)

    def deletePath(self, path):
        for pos in range(1,len(path[0])-1):
            self.grid[path[0][pos]][path[1][pos]][path[2][pos]] = 0
    
    
    ##############################################
    #
    # part for finding a neighbouring path
    #
    ##############################################
    
    # search for a neighbouring path
    def getNeighbourPaths(self, pos, paths):
    
        x = pos.getX()
        y = pos.getY()
        z = pos.getZ()
        
        neighbouringPaths = []
        
        # look in all directions
        options = [[x + 1, y, z], [x - 1, y, z], [x, y + 1, z], [x, y - 1, z], [x, y, z + 1], [x, y, z - 1]]
        for option in options:
            x = option[0]
            y = option[1]
            z = option[2]
            if x <= self.length-1 and y <= self.width-1 and z <= self.height-1 and x >= 0 and y >= 0 and z >= 0 and self.grid[x][y][z] == 2:
                neighbouringPaths.append(self.searchPath(Position.Position(x,y,z), paths))
        
        if len(neighbouringPaths) == 0:
            return None
        return neighbouringPaths

    # loop over all paths
    def searchPath(self, pos, paths):
        index = 0
        for path in paths:
            if self.isPosInPath(pos, path):
                return [path, index]
            index += 1
        print "no neighbour path found error"
            
    # check in which path the position is
    def isPosInPath(self, pos, path):
        for i in range(len(path[0])):
            if path[0][i] == pos.getX() and path[1][i] == pos.getY() and path[2][i] == pos.getZ():
                return True
        return False   
    
    def randomUp(self, currentPath, pathData):
        x = currentPath[-1].getX()
        y = currentPath[-1].getY()
        z = currentPath[-1].getZ()
        upz = z + 1
        if upz <= self.height-1 and self.grid[x][y][upz] == 0 and not (pathData.inClosedList(Position.Position(x, y, upz))):
            upPath = copy.deepcopy(currentPath)
            upPath.append(Position.Position(x, y, upz))
            return upPath
        else:
            return currentPath
        
    def setRandomOrNeighbour(self, flag):
        if flag == "r":
            self.random = True
        else:
            self.random = False