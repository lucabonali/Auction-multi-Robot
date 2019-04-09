from mesa import Model
from mesa.time import RandomActivation
from MiniAveAgent import MiniAveRoutingAgent
from MiniMaxAgent import MiniMaxRoutingAgent
from MiniSumAgent import MiniSumRoutingAgent
from Node import Node


class Auction(Model):
    def __init__(self, mapHandler, objective):
        super().__init__()
        self.objective = objective
        self.mapHandler = mapHandler
        self.schedule = RandomActivation(self)
        self.mapChar = []
        self.robotPos = []
        self.targetPos = []
        self.bidList = []

        self.startRoutingAuction()

    #Should be called from the main function to advance the auction by one step, in a random way
    def step(self):
        self.schedule.step()

    def startRoutingAuction(self):
        self.mapChar = self.mapHandler.map
        self.robotPos = self.mapHandler.robotPos
        self.targetPos = self.mapHandler.targetPos
        self.createAgents(self.robotPos, self.targetPos, self.mapChar)

    def createAgents(self, robPos, tarPos, mapChar):
        for i in range(len(robPos)):
            agentNode = Node(father=None, xCoord=robPos[i][0], yCoord=robPos[i][1], value="R")
            if self.objective == "s":
                a = MiniSumRoutingAgent(i,self,len(robPos), robPos[i], tarPos, agentNode, mapChar)
            if self.objective == "m":
                a = MiniMaxRoutingAgent(i, self, len(robPos), robPos[i], tarPos, agentNode, mapChar)
            if self.objective == "a":
                a = MiniAveRoutingAgent(i, self, len(robPos), robPos[i], tarPos, agentNode, mapChar)
            self.schedule.add(a)
        for i in self.schedule.agents:
            i.otherRobots = self.getOtherRobots(i)


    def getOtherRobots(self, agent):
        list = []
        for i in self.schedule.agents:
            if not agent == i:
                list.append(i)
        return list
