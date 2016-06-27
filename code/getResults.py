#!/usr/bin/env python
from Tkinter import *
import ttk
import netlists
import astar3D
import matplotlib
matplotlib.use('TkAgg')

import visualization
import csv
import Print

from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
import numpy as np

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import Position

import sys
if sys.version_info[0] < 3:
	import Tkinter as Tk
else:
	import tkinter as Tk


# red: #804000
# green: #408000
# blue: #004080
# purple: #400080

class App:
	def __init__(self, master):
		self.master = master
		self.buttonFrame = Frame()
		self.buttonFrame.pack(fill=X, padx=10, pady=20)

		self.setupPrintRB()
		self.setupConnections()
		self.setupIterations()
		self.setupButtons()
		self.setupPathSelection()

	def start(self):

		measures = self.getPrint()
		p = Print.getPrint2()

		# choose iterations
		iterations = self.iters.get()
		# choose deletion method
		randomOrNeighbour = "n"
		reMaking = True
		shortFirst = True

		successRates = []

		for connections in range(49, 51):

			# provide a .csv file name
			self.fileName = "print" + self.printvar.get() + "\\" + self.printvar.get() + "_" + str(connections) + ".csv"

			# [success, total iterations] (not being used at the moment)
			successRate = [0, 0]

			for i in range(iterations):
				nets = netlists.getRandomNetlist(p, connections)
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

	def setupPrintRB(self):
		self.printvar = StringVar(self.master)
		Label(self.buttonFrame, text="Print: ", font=("Helvetica", 12)).pack(side=LEFT)

		self.printvar.set("1") # default value
		w = OptionMenu(self.buttonFrame, self.printvar, "1", "2", "test")
		w.pack(side=LEFT)
		w.config(bg = "#94b8b8", activebackground="#c2d6d6")

	def getPrint(self):
		var = self.printvar.get()
		measures = []
		if var == "1":
			measures.append(18)
			measures.append(13)
			measures.append(7)
		if var == "2":
			measures.append(18)
			measures.append(17)
			measures.append(7)
		if var == "test":
			measures.append(6)
			measures.append(6)
			measures.append(6)			

		return measures

	def setupIterations(self):
		self.iters = Scale(self.buttonFrame, fg="#1f2e2e", label="No. of Iterations: ", from_=1, to=1000, orient=HORIZONTAL, troughcolor="white")
		self.iters.pack(side=LEFT)

	def setupConnections(self, *args):
		self.cons = Scale(self.buttonFrame, fg="#c2d6d6", label="Size of Netlist: ", troughcolor="white", from_=10, to=100, orient=HORIZONTAL, state="disabled", sliderrelief=SUNKEN)
		self.cons.pack(side=LEFT)

	def setupRandomFocus(self, *args):
		if self.netlistvar.get() == "random":
			self.cons.config(state="normal", sliderrelief=RAISED, fg="#1f2e2e")
		else:
			self.cons.config(state="disabled", sliderrelief=SUNKEN, fg="#c2d6d6")

	def setupButtons(self):
		self.button = Button(self.buttonFrame, text="QUIT", fg="red", command=lambda: self.quit())
		self.button.pack(side=RIGHT)
		self.button = Button(self.buttonFrame, text="GO!", highlightcolor="black", fg="#33cc33", command=lambda: self.start())
		self.button.pack(side=RIGHT)
		self.updateButton = Button(self.buttonFrame, state="disabled", text="update", command=lambda: self.setPaths(), relief="groove")
		self.updateButton.pack(side=RIGHT)

	def setupPathSelection(self):
		self.showPathsFrom = Scale(self.buttonFrame, sliderrelief=SUNKEN, state="disabled", fg="#c2d6d6", label="Paths from: ", troughcolor="white", from_=1, to=2, orient=HORIZONTAL, length=90)
		self.showPathsFrom.pack(side=LEFT)
		self.showPathsTo = Scale(self.buttonFrame, sliderrelief=SUNKEN, state="disabled", fg="#c2d6d6", label="To: ", troughcolor="white", from_=1, to=2, orient=HORIZONTAL, length=90)
		self.showPathsTo.pack(side=LEFT)
		self.showPathsTo.set(2)

	def enableShowPaths(self):
		maxPathLength = self.getLongestPath()
		self.showPathsFrom.config(state="normal", fg="#1f2e2e", from_=1, to=maxPathLength, sliderrelief=RAISED)
		self.showPathsTo.config(state="normal", fg="#1f2e2e", to=maxPathLength, sliderrelief=RAISED)
		self.showPathsTo.set(maxPathLength)
		self.updateButton.config(state="normal", relief="raised")

	def setPaths(self):
		newPaths = []
		for element in self.paths:
			if len(element[0]) >= self.showPathsFrom.get() and len(element[0]) <= self.showPathsTo.get():
				newPaths.append(element)
		visualization.plotAstar(self.v[0], self.v[1], self.v[2], newPaths, self.v[4])

	def getLongestPath(self):
		max = 0
		for path in self.paths:
			if len(path[0]) > max:
				max = len(path[0])
		return max


if __name__ == "__main__":

	root = Tk.Tk()
	root.wm_title("Chips & Circuits")

	app = App(root)

	root.mainloop()