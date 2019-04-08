import random
from mesa import Model
from mesa.time import RandomActivation

from Cluster import Cluster
from ClusteringAgent import ClusteringAgent
from Drawer import Drawer
from Node import Node
from Target import Target


class TargetClustering(Model):  # Like auction class

    def __init__(self, map, targetPos):
        super().__init__()
        self.map = map
        self.targetPos = targetPos
        self.robotPos = []
        self.agents = []
        self.targetClusters = self.formClusters(15)
        self.schedule = RandomActivation(self)
        self.assignAgentToClusters()


    def step(self):
        self.schedule.step()
        self.drawMap()

    def getRandomPosition(self, nRobots):
        robotRandomPos = []
        for i in range(nRobots):
            newPos = self.getPos(robotRandomPos)
            robotRandomPos.append(newPos)
        return robotRandomPos

    def getPos(self, robotPos):
        xRandCoord = random.randint(1, len(self.map)-1)
        yRandCoord = random.randint(1, len(self.map[0])-1)
        newPos = (xRandCoord, yRandCoord)
        if not (newPos in self.robotPos and (not self.map[newPos[0]][newPos[1]] == "#") and (not self.map[newPos[0]][newPos[1]] == "T")):
            return newPos
        return self.getPos(robotPos)

    def formClusters(self, minThreshold):
        cluster = Cluster(self.formTargets(),minThreshold)
        cluster.calculateDistances()
        print("END CLUSTERING")
        return cluster.formClusters()

    def formTargets(self):
        targetList = []
        for i in self.targetPos:
            targetList.append(Target(i[0],i[1]))
        return targetList

    def assignAgentToClusters(self):
        cont = 0
        for i in self.targetClusters:
            xCoord = self.getFirstPosition(i[0])[0]
            yCoord = self.getFirstPosition(i[0])[1]
            a = ClusteringAgent(unique_id=cont,model=self, targets=i,agentNode=Node(father= None,xCoord=xCoord,yCoord=yCoord,value=self.map[xCoord][yCoord]),mapChar=self.map)
            self.agents.append(a)
            self.schedule.add(a)
            self.map[xCoord][yCoord] = "R"
            cont += 1


    def getFirstPosition(self, i):
        if self.map[i.x-1][i.y] == " ":
            return (i.x-1,i.y)
        elif self.map[i.x][i.y-1] == " ":
            return (i.x,i.y-1)
        elif self.map[i.x+1][i.y] == " ":
            return (i.x+1,i.y)
        elif self.map[i.x+1][i.y+1] == " ":
            return (i.x+1,i.y+1)

    def drawMap(self):
        drawer = Drawer(self.agents)
        drawer.printMap(self.map)








