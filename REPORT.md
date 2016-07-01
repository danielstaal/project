# Report


#### Problem description

The case is Chips & Circuits. In Chip design, ideally the connections between gates are as short as possible. This project is about finding ways to compute the shortest length of the sum of all the paths in a chip and figuring out why for certain prints (configurations of 25 gates placed on the bottom layer of a 18x13x7 cuboid) it is especially hard or easy to find valid solutions. In the project a user friendly application has been built to show the results from random netlists (a list of gates that have to be connected) in a range of 10 to 50 connections for three different prints.

<img src="https://github.com/danielstaal/project/blob/master/doc/App.PNG?raw=true" width="800">

The App created in this project is a local computer application, running in a python environment using a canvas module called Tkinter. In the left window, graphs about average time and lengths from a certain print are displayed. In the right window, the user can see an example solution for the amount of connections that is selected in the left window.

#### Technical Design
The core of the program to find a solution, given a netlist and a print, is in the file called Astar3D.py. This file receives the starting parameters of a particular case and returns a solution and the computation time that was needed to find a solution. This program is used to build up a database of results using different prints and randomly generated netlists. In the application, information from this database can be examined. In the application no real time results are generated. A more detailed description of the two separate parts, the solver and the application, will now be given:

##### Finding a single solution
The algorithm to find a valid solution to connect all the connections from a netlist in a particular print consists of several features. To find the shortest path from A to B in the 18x13x7 grid, the A-star algorithm is being used, and is allowed to move in every direction horizontally of vertically. If the size of the netlist is large enough, chances are that at some point a path from A to B cannot be found, because A-star is blocked in all directions. Whenever this occurs, one of the paths that add to the blockade is removed entirely from the grid. This process repeats until the original path can be finished. I call this method neighbour deletion. Lastly, after a valid solution is found, a simple hill climber is used. The hill climber individually removes each path and immediately remakes it. By doing this, space that can have arisen during neighbour deletion, is used. This process repeats until the total path length did not change after all paths have been remade. 

##### The application
In the application two windows are shown, and additional information for the selected amount of connections is shown. The successrate is computed by taking the percentage of randomly generated netlists that is solved by the algorithm for this number of connections. The optimality score is computed by taking the average of dividing the theoretical lowest total path length for a netlist by the total length that is found. This theoretical minimum is calculated by separately making each connection from the netlist, removing each path after it has been made. On the top left of the application a print can be selected, automatically showing the results of this print in the two windows. Next to this option, the user can select a range of path lengths that will be exclusively shown in the right window after clicking the update button. This right window is rotatable by dragging the mouse and thus can be viewed from different angles. All the results are collected from the database directory. The App is created in the App.py file, consequently the application is runnable by using the command: python App.py.

#### Challenges faced 
(Major challenges about the App building procedure will be discussed, rather than about the problem solver.)

The main challenge of this project was to create a user friendly application to show the results of the Chips&Circuits project. Firstly a python module had to be found to create a separate screen/canvas connected to the terminal, instead of within the terminal. The python canvas module Tkinter seemed to be a nice environment to create the application. A challenge of this module was to embed plots of the results within the same canvas to be able to use a single window to operate in, using the matplotlib module and the Tkinter module together. To further simplify the application, an interactive graph was implemented to provide a clearer user interface by removing buttons and options. The next challenge was to collect data, which takes about 8 hours to try 10 random netlists in a particular print in a range from 10 to 50 connections. The 'lisa cluster' has been used to make it quicker and easier to find results. The lisa cluster allows to upload data to the lisa system and to send batch jobs to be handled within a given time. I did not make use of the possibility of implementing parallel processing. The results gained from serial processing on one node seemed to be sufficient for now. However, if a larger amount of results is needed probably parallel processing would be useful to speed up the process. Lastly work has been done concerning the production of a 3D-print. This process seemed to be rather difficult, because I do not have any experience in this field. Soon it became clear that the python visualization was useless for the 3D-print, because the filetype could not be transformed to a filetype that the 3D-printer recognizes. A model had to be built from scratch as a ".stl" file. Mathematica seemed to be a good tool to create a ".stl" file from solid shapes. Cylinders and spheres where combined to create connected solid tubes. In python I wrote a program to transform the solution data of a particular grid to code that mathematica can interpret. 

#### Discussion on decisions
The decision to create a single screen to be able to view a global graph of the results and a single example at the same time seems to be valid. It reduces the complexity of the application by not having to switch screens or close any screens while examining the results. The decision to reduce the application from a solver to an application that just shows database results could be questionable. The option to use live computation of the algorithm in the application might stimulate the active experience of the user and provide a more lively feel to the program. However when computing a netlist larger than 20 connections, computation time might be a few minutes which might be an unpleasant for the user. This is why I chose to use database results in the application, and not a solver. In the future, the application could be improved by collecting a larger database to give more value to the results.

#### Results
In this additional section, results will be shown:

##### Example grid solutions (screenshots from the application)
44 Connections on the original print:

<img src="https://github.com/danielstaal/project/blob/master/doc/figure_1.png?raw=true" width="1000">

48 Connections on the original print, showing only the 6 longest paths:

<img src="https://github.com/danielstaal/project/blob/master/doc/longPaths.PNG?raw=true" width="300">

10 Connections on the original print:

<img src="https://github.com/danielstaal/project/blob/master/doc/10con.PNG?raw=true" width="300">

50 Connections on an ideal print(print 2):

<img src="https://github.com/danielstaal/project/blob/master/doc/50con.PNG?raw=true" width="300">

##### Overall print results (screenshots from the application)

Print 1 (original print):

<img src="https://github.com/danielstaal/project/blob/master/doc/Print1.PNG?raw=true" width="500">

Print 2 (ideal print):

<img src="https://github.com/danielstaal/project/blob/master/doc/Print2.PNG?raw=true" width="500">

Print 3 (original print with 4 small hand picked changes in gate positions): 

<img src="https://github.com/danielstaal/project/blob/master/doc/Print3.PNG?raw=true" width="500">

##### Success Rates

<img src="https://github.com/danielstaal/project/blob/master/doc/suc.PNG?raw=true" width="500">

#### Conclusion
To be able to draw conclusions from these results, more data would be necessary. This was a practical project, but in the future could be extended to a research project to try to find significant changes in computation time, total path length and successrate when using different prints or making slight improvements on original prints. Evolutionary learning methods could be used to try to find an optimal print, by making slight changes every generation. Furthermore the solving algorithm might be improvable to find shorter total path lengths. This was not the main goal of this project, but rather to create a clear visualization to examine the results and compare performance of different prints, however the performance of the solver seems acceptable. To sum up: in the future it might be interesting to scientifically examine the results shown in the application.


