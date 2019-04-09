import random
from mesa.time import RandomActivation
from Clustering.Cluster import Cluster
from Clustering.Target import Target


class TargetClustering():  # Like auction class

    def __init__(self, map, targetPos):
        super().__init__()
        self.map = map
        self.targetPos = targetPos
        self.robotPos = []
        self.agents = []
        self.targetClusters = self.formClusters(10)
        self.schedule = RandomActivation(self)
        self.assignAgentToClusters()

    def formClusters(self, minThreshold):
        cluster = Cluster(self.formTargets(), self.map, minThreshold)
        cluster.calculateDistances()
        print("END CLUSTERING")
        return cluster.formClusters()

    def formTargets(self):
        targetList = []
        for i in self.targetPos:
            targetList.append(Target(i[0], i[1]))
        return targetList

    def assignAgentToClusters(self):
        cont = 0
        for i in self.targetClusters:
            xCoord = self.getFirstPosition(i[random.randint(0, len(i) - 1)])[0]
            yCoord = self.getFirstPosition(i[random.randint(0, len(i) - 1)])[1]
            self.map[xCoord][yCoord] = "R"
            cont += 1
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == "R":
                    self.robotPos.append((i, j))

    def getFirstPosition(self, i):
        if self.map[i.x - 1][i.y] == " ":
            return (i.x - 1, i.y)
        elif self.map[i.x][i.y - 1] == " ":
            return (i.x, i.y - 1)
        elif self.map[i.x + 1][i.y] == " ":
            return (i.x + 1, i.y)
        elif self.map[i.x + 1][i.y + 1] == " ":
            return (i.x + 1, i.y + 1)


