# Report


#### Problem description

The case is Chips & Circuits. In Chip design, ideally the connections between gates are as short as possible. This project is about finding ways to compute the shortest length of the sum of all the paths in a chip and figuring out why for certain prints (configurations of 25 gates placed on the bottom layer of a 18x13x7 cuboid) it is especially hard or easy to find valid solutions. In the project a user friendly application has been built to show the results from random netlists (a list of gates that have to be connected) in a range of 10 to 50 connections for three different prints.

<img src="https://github.com/danielstaal/project/blob/master/doc/App.PNG?raw=true" width="800">

The App created in this project is a local computer application, running in a python environment using a canvas module called Tkinter. In the left window, graphs about average time and lengths from a certain print are displayed. In the right window, the user can see an example solution for the amount of connections that is selected in the left window.

#### Technical Design
The core of the program to find a solution given a netlist and a print is in the file called Astar3D.py. This file receives the setup of this particular problem an returns a solution and the computation time that was needed to find this solution. This program is used to build up a database of results using different prints and randomly generated netlists. In the application information from this database can be examined. In the application no real time results are generated but rather taken from this database. Now a more detailed description of the two separate parts will be given.

##### Finding a single solution
The algorithm to find a valid solution to connect all the connections from in netlist in a particular print consists of several features. To find the shortest path from A to B in the 18x13x7 grid, the A-star algorithm is being used, and is allowed to move in every direction horizontally of vertically. If the size of the netlist is large enough, chances are that at some point a path from A to B cannot be found, because A-star is blocked in all directions. Whenever this occurs, one of the paths that add to the blockade is removed entirely from the grid. This process repeats until the original path can be finished. I call this process neighbour deletion. Lastly, after a valid solution is found, a simple hill climber is used. The hill climber individually removes each path and immediately remakes it. By doing this, space that can be arisen during neighbour deletion, is used. This process repeats until the total path length did not change after all paths have been remade. 

##### The application
In the application two windows can be viewed, and additional information for the selected amount of connections is shown. 




Create a report (REPORT.md), based on your design document, containing important decisions that you’ve made, e.g. where you changed your mind during the past weeks. This is how you show the reviewer that you actually understand what you have done.

Start with a short description of your application (like in the README.md, but very short, including a single screen shot).

Clearly describe the technical design: how is the functionality implemented in your code? This should be like your DESIGN.md but updated 
to reflect the final application. First, give a high level overview, which helps us navigate and understand the total of your code 
(which components are there?). Second, go into detail, and describe the modules/classes and how they relate.

Clearly describe challenges that your have met during development. Document all important changes that your have made with regard to your
design document (from the PROCESS.md). Here, we can see how much you have learned in the past month.

Defend your decisions by writing an argument of a most a single paragraph. Why was it good to do it different than you thought before?
Are there trade-offs for your current solution? In an ideal world, given much more time, would you choose another solution?

Make sure the document is complete and reflects the final state of the application. The document will be an important part of your grade.
