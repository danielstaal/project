'''
Executable file Chips & Circuits
Date: 26/05/2016
Daniel Staal

This program allows the user to choose a print, netlist, search methods and 
a filename to output the result


To execute this program:        python chips_exe.py
'''


import astar3D
import netlists
import time
import sys

if __name__ == "__main__":
    
    print ""
    print "Welcome to Chips & Circuits! Please give the starting variables:"
    print ""

    measures = []
    netlist = None
    
    # choose print
    printNo = int(raw_input("print(1 or 2): "))
    if printNo == 1:
        # dimentions of the grid
        # print #1
        measures.append(18)
        measures.append(13)
        measures.append(7)
    elif printNo == 2:
        # print #2
        measures.append(18)
        measures.append(17)
        measures.append(7)
    else:
        measures.append(6)
        measures.append(6)
        measures.append(6)

    # choose netlist
    netlistNo = int(raw_input("netlist(1, 2 or 3): "))
    if netlistNo == 1:
        netlists = netlists.getNetlist1()
    elif netlistNo == 2:
        netlists = netlists.getNetlist2()
    elif netlistNo == 3:
        netlists = netlists.getNetlist3()
    else:
        netlists = netlists.getNetlistTest()

    netlist = netlists[0]
    gates = netlists[1]

    # choose iterations
    iterations = int(raw_input("number of iterations: "))

    # choose deletion method
    randomOrNeighbour = "n" #raw_input("random or neighbour deletion(r or n): ")

    # hill climber or not
    reMaking = "y"#raw_input("Remaking(y or n): ")
    # if reMaking == "y":
    #     reMaking = True
    # else:
    #     reMaking = False

    # sort from shortest to longest before connecting?
    shortFirst = "y"# raw_input("Shortfirst(y or n): ")
    # if shortFirst == "y":
    #     shortFirst = True
    # else:
    #     shortFirst = False
    
    # provide a .csv file name
    fileName = raw_input("csv file name: ")
        
    # execute the algorithm with the given parameters
    astar3D.executeAlgorithm(measures, netlist, gates, iterations, fileName, randomOrNeighbour, reMaking, shortFirst)