#!/usr/bin/env python
from Tkinter import *
import ttk
import netlists
import astar3D
import matplotlib
matplotlib.use('TkAgg')
import numpy as np

import os.path

from random import randint
import ast

import visualization
import csv
import Print
import matplotlib.cm as cm

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler

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
		# pad=70
		# self._geom='200x200+0+0'
		# master.geometry("{0}x{1}+0+0".format(
		# 	master.winfo_screenwidth(), master.winfo_screenheight()-pad))

		# to keep track of if some action has been done
		self.iteration = 0
		self.pathsSet = 0
		self.selectedNetlist = 10

		# setup the frame
		self.master = master
		self.buttonFrame = Frame()
		self.buttonFrame.pack(fill=X, padx=10, pady=12)
		self.infoFrame = Frame(borderwidth=1, relief=GROOVE)
		self.infoFrame.pack(fill=X, padx=10, pady=7)

		# setup the possible actions for the user
		self.setupPrintRB()
		self.setupConnections()
		self.setupButtons()
		self.setupPathSelection()

		# show the initial graph with no specific point selected
		self.showInfoAndGraph()

		self.printvar.trace("w", lambda x, y, z: self.printChanged())

	def printChanged(self):
		# ugly code to make sure the path bounds are correct
		plotInfo = self.readData(self.cons.get())
		self.paths = ast.literal_eval(plotInfo[4])

		self.enableShowPaths()
		self.showInfoAndGraph()

	def showInfoAndGraph(self):
		# self.enableShowPaths()

		# replot the graph
		if self.iteration != 0:
			self.canvas.get_tk_widget().pack_forget()
			self.canvas2.get_tk_widget().pack_forget()

		noOfConnections = self.cons.get()

		self.showGraph(noOfConnections)

		self.showGrid()

		# show the info to the user
		plotInfo = self.readData(noOfConnections)
		self.showInfo(plotInfo)


	def onpick(self, event):
		print "hi"

	def showGraph(self, selected):
		f = plt.figure()
		a = f.add_subplot(111)
		a2 = a.twinx()

		f.canvas.mpl_connect('pick_event', self.onpick)

		# a tk.DrawingArea
		self.canvas = FigureCanvasTkAgg(f, self.master)
		self.canvas.show()
		self.canvas.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=1)

		averageTimes = [[], []]

		[colorTop, top] = self.getLengthAndColors()
		colors = cm.brg(np.linspace(0, 1, colorTop))

		# add half the color value
		colorAdd = (colorTop-1)/2

		SE = None

		for i in range(10, top):
			data = self.readData(i)
			if data[0]:
				
				# set marker size, extra large if selected
				s = 30
				if i == selected:
					s = 50
					SE, = a.plot((i, i), (100, 1100), 'r--', zorder=-1)

				# totalLengths errorbar
				x = [i] * len(data[0])
				y = data[0]
				a.errorbar(x, y, zorder=-1, c='k')

				# totalLengths errorbar
				x = i
				y = (sum(data[0])/float(len(data[0])))

				if i == 10:
					TL = a.scatter(x, y, c=colors[data[3][0] + colorAdd], s=s, zorder=3)
				else:
					a.scatter(x, y, c=colors[data[3][0] + colorAdd], s=s, zorder=0, picker=True)
				
				# save times
				averageTimes[0].append(i)
				averageTimes[1].append((sum(data[1])/float(len(data[1]))))

				#  constraint relaxation scatter
				x = i
				y = (sum(data[2])/float(len(data[2])))
				CR = a.scatter(x, y, c="blue", s=s, zorder=0, picker=True)

		# plot the average time
		Ti, = a2.plot(averageTimes[0], averageTimes[1], c="#cc9900", zorder=2, picker=True)

		plt.legend((TL, CR, Ti, SE),
		   ('Total Length (more red -> lower successrate)', 'Theoretical Minimum', 'Time', 'Selected Netlist'),
		   scatterpoints=1,
		   loc='upper left',
		   ncol=1,
		   fontsize=8)

		plt.title("Results of Random Netlists on Print " + self.printvar.get())

		a.set_xlabel('Amount of connections')
		a.set_ylabel('Average Total Length')
		a2.set_ylabel('Average Time(s)')

		a2.set_ylim(bottom=0)



	def getLengthAndColors(self):
		counter = 0
		colorTop = 0

		for i in range(10, 51):
			if i == 10:
				fileName = "print" + str(self.printvar.get()) + "\\" + self.printvar.get() + "_" + str(i) + ".csv"
				# read one file
				with open(fileName, 'rb') as csvfile:
					reader = csv.reader(csvfile, delimiter=',')
					for row in reader:
						colorTop += 1

			fileName = "print" + str(self.printvar.get()) + "\\" + self.printvar.get() + "_" + str(i) + ".csv"

			if os.path.isfile(fileName):
				counter += 1
		return [colorTop*2 + 1, counter + 10]

	def readData(self, i):
		times = []
		totalLengths = []
		cr = []
		successrate = []
		path = []

		fileName = "print" + str(self.printvar.get()) + "\\" + self.printvar.get() + "_" + str(i) + ".csv"

		# read one file
		with open(fileName, 'rb') as csvfile:
			reader = csv.reader(csvfile, delimiter=',')
			counter = 0
			for row in reader:
				if counter == 0:
					path = row[3]
				counter += 1
				totalLengths.append(float(row[0]))
				times.append(float(row[1]))
				cr.append(float(row[2]))
			successrate.append(counter)

		return [totalLengths, times, cr, successrate, path]

	def showInfo(self, plotInfo):
		# collect the info
		avTL = sum(plotInfo[0])/float(len(plotInfo[0]))
		avCR = sum(plotInfo[2])/float(len(plotInfo[2]))
		avTime = sum(plotInfo[1])/float(len(plotInfo[1]))

		# setup the labels
		if self.iteration == 0:
			self.ti = StringVar()
			self.to = StringVar()
			self.tim = StringVar()
			self.su = StringVar()
			self.op = StringVar()

			Label(self.infoFrame, textvariable=self.ti, pady=10, font=("Helvetica", 12)).pack(side=LEFT)
			self.ti.set(str(self.cons.get()) + " Random Connections" + "	|")
			Label(self.infoFrame, textvariable=self.to, font=("Helvetica", 10)).pack(side=LEFT)
			self.to.set("Average Total Length: " + str(round(avTL, 2)) + "	|")
			Label(self.infoFrame, textvariable=self.tim, font=("Helvetica", 10)).pack(side=LEFT)
			self.tim.set("Average Time(s): " + str(round(avTime, 2)) + "	|")
			Label(self.infoFrame, textvariable=self.su, font=("Helvetica", 10)).pack(side=LEFT)
			self.su.set("Succesrate: " + str((plotInfo[3][0]/10.0) * 100.0) + "%	|")
			Label(self.infoFrame, textvariable=self.op, font=("Helvetica", 10)).pack(side=LEFT)
			self.op.set("Optimality score: " + str(round(avCR/avTL, 2)) + "	")

			# remember that the label setup has been done
			self.iteration = 1
		else:
			self.ti.set(str(self.cons.get()) + " Random Connections" + "	|")
			self.to.set("Average Total Length: " + str(round(avTL, 2)) + "	|")
			self.tim.set("Average Time(s): " + str(round(avTime, 2)) + "	|")
			self.su.set("Succesrate: " + str((plotInfo[3][0]/10.0) * 100.0) + "%	|")
			self.op.set("Optimality score: " + str(round(avCR/avTL, 2)) + "	")

	def quit(self):
		root.quit()
		root.destroy()	

	def setupPrintRB(self):
		self.printvar = StringVar(self.master)
		Label(self.buttonFrame, text="Print: ", font=("Helvetica", 12)).pack(side=LEFT)

		self.printvar.set("1") # default value
		w = OptionMenu(self.buttonFrame, self.printvar, "1", "2", "3", "test")
		w.pack(side=LEFT)
		w.config(bg = "#94b8b8", activebackground="#c2d6d6")

	def getPrint(self):
		var = self.printvar.get()
		measures = []

		measures.append(18)
		measures.append(13)
		measures.append(7)

		return measures

	def setupConnections(self, *args):
		self.cons = Scale(self.buttonFrame, fg="#1f2e2e", label="Size of Netlist: ", troughcolor="white", from_=10, to=50, orient=HORIZONTAL)
		self.cons.pack(side=LEFT)

	def setupButtons(self):
		self.button = Button(self.buttonFrame, text="QUIT", fg="red", command=lambda: self.quit())
		self.button.pack(side=RIGHT)

	def setupPathSelection(self):
		self.showPathsFrom = Scale(self.buttonFrame, sliderrelief=SUNKEN, state="disabled", fg="#c2d6d6", label="Paths from: ", troughcolor="white", from_=1, to=2, orient=HORIZONTAL, length=90)
		self.showPathsFrom.pack(side=LEFT)
		self.showPathsTo = Scale(self.buttonFrame, sliderrelief=SUNKEN, state="disabled", fg="#c2d6d6", label="To: ", troughcolor="white", from_=1, to=2, orient=HORIZONTAL, length=90)
		self.showPathsTo.pack(side=LEFT)
		self.showPathsTo.set(2)
		# self.updateButton = Button(self.buttonFrame, text="SHOW GRID(Return key)", fg="#004d00", command=lambda: self.showGrid(), relief="raised")
		# self.updateButton.pack(side=LEFT)
		self.button = Button(self.buttonFrame, text="SELECT NETLIST SIZE(Arrow keys)", fg="#004d00", highlightcolor="black", command=lambda: self.showInfoAndGraph())
		self.button.pack(side=LEFT)

	def enableShowPaths(self):
		maxPathLength = self.getLongestPath()
		self.showPathsFrom.config(state="normal", fg="#1f2e2e", from_=1, to=maxPathLength, sliderrelief=RAISED)
		self.showPathsTo.config(state="normal", fg="#1f2e2e", to=maxPathLength, sliderrelief=RAISED)
		self.showPathsTo.set(maxPathLength)

	# def changeTo(self):
	# 	to = self.showPathsTo.get()
	# 	from_ = self.showPathsFrom.get()
	# 	print to
	# 	print from_
	# 	if to < from_:
	# 		self.showPathsTo.set(from_)

	def showGrid(self):
		plotInfo = self.readData(self.cons.get())
		self.paths = ast.literal_eval(plotInfo[4])

		# if the user never asked to show the grid before or asks for a new grid
		if self.pathsSet == 0 or self.selectedNetlist != self.cons.get():
			self.enableShowPaths()
			self.pathsSet = 1

		# remember the selected netlist
		self.selectedNetlist = self.cons.get()
		
		# prepare for the grid visualization
		measures = self.getPrint()

		printObject = Print.Print()
		defToCall = "getPrint" + self.printvar.get()
		gates = getattr(printObject, defToCall)()
		self.v = [measures[0], measures[1], measures[2], self.paths, gates]

		# select only the paths with the selected lengths
		newPaths = []
		for element in self.paths:
			if len(element[0]) >= self.showPathsFrom.get() and len(element[0]) <= self.showPathsTo.get():
				newPaths.append(element)

		self.visualizeGrid(self.v[0], self.v[1], self.v[2], newPaths, self.v[4])

	# embed an example grid of the selected size
	def visualizeGrid(self, length, width, height, paths, gates):
		f = plt.figure()
	
		# a tk.DrawingArea
		self.canvas2 = FigureCanvasTkAgg(f, self.master)
		self.canvas2.show()
		self.canvas2.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=1)

		ax = f.add_subplot(111, projection='3d')

		# create a color palette 
		colors = cm.nipy_spectral(np.linspace(0, 1, len(paths)))
		usedColors = []

		for path in paths:
			x = path[0]
			y = path[1]
			z = path[2]

			# to create a nice mix of colors: pick a random not used color
			randIndex = randint(0, len(colors)-1)
			while randIndex in usedColors:
				randIndex = randint(0, len(colors)-1)
			c = colors[randIndex]
			usedColors.append(randIndex)

			ax.plot(x, y, z, color=c, zorder=-1)
		x = []
		y = []
		z = []
		for gate in gates:
			x.append(gate.getX())
			y.append(gate.getY())
			z.append(gate.getZ())

		ax.scatter(x, y, z, c='black', marker="s", s=60, zorder=10)

		ax.set_xlim3d([length-1, 0])
		ax.set_ylim3d([0, width-1])
		ax.set_zlim3d([0, height-1])

		ax.set_xlabel('X')
		ax.set_ylabel('Y')
		ax.set_zlabel('Layer')
		
		title = str(len(paths)) + " Random Connections"
		plt.title(title)		

	def getLongestPath(self):
		max = 0
		for path in self.paths:
			if len(path[0]) > max:
				max = len(path[0])
		return max

	def leftKey(self, event):
		plt.close('all')
		self.cons.set(self.cons.get() - 1)
		self.showInfoAndGraph()

	def rightKey(self, event):
		plt.close('all')
		self.cons.set(self.cons.get() + 1)
		self.showInfoAndGraph()

	def returnKey(self, event):
		self.showGrid()		

if __name__ == "__main__":

	root = Tk.Tk()
	root.wm_title("Chips & Circuits")

	root.wm_state('zoomed')

	app = App(root)
	root.after(1, lambda: root.focus_force())

	root.bind('<Left>', app.leftKey)
	root.bind('<Right>', app.rightKey)
	root.bind('<Return>', app.returnKey)

	root.mainloop()