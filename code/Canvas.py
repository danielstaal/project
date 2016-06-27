import visualization


from Tkinter import *
import netlists
import astar3D
import matplotlib
matplotlib.use('TkAgg')

from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler


from matplotlib.figure import Figure
class App:

	def __init__(self, master):

		self.master = master

		# title = Label(self.master, text="Chips & Circuits", font=("Helvetica", 16))
		# title.grid(row=0, column=1)

		self.setupPrintRB()
		self.setupNetlistRB()
		# self.setupIterations()

		self.button = Button(master, text="GO!", fg="green", command=self.start)
		self.button.grid(row=4, column=2)
		self.button = Button(self.master, text="QUIT", fg="red", command=self.quit)
		self.button.grid(row=4, column=3)


	def start(self):
		measures = self.getPrint()
		nets = self.getNetlist()
		netlist = nets[0]
		gates = nets[1]

		# choose iterations
		iterations = 1
		# choose deletion method
		randomOrNeighbour = "n"
		reMaking = "y"
		shortFirst = "y"
		# provide a .csv file name
		fileName = "test"
		# execute the algorithm with the given parameters
		v = astar3D.executeAlgorithm(measures, netlist, gates, iterations, fileName, randomOrNeighbour, reMaking, shortFirst)


		visualization.plotAstar(v[0], v[1], v[2], v[3], v[4])

	def quit(self):
		root.quit()
		root.destroy()	

	def setupPrintRB(self):
		self.printvar = IntVar()
		self.printLabel = StringVar()
		self.printLabel.set("Print: ")
		Label(self.master, textvariable=self.printLabel, font=10).grid(row=2, column=0)
		Radiobutton(self.master, text="Print 1", variable=self.printvar, value=1).grid(row=2, column=1)
		Radiobutton(self.master, text="Print 2", variable=self.printvar, value=2).grid(row=2, column=2)
		Radiobutton(self.master, text="test", variable=self.printvar, value=3).grid(row=2, column=3)

	def getPrint(self):
		var = self.printvar.get()
		measures = []
		if var == 1:
			measures.append(18)
			measures.append(13)
			measures.append(7)
		if var == 2:
			measures.append(18)
			measures.append(17)
			measures.append(7)
		if var == 3:
			measures.append(6)
			measures.append(6)
			measures.append(6)			

		return measures

	def setupNetlistRB(self):
		self.netlistvar = IntVar()
		Label(self.master, text="Netlist: ", font=10).grid(row=3, column=0)
		Radiobutton(self.master, text="Netlist 1", variable=self.netlistvar, value=1).grid(row=3, column=1)
		Radiobutton(self.master, text="Netlist 2", variable=self.netlistvar, value=2).grid(row=3, column=2)
		Radiobutton(self.master, text="Netlist 3", variable=self.netlistvar, value=3).grid(row=3, column=3)
		Radiobutton(self.master, text="test", variable=self.netlistvar, value=4).grid(row=3, column=4)

	def getNetlist(self):
		var = self.netlistvar.get()
		if var == 1:
		    nets = netlists.getNetlist1()
		elif var == 2:
		    nets = netlists.getNetlist2()
		elif var == 3:
		    nets = netlists.getNetlist3()
		elif var == 4:
		    nets = netlists.getNetlistTest()
		return nets

	# def setupIterations():


root = Tk()
root.wm_title("Chips & Circuits")

app = App(root)

root.mainloop()




