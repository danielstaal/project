'''
netlists file
Date: 26/05/2016
Daniel Staal, Eelco Alink, Amar Skenderovic

This file has only one purpose: return the netlist that the user chose
'''

import Position
from random import randint
import copy
import sys


def getRandomNetlist(gates, noOfConnections):

    countOccurrences = [6]
    netlist = []

    while max(countOccurrences) > 5:
        countOccurrences = [0] * len(gates)
        netlist = []
        # print "too many connections at gate"
        for connection in range(noOfConnections):
            i_startgate = randint(0, len(gates)-1)
            i_endgate = randint(0, len(gates)-1)
            while i_startgate == i_endgate:
                i_startgate = randint(0, len(gates)-1)
                i_endgate = randint(0, len(gates)-1)

            start = gates[i_startgate]
            countOccurrences[i_startgate] += 1
            end = gates[i_endgate]
            countOccurrences[i_endgate] += 1
            netlist.append([start, end])

    return [netlist, gates]


def updateNetlist(netlist):
    # length = len(netlist)
    elements = [item for sublist in netlist for item in sublist]
    # print len(elements)
    
    gates = []
    for element in elements:
        if elementIsNotInGates(element, gates):
            gates.append(element)
            
    # # create the available directions for each gate
    # availableList = setAvailable(gates)

    # # set the new connections
    # newNetlist = changeConnections(availableList, netlist, gates)
    
    return [netlist, gates]
    
# def setAvailable(gates):
#     availableList = []
#     availableSet = []
#     for element in gates:
#         gate = []
#         x = element.getX()
#         y = element.getY()
#         z = element.getZ()
#         options = [[x + 1, y, z], [x, y + 1, z], [x, y, z + 1], [x - 1, y, z], [x, y - 1, z]]
#         for option in options:
#             if option not in availableSet:
#                 gate.append(option)
#                 availableSet.append(option)
#         availableList.append(gate)
#     return availableList

# def changeConnections(availableList, netlist, gates):
#     newConnections = []
#     for connection in netlist:
#         index = getIndex(connection[0], gates)

#         option = availableList[index][0]
#         start = Position.Position(option[0], option[1], option[2])
#         availableList[index].pop(0)
        
#         index = getIndex(connection[1], gates)
#         option = availableList[index][0]
#         end = Position.Position(option[0], option[1], option[2])
#         availableList[index].pop(0)

#         newConnections.append([start, end])
#     return newConnections
        
def getIndex(position, gates):
    counter = 0
    for element in gates:
        if position.getX() == element.getX() and position.getY() == element.getY() and position.getZ() == element.getZ():
            return counter
        counter += 1
            
def elementIsNotInGates(element, list):
    for item in list:
        if element.getX() == item.getX() and element.getY() == item.getY() and element.getZ() == item.getZ():
            return False
    return True

# print 1
# lengte 30
def getNetlist1():
    netlist = [[Position.Position(1,11,0), Position.Position(3,2,0)], 
    [Position.Position(12,2,0), Position.Position(12,3,0)], 
    [Position.Position(6,1,0),  Position.Position(1,1,0)], 
    [Position.Position(2,8,0),  Position.Position(2,10,0)], 
    [Position.Position(15,1,0), Position.Position(12,2,0)], 
    [Position.Position(12,3,0), Position.Position(13,7,0)], 
    [Position.Position(15,1,0), Position.Position(1,11,0)], 
    [Position.Position(1,11,0), Position.Position(8,4,0)], 
    [Position.Position(9,10,0), Position.Position(13,7,0)],
    [Position.Position(2,8,0),  Position.Position(9,8,0)],
    [Position.Position(1,9,0),  Position.Position(4,5,0)], 
    [Position.Position(2,8,0),  Position.Position(8,4,0)], 
    [Position.Position(13,7,0), Position.Position(11,8,0)], 
    [Position.Position(15,8,0), Position.Position(10,1,0)], 
    [Position.Position(9,10,0), Position.Position(11,5,0)], 
    [Position.Position(4,5,0),  Position.Position(3,2,0)],
    [Position.Position(11,5,0), Position.Position(12,11,0)], 
    [Position.Position(15,1,0), Position.Position(2,8,0)], 
    [Position.Position(10,1,0), Position.Position(1,9,0)], 
    [Position.Position(15,1,0), Position.Position(3,2,0)], 
    [Position.Position(1,9,0),  Position.Position(15,8,0)], 
    [Position.Position(6,8,0),  Position.Position(1,5,0)], 
    [Position.Position(15,8,0), Position.Position(12,2,0)], 
    [Position.Position(15,1,0), Position.Position(1,1,0)],
    [Position.Position(2,8,0),  Position.Position(12,2,0)],
    [Position.Position(12,3,0), Position.Position(1,5,0)], 
    [Position.Position(1,5,0),  Position.Position(13,7,0)], 
    [Position.Position(4,5,0),  Position.Position(12,3,0)],
    [Position.Position(9,10,0), Position.Position(6,8,0)],
    [Position.Position(14,2,0), Position.Position(16,7,0)]]
    return updateNetlist(netlist)
    # return netlist

