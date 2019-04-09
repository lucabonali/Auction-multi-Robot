from Bid import Bid
from RoutingAgent import RoutingAgent


class MiniSumRoutingAgent(RoutingAgent):
    def __init__(self,unique_id, model,nRobots,position,targets, agentNode, mapChar):
        super().__init__(unique_id, model,nRobots,position,targets, agentNode, mapChar)
        self.newRPC = 0
        self.oldRPC = 0


    def computeBid(self):
        self.newRPC = len(self.path.path[self.path.trackCounter])
        self.oldRPC = self.calculateOldRPC()
        value = self.newRPC - self.oldRPC
        target = self.path.path[self.path.trackCounter][-1]
        self.bid = Bid(self,value,target)
        self.oldRPC = self.newRPC


    def updateAllocation(self):
        self.agentNode = self.path.path[self.path.trackCounter][-1]
        self.path.trackCounter = self.path.trackCounter + 1

    def calculateOldRPC(self):
        try:
            return len(self.path.path[-2])
        except:
            return 0



