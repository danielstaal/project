'''
Transform paths of chip to mathematica input for .stl file
Date: 27/06/2016
Daniel Staal

Write a path in this file that will be printed in the terminal. This can be inputted in mathematica
to receive a model in a .stl filetype
'''

def toXYZ(paths):
	newPaths = []
	for path in paths:
		newPath = []
		for i in range(len(path[0])):
			newPath.append([path[0][i], path[1][i], path[2][i]])
		newPaths.append(newPath)
	return newPaths

def toModel(paths):
	model = "Graphics3D[{"

	for path in paths:
		counter = 0
		for coor in path:
			if counter + 1 < len(path):
				model += "Cylinder[{{"
				model += str(coor[0]) + ", "
				model += str(coor[1]) + ", "
				model += str(coor[2]) + "}, {"

				model += str(path[counter + 1][0]) + ", "
				model += str(path[counter + 1][1]) + ", "
				model += str(path[counter + 1][2]) + "}}, r], \nSphere[{"

				model += str(path[counter + 1][0]) + ", "
				model += str(path[counter + 1][1]) + ", "
				model += str(path[counter + 1][2]) + "}, r], "

			counter += 1
	model = model[:-2]
	model += "}]"

	print model 


paths = [[[12, 12], [2, 3], [0, 0]], [[13, 12, 11, 11], [7, 7, 7, 8], [0, 0, 0, 0]], [[6, 5, 4, 3, 2, 1], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]], [[9, 8, 7, 6, 6, 6], [10, 10, 10, 10, 9, 8], [0, 0, 0, 0, 0, 0]], [[9, 10, 11, 12, 13, 13, 13, 13], [10, 10, 10, 10, 10, 9, 8, 7], [0, 0, 0, 0, 0, 0, 0, 0]], [[9, 9, 10, 10, 10, 10, 11, 11], [10, 9, 9, 8, 7, 6, 6, 5], [0, 0, 0, 0, 0, 0, 0, 0]], [[11, 12, 12, 12, 12, 12, 12, 12, 12, 12], [5, 5, 6, 6, 7, 8, 9, 10, 11, 11], [0, 0, 0, 1, 1, 1, 1, 1, 1, 0]], [[15, 14, 14, 14, 14, 14, 14, 14, 13, 12, 12, 12], [8, 8, 7, 6, 5, 4, 3, 3, 3, 3, 2, 2], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0]], [[4, 5, 6, 7, 8, 9, 10, 10, 11, 12, 12], [5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], [[15, 15, 15, 15, 15, 15, 15, 15, 14, 13, 13, 12, 11, 10, 10], [8, 7, 6, 5, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0]], [[15, 15, 14, 13, 12, 11, 10, 9, 8, 7, 7, 7, 6, 5, 4, 3], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 2, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], [[1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 8], [11, 11, 11, 11, 11, 11, 11, 11, 11, 10, 10, 9, 8, 7, 6, 5, 4, 4, 4], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]], [[1, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 13, 13], [5, 5, 5, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7], [0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0]], [[2, 3, 4, 5, 5, 6, 7, 7, 7, 7, 7, 7, 8, 9, 10, 11, 11, 11, 12], [8, 8, 8, 8, 7, 7, 7, 6, 6, 5, 4, 3, 3, 3, 3, 3, 2, 2, 2], [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]], [[10, 9, 8, 8, 8, 7, 6, 5, 5, 5, 5, 4, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 2, 2, 2, 2, 2, 3, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 8, 9, 9, 9, 9], [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 2, 1, 0]], [[15, 14, 13, 12, 12], [1, 1, 1, 1, 2], [0, 0, 0, 0, 0]], [[12, 13, 13, 13, 13, 13], [3, 3, 4, 5, 6, 7], [0, 0, 0, 0, 0, 0]], [[1, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15, 15, 15, 15], [9, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8], [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0]], [[2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2], [8, 7, 7, 7, 6, 6, 6, 7, 8, 9, 9, 9, 9, 10, 10], [0, 0, 0, 1, 1, 2, 3, 3, 3, 3, 2, 1, 0, 0, 0]], [[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4], [9, 9, 8, 8, 8, 8, 7, 6, 5, 5, 5, 5, 5, 4, 3, 3, 3, 4, 5, 5], [0, 0, 0, 1, 2, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1, 0, 0, 0, 0]], [[1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3], [11, 11, 11, 11, 10, 10, 9, 8, 7, 6, 6, 6, 5, 4, 3, 2, 2, 2, 2, 2], [0, 1, 1, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 3, 2, 1, 0]], [[15, 15, 14, 14, 13, 12, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 10, 10, 10, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1], [1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 9, 10, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 11], [0, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], [[4, 4, 4, 3, 2, 2, 2, 2, 3], [5, 4, 4, 4, 4, 3, 2, 2, 2], [0, 0, 1, 1, 1, 1, 1, 0, 0]], [[2, 1, 1, 1, 2, 3, 4, 5, 6, 6, 6, 7, 8, 8, 8, 9], [8, 8, 7, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 8, 8, 8], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0]], [[12, 11, 10, 9, 8, 7, 6, 5, 4, 4, 4, 4, 4, 3, 2, 1, 1, 1, 1, 1], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 3, 3, 3, 3, 2, 1, 0, 0]], [[2, 2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8], [8, 9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 7, 6, 5, 4, 4, 4, 4], [0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 2, 1, 0]], [[15, 16, 16, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]], [[15, 15, 16, 16, 16, 16, 16, 15, 14, 13, 12, 11, 10, 10, 10, 9, 8, 7, 6, 5, 4, 4, 4, 4, 3, 2, 2], [1, 2, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 8, 8, 8], [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 0]]]

paths = toXYZ(paths)
toModel(paths)
# Graphics3D[{

# Cylinder[{{9, 10, 0}, {10, 10, 0}}, r], 
#   Cylinder[{{10, 10, 0}, {11, 10, 0}}, r], 
# Sphere[{10, 10, 0}, r],
#   Cylinder[{{11, 10, 0}, {12, 10, 0}}, r], 
# Sphere[{11, 10, 0}, r],
#   Cylinder[{{12, 10, 0}, {13, 10, 0}}, r], 
# Sphere[{12, 10, 0}, r],
#   Cylinder[{{13, 10, 0}, {13, 9, 0}}, r], 
# Sphere[{13, 9, 0}, r],
# Sphere[{13, 10, 0}, r],
#   Cylinder[{{13, 9, 0}, {13, 8, 0}}, r], 
#   Cylinder[{{13, 8, 0}, {13, 7, 0}}, r], 
# Sphere[{13, 7, 0}, r]}]

