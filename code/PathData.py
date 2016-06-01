'''
file to keep track of A* path information
Date: 26/05/2016
Daniel Staal

This class keeps track of all the data of a single path to be computed by A*.
Every new connection called from astar3D starts with a new PathData object.

class variables:
    openList
    closedList
'''

import Extra
import sys
import Position
import visualization

class PathData:    
    def __init__(self):
        # list of paths that can be continued, containing: a path and Fscore
        self.openList = []
        # List of coordinates already visited 
        self.closedList = []
    
    # function to put a path as openPath in the open list
    def putInOpenList(self, path, F):
        self.openList.append([path, F])
        
    # function to put an element in the closed list
    def putInClosedList(self, pos):
        self.deleteFromOpenList(pos)
        self.closedList.append(pos)
    
    # function to check if a position is in the closed list
    def inClosedList(self, position):
        for element in self.closedList:
            if element.getX() == position.getX() and element.getY() == position.getY() and element.getZ() == position.getZ():
                return True
        return False 
    
    # function to delete element from the open list
    def deleteFromOpenList(self, position):
        counter = 0
        for element in self.openList:
            if position.getX() == element[0][-1].getX() and position.getY() == element[0][-1].getY() and position.getZ() == element[0][-1].getZ():
                del self.openList[counter]
            counter += 1

    def getLowestFScore(self, currentPos, endPos, paths, grid):
        
        if len(self.openList) == 0:
            # print "Connection blocked at connection: ", currentPos.getX(), currentPos.getY(), currentPos.getZ()
            # print "to: ", endPos.getX(), endPos.getY(), endPos.getZ()
            # print "number of assigned paths: ", len(paths)
            # print paths

            return "blocked"
  
        if(len(self.openList) > 300):
            return "turnaround"
  
        else:
            lowestFscore = 10000
            H = 10000
            for possiblePath in self.openList:
                newH = Extra.calcDistance(possiblePath[0][-1], endPos)
                if (possiblePath[1] < lowestFscore) or (possiblePath[1] == lowestFscore and newH < H):
                    lowestFscore = possiblePath[1]
                    H = newH
                    bestPath = possiblePath[0]
        return bestPath