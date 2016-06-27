#!/usr/bin/env python
import netlists
import astar3D

import csv
import Print

from numpy import arange, sin, pi

import numpy as np

import time
import datetime

import Position

import sys

# red: #804000
# green: #408000
# blue: #004080
# purple: #400080

class App:
	def __init__(self, args):
		printObject = Print.Print()
		defToCall = "getPrint" + args[1]
		self.p = getattr(printObject, defToCall)()

		self.pr = args[1]
		self.from_ = args[2]

		self.start()


	def start(self):

		measures = self.getPrint()

		# choose iterations
		iterations = 10
		# choose deletion method
		randomOrNeighbour = "n"
		reMaking = True
		shortFirst = True

		successRates = []

		timestart = time.time()

		for connections in range(int(self.from_), 51):
			print "No of Connections: ", connections

			print "Starting time: ", datetime.datetime.now().time()

			# provide a .csv file name
			self.fileName = "print" + self.pr + "\\" + self.pr + "_" + str(connections) + ".csv"

			# [success, total iterations] (not being used at the moment)
			successRate = [0, 0]

			for i in range(iterations):
				nets = netlists.getRandomNetlist(self.p, connections)
				netlist = nets[0]
				gates = nets[1]
				success = astar3D.executeAlgorithm(measures, netlist, gates, 1, self.fileName, randomOrNeighbour, reMaking, shortFirst)
				successRate[1] += 1 
				if success:
					successRate[0] += 1
			successRates.append(successRate)

	def quit(self):
		root.quit()
		root.destroy()	

	def getPrint(self):
		measures = []
		measures.append(18)
		measures.append(13)
		measures.append(7)		

		return measures


if __name__ == "__main__":
	app = App(sys.argv)

