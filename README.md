# Project Chips & Circuits
Daniël Staal<br>
daniel.staal@hotmail.com<br>
27/06/2016

<img src="https://github.com/danielstaal/project/blob/master/doc/figure_1.png?raw=true" width="1000">

NOTE: To run the program call: python App.py

## Problem

The case is Chips & Circuits. A number of gates placed inside a print have to be connected in an optimal way. A print is square shaped and is always settled in the bottom layer of a 3-dimensional cuboidal grid with a total of 7 layers. Therefore each gate can be connected upto a maximum of 5 other gates(south, west, east, north and up a layer). The main objective will be to find an as low as possible sum of all the paths lengths and to find a solution for each netlist, the list of connections to be made, on a particular print.

## Goals

- Use the largest print (18x17x7) and create 50 random gate placements in a print. For every configuration 50 random netlists could be created and the program tries to solve each netlist in each print. 
- Create a program that is user friendly.

## Overview

- Program runs in a Tkinter application, launched by calling python App.py
- Results from a database are showed to the user

## Data

Standard given netlists, prints. Python (libraries)

## Parts of the application

A*, visualisation (matplotlib), path deletion algorithms, hill climber

## Technical problems or limitations

The main problems that might occur can be split into two categories: too high time complexity and no solution is found