# print 1
# lengte 40
def getNetlist2():
    netlist = [[Position.Position(16,5,0), Position.Position(1,9,0)], 
    [Position.Position(1,11,0),  Position.Position(1,9,0)], 
    [Position.Position(14,2,0),  Position.Position(1,5,0)], 
    [Position.Position(2,8,0),   Position.Position(4,5,0)], 
    [Position.Position(16,5,0),  Position.Position(13,7,0)], 
    [Position.Position(8,4,0),   Position.Position(11,8,0)], 
    [Position.Position(6,1,0),   Position.Position(9,10,0)], 
    [Position.Position(4,5,0),   Position.Position(1,9,0)], 
    [Position.Position(3,2,0),   Position.Position(15,1,0)], 
    [Position.Position(4,5,0),   Position.Position(12,2,0)], 
    [Position.Position(9,8,0),   Position.Position(11,5,0)], 
    [Position.Position(6,1,0),   Position.Position(2,10,0)], 
    [Position.Position(9,10,0),  Position.Position(8,4,0)], 
    [Position.Position(9,10,0),  Position.Position(4,5,0)], 
    [Position.Position(15,8,0),  Position.Position(8,4,0)], 
    [Position.Position(13,7,0),  Position.Position(15,8,0)], 
    [Position.Position(4,5,0),   Position.Position(3,2,0)], 
    [Position.Position(1,5,0),   Position.Position(1,11,0)], 
    [Position.Position(9,10,0),  Position.Position(11,8,0)], 
    [Position.Position(6,8,0),   Position.Position(2,10,0)], 
    [Position.Position(3,2,0),   Position.Position(1,1,0)], 
    [Position.Position(11,8,0),  Position.Position(2,10,0)], 
    [Position.Position(12,2,0),  Position.Position(9,8,0)], 
    [Position.Position(8,4,0),   Position.Position(1,11,0)], 
    [Position.Position(11,8,0),  Position.Position(13,7,0)], 
    [Position.Position(13,7,0),  Position.Position(11,5,0)], 
    [Position.Position(11,5,0),  Position.Position(12,3,0)], 
    [Position.Position(16,7,0),  Position.Position(12,3,0)], 
    [Position.Position(16,7,0),  Position.Position(14,2,0)], 
    [Position.Position(16,7,0),  Position.Position(6,1,0)], 
    [Position.Position(12,11,0), Position.Position(16,5,0)], 
    [Position.Position(11,5,0),  Position.Position(2,8,0)], 
    [Position.Position(10,1,0),  Position.Position(12,2,0)], 
    [Position.Position(11,5,0),  Position.Position(16,5,0)], 
    [Position.Position(1,1,0),   Position.Position(2,8,0)], 
    [Position.Position(16,7,0),  Position.Position(12,2,0)], 
    [Position.Position(2,8,0),   Position.Position(3,2,0)], 
    [Position.Position(15,8,0),  Position.Position(1,5,0)], 
    [Position.Position(15,1,0),  Position.Position(1,1,0)], 
    [Position.Position(2,8,0),   Position.Position(13,7,0)]]
    # updateNetlist(netlist)
    return updateNetlist(netlist)

    
