# function to calculate manhattan distance
def calcDistance(pos1, pos2):
    distance = abs(pos1.getX() - pos2.getX()) + abs(pos1.getY() - pos2.getY()) + abs(pos1.getZ() - pos2.getZ())
    return distance