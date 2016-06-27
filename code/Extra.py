# function to calculate manhattan distance
def calcDistance(pos1, pos2, layerFactor):
    distance = abs(pos1.getX() - pos2.getX()) + abs(pos1.getY() - pos2.getY()) + layerFactor*(abs(pos1.getZ() - pos2.getZ()))
    return distance