# print 1
# lengte 50
def getNetlist3():
    netlist = [[Position.Position(1,1,0), Position.Position(13,7,0)], 
    [Position.Position(1,1,0), Position.Position(16,7,0)], 
    [Position.Position(1,1,0), Position.Position(9,10,0)], 
    [Position.Position(8,4,0), Position.Position(12,3,0)], 
    [Position.Position(10,1,0), Position.Position(14,2,0)], 
    [Position.Position(15,1,0), Position.Position(15,8,0)], 
    [Position.Position(15,1,0), Position.Position(1,5,0)], 
    [Position.Position(3,2,0), Position.Position(8,4,0)], 
    [Position.Position(3,2,0), Position.Position(1,5,0)], 
    [Position.Position(12,2,0), Position.Position(16,7,0)], 
    [Position.Position(14,2,0), Position.Position(3,2,0)], 
    [Position.Position(3,2,0), Position.Position(6,1,0)], 
    [Position.Position(12,3,0), Position.Position(1,11,0)], 
    [Position.Position(4,5,0), Position.Position(1,1,0)], 
    [Position.Position(4,5,0), Position.Position(6,1,0)], 
    [Position.Position(8,4,0), Position.Position(6,1,0)], 
    [Position.Position(12,3,0), Position.Position(12,2,0)], 
    [Position.Position(16,5,0), Position.Position(16,7,0)], 
    [Position.Position(13,7,0), Position.Position(10,1,0)], 
    [Position.Position(8,4,0), Position.Position(4,5,0)], 
    [Position.Position(11,5,0), Position.Position(1,1,0)], 
    [Position.Position(11,5,0), Position.Position(9,8,0)], 
    [Position.Position(11,5,0), Position.Position(15,1,0)], 
    [Position.Position(8,4,0), Position.Position(1,5,0)], 
    [Position.Position(16,5,0), Position.Position(12,11,0)], 
    [Position.Position(13,7,0), Position.Position(3,2,0)], 
    [Position.Position(13,7,0), Position.Position(15,8,0)], 
    [Position.Position(2,8,0), Position.Position(2,10,0)], 
    [Position.Position(4,5,0), Position.Position(15,1,0)], 
    [Position.Position(11,8,0), Position.Position(4,5,0)], 
    [Position.Position(12,11,0), Position.Position(1,11,0)], 
    [Position.Position(6,8,0), Position.Position(12,3,0)], 
    [Position.Position(9,8,0), Position.Position(2,8,0)], 
    [Position.Position(9,8,0), Position.Position(2,10,0)], 
    [Position.Position(9,8,0), Position.Position(1,5,0)], 
    [Position.Position(11,8,0), Position.Position(1,9,0)], 
    [Position.Position(11,8,0), Position.Position(10,1,0)], 
    [Position.Position(16,5,0), Position.Position(1,5,0)], 
    [Position.Position(6,1,0), Position.Position(13,7,0)], 
    [Position.Position(15,8,0), Position.Position(2,10,0)], 
    [Position.Position(1,9,0), Position.Position(14,2,0)], 
    [Position.Position(6,1,0), Position.Position(2,8,0)], 
    [Position.Position(10,1,0), Position.Position(6,8,0)], 
    [Position.Position(1,9,0), Position.Position(6,8,0)], 
    [Position.Position(9,10,0), Position.Position(11,5,0)], 
    [Position.Position(9,10,0), Position.Position(11,8,0)], 
    [Position.Position(10,1,0), Position.Position(15,1,0)], 
    [Position.Position(12,2,0), Position.Position(16,5,0)], 
    [Position.Position(12,11,0), Position.Position(2,8,0)], 
    [Position.Position(12,11,0), Position.Position(6,8,0)]]
    # updateNetlist(netlist)
    return updateNetlist(netlist)

