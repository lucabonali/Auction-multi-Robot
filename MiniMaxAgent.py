from Bid import Bid
from RoutingAgent import RoutingAgent


class MiniMaxRoutingAgent(RoutingAgent):
    def __init__(self,unique_id, model,nRobots,position,targets, agentNode, mapChar):
        super().__init__(unique_id, model,nRobots,position,targets, agentNode, mapChar)
        self.RPC = 0


    def computeBid(self):
        self.newRPC = len(self.path.path[self.path.trackCounter])
        value = self.newRPC
        target = self.path.path[self.path.trackCounter][-1]
        self.bid = Bid(self,value,target)

    def updateAllocation(self):
        self.agentNode = self.path.path[self.path.trackCounter][-1]
        self.path.trackCounter = self.path.trackCounter + 1


