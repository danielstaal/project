#!/usr/bin/env python
from Tkinter import *
import ttk
import netlists
import astar3D
import matplotlib
matplotlib.use('TkAgg')

import ast

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

		self.setupFromDatabase()
		self.setupPrintRB()
		self.setupNetlistRB()
		self.setupConnections()
		self.setupIterations()
		self.setupButtons()
		self.netlistvar.trace('w', self.setupRandomFocus)
		self.setupPathSelection()

		self.showGraph([[], []])

	def start(self):
		self.canvas.get_tk_widget().pack_forget()

		# if database checkbox is checked
		if self.database.get():
			self.getOldData()

		else:
			self.getNewData()

	def getOldData(self):
		self.fileName = "database\\" + self.printvar.get() + "_" + str(self.cons.get()) + ".csv"

		plotInfo = self.getPlot()
		paths = ast.literal_eval(plotInfo[2])

		measures = self.getPrint()
		nets = self.getNetlist()
		netlist = nets[0]
		gates = nets[1]

		self.showGraph(plotInfo)
		plt.close('all')

		self.v = [measures[0], measures[1], measures[2], paths, gates]

		visualization.plotAstar(self.v[0], self.v[1], self.v[2], self.v[3], self.v[4])
		
		self.paths = paths
		self.enableShowPaths()

	def getNewData(self):
		measures = self.getPrint()
		nets = self.getNetlist()
		netlist = nets[0]
		gates = nets[1]

		# choose iterations
		iterations = self.iters.get()
		# choose deletion method
		randomOrNeighbour = "n"
		reMaking = True
		shortFirst = True
		# provide a .csv file name
		self.fileName = 'tograph.csv'

		# execute the algorithm with the given parameters
		self.v = astar3D.executeAlgorithm(measures, netlist, gates, iterations, self.fileName, randomOrNeighbour, reMaking, shortFirst)
		# print self.getNetlist()
		self.showGraph(self.getPlot())
		plt.close('all')

		visualization.plotAstar(self.v[0], self.v[1], self.v[2], self.v[3], self.v[4])
		
		self.paths = self.v[3]
		self.enableShowPaths()

	def showGraph(self, toPlot):
 		f = plt.figure()
		a = f.add_subplot(211)

		# plt.plot(toPlot[0], toPlot[1])
		plt.hist(toPlot[1], facecolor='green')
		a.set_xlabel('Time(s)')
		a.set_ylabel('Count')

		b = f.add_subplot(212)
		plt.hist(toPlot[0], facecolor='green')
		b.set_xlabel('TotalLength')
		b.set_ylabel('Count')

		# a tk.DrawingArea
		self.canvas = FigureCanvasTkAgg(f, self.master)
		self.canvas.show()
		self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

	def getPlot(self):
		times = []
		totalLengths = []
		toVisualize = []
		with open(self.fileName, 'rb') as csvfile:
			reader = csv.reader(csvfile, delimiter=',')
			counter = 0
			for row in reader:
				if counter == 0:
					toVisualize = row[2]
				counter = 1
				totalLengths.append(float(row[0]))
				times.append(float(row[1]))

		return [totalLengths, times, toVisualize]

	def quit(self):
		root.quit()
		root.destroy()	

	def setupFromDatabase(self):
		self.database = IntVar()
		self.fromDatabaseButton = Checkbutton(self.buttonFrame, text="From Database", variable=self.database, command=self.setRandom)
		self.fromDatabaseButton.pack(side=LEFT)

	def setRandom(self):
		self.netlistvar.set("random")z

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

	def setupNetlistRB(self):
		self.netlistvar = StringVar(self.master)
		Label(self.buttonFrame, text="Netlist: ", font=("Helvetica", 12)).pack(side=LEFT)

		self.netlistvar.set("1") # default value
		w = OptionMenu(self.buttonFrame, self.netlistvar, "1", "2", "3", "test", "random")
		w.pack(side=LEFT)
		w.config(bg = "#94b8b8", activebackground="#c2d6d6")

	def getNetlist(self):
		var = self.netlistvar.get()
		if var == "1":
			nets = netlists.getNetlist1()
		elif var == "2":
			nets = netlists.getNetlist2()
		elif var == "3":
			nets = netlists.getNetlist3()
		elif var == "test":
			nets = netlists.getNetlistTest()
		elif var == "random":
			p = Print.getPrint1()
			nets = netlists.getRandomNetlist(p, self.cons.get())
		return nets

	def setupIterations(self):
		self.iters = Scale(self.buttonFrame, fg="#1f2e2e", label="No. of Iterations: ", from_=1, to=100, orient=HORIZONTAL, troughcolor="white")
		self.iters.pack(side=LEFT)

	def setupConnections(self, *args):
		self.cons = Scale(self.buttonFrame, fg="#c2d6d6", label="Size of Netlist: ", troughcolor="white", from_=10, to=50, orient=HORIZONTAL, state="disabled", sliderrelief=SUNKEN)
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

	# def changeTo(self):
	# 	to = self.showPathsTo.get()
	# 	from_ = self.showPathsFrom.get()
	# 	print to
	# 	print from_
	# 	if to < from_:
	# 		self.showPathsTo.set(from_)

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