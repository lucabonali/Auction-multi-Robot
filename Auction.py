from colorama import Fore
from mesa import Model
from mesa.time import RandomActivation

from MiniAveAgent import MiniAveRoutingAgent
from MiniMaxAgent import MiniMaxRoutingAgent
from RoutingAgent import RoutingAgent
from Drawer import Drawer
from MapHandler import *
from MiniSumAgent import MiniSumRoutingAgent
from Node import Node


class Auction(Model):
    def __init__(self, path):
        self.schedule = RandomActivation(self)
        self.mapChar = []
        self.robotPos = []
        self.targetPos = []
        self.bidList = []

        self.startRoutingAuction(path)

    #Should be called from the main function to advance the auction by one step, in a random way
    def step(self):
        self.schedule.step()

    def startRoutingAuction(self, path):
        mapHandler = MapHandler(path)
        mapHandler.readMap()
        self.mapChar = mapHandler.map
        self.robotPos = mapHandler.robotPos
        self.targetPos = mapHandler.targetPos
        self.createAgents(self.robotPos, self.targetPos, self.mapChar)

    def createAgents(self, robPos, tarPos, mapChar):
        for i in range(len(robPos)):
            agentNode = Node(father=None, xCoord=robPos[i][0], yCoord=robPos[i][1], value="R")
            a = MiniMaxRoutingAgent(i,self,len(robPos), robPos[i], tarPos, agentNode, mapChar)
            self.schedule.add(a)
        for i in self.schedule.agents:
            i.otherRobots = self.getOtherRobots(i)


    def getOtherRobots(self, agent):
        list = []
        for i in self.schedule.agents:
            if not agent == i:
                list.append(i)
        return list