# print 1
# lengte 50
# lijst met gate nummers erbij
def getSortedNetlist3():
    return [[[0, Position.Position(1,1,0)], [10, Position.Position(4,5,0)]],
    [[0, Position.Position(1,1,0)], [11, Position.Position(11,5,0)]],
    [[0, Position.Position(1,1,0)], [13, Position.Position(13,7,0)]],
    [[0, Position.Position(1,1,0)], [14, Position.Position(16,7,0)]],
    [[0, Position.Position(1,1,0)], [22, Position.Position(9,10,0)]],
    [[1, Position.Position(6,1,0)], [4, Position.Position(3,2,0)]],
    [[1, Position.Position(6,1,0)], [8, Position.Position(8,4,0)]],
    [[1, Position.Position(6,1,0)], [10, Position.Position(4,5,0)]],
    [[1, Position.Position(6,1,0)], [13, Position.Position(13,7,0)]],
    [[1, Position.Position(6,1,0)], [15, Position.Position(2,8,0)]],
    [[2, Position.Position(10,1,0)], [3, Position.Position(15,1,0)]],
    [[2, Position.Position(10,1,0)], [6, Position.Position(14,2,0)]],
    [[2, Position.Position(10,1,0)], [13, Position.Position(13,7,0)]],
    [[2, Position.Position(10,1,0)], [16, Position.Position(6,8,0)]],
    [[3, Position.Position(15,1,0)], [9, Position.Position(1,5,0)]],
    [[3, Position.Position(15,1,0)], [10, Position.Position(4,5,0)]],
    [[3, Position.Position(15,1,0)], [11, Position.Position(11,5,0)]],
    [[3, Position.Position(15,1,0)], [19, Position.Position(15,8,0)]],
    [[4, Position.Position(3,2,0)], [6, Position.Position(14,2,0)]],
    [[4, Position.Position(3,2,0)], [8, Position.Position(8,4,0)]],
    [[4, Position.Position(3,2,0)], [9, Position.Position(1,5,0)]],
    [[4, Position.Position(3,2,0)], [13, Position.Position(13,7,0)]],
    [[5, Position.Position(12,2,0)], [7, Position.Position(12,3,0)]],
    [[5, Position.Position(12,2,0)], [12, Position.Position(16,5,0)]],
    [[5, Position.Position(12,2,0)], [14, Position.Position(16,7,0)]],
    [[6, Position.Position(14,2,0)], [20, Position.Position(1,9,0)]],
    [[7, Position.Position(12,3,0)], [8, Position.Position(8,4,0)]],
    [[7, Position.Position(12,3,0)], [16, Position.Position(6,8,0)]],
    [[7, Position.Position(12,3,0)], [23, Position.Position(1,11,0)]],
    [[8, Position.Position(8,4,0)], [9, Position.Position(1,5,0)]],
    [[8, Position.Position(8,4,0)], [10, Position.Position(4,5,0)]],
    [[9, Position.Position(1,5,0)], [12, Position.Position(16,5,0)]],
    [[9, Position.Position(1,5,0)], [17, Position.Position(9,8,0)]],
    [[10, Position.Position(4,5,0)], [18, Position.Position(11,8,0)]],
    [[11, Position.Position(11,5,0)], [17, Position.Position(9,8,0)]],
    [[11, Position.Position(11,5,0)], [22, Position.Position(9,10,0)]],
    [[12, Position.Position(16,5,0)], [14, Position.Position(16,7,0)]],
    [[12, Position.Position(16,5,0)], [24, Position.Position(12,11,0)]],
    [[13, Position.Position(13,7,0)], [19, Position.Position(15,8,0)]],
    [[15, Position.Position(2,8,0)], [17, Position.Position(9,8,0)]],
    [[15, Position.Position(2,8,0)], [21, Position.Position(2,10,0)]],
    [[15, Position.Position(2,8,0)], [24, Position.Position(12,11,0)]],
    [[16, Position.Position(6,8,0)], [20, Position.Position(1,9,0)]],
    [[16, Position.Position(6,8,0)], [24, Position.Position(12,11,0)]],
    [[17, Position.Position(9,8,0)], [21, Position.Position(2,10,0)]],
    [[18, Position.Position(11,8,0)], [2, Position.Position(10,1,0)]],
    [[18, Position.Position(11,8,0)], [20, Position.Position(1,9,0)]],
    [[18, Position.Position(11,8,0)], [22, Position.Position(9,10,0)]],
    [[19, Position.Position(15,8,0)], [21, Position.Position(2,10,0)]],
    [[23, Position.Position(1,11,0)], [24, Position.Position(12,11,0)]]]

def getNetlistTest():
    netlist = [
    # [Position.Position(1,1,0), Position.Position(16,11,0)],
    # [Position.Position(1,1,0), Position.Position(4,4,0)],
    # [Position.Position(1,1,0), Position.Position(4,4,0)],
    # [Position.Position(1,1,0), Position.Position(4,4,0)],
    # [Position.Position(1,1,0), Position.Position(4,4,0)],
    # [Position.Position(1,4,0), Position.Position(4,1,0)],
    [Position.Position(1,4,0), Position.Position(4,1,0)],
    [Position.Position(1,4,0), Position.Position(4,1,0)],
    [Position.Position(1,4,0), Position.Position(4,1,0)]]
    return updateNetlist(netlist)