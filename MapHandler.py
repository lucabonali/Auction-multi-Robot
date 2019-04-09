import random

from Clustering.TargetClustering import TargetClustering


class MapHandler():

    def __init__(self, path):
        self.path = path
        self.robotPos = []
        self.targetPos = []

    def readMap(self):
        f = open(self.path, "r")
        height = sum(1 for line in open(self.path))
        self.map = [None] * height
        for i in range(height):
            self.map[i] = list(f.readline().rstrip())
        self.initializeRobotAndTargetPosition()

    def initializeRobotAndTargetPosition(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == "R":
                    self.robotPos.append((i,j))
                if self.map[i][j] == "T":
                    self.targetPos.append((i,j))
        if len(self.robotPos) == 0:
            self.positionRobotInMap()


    def positionRobotInMap(self):
        targetClustering = TargetClustering(self.map, self.targetPos)
        self.map = targetClustering.map
        self.robotPos = targetClustering.robotPos


    def getRandomPosition(self, nRobots):
        robotRandomPos = []
        for i in range(nRobots):
            newPos = self.getPos(robotRandomPos)
            robotRandomPos.append(newPos)
        return robotRandomPos

    def getPos(self, robotPos):
        xRandCoord = random.randint(1, len(self.map) - 1)
        yRandCoord = random.randint(1, len(self.map[0]) - 1)
        newPos = (xRandCoord, yRandCoord)
        if not (newPos in self.robotPos and (not self.map[newPos[0]][newPos[1]] == "#") and (
        not self.map[newPos[0]][newPos[1]] == "T")):
            return newPos
        return self.getPos(robotPos)



