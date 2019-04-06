from Bid import Bid
from RoutingAgent import RoutingAgent


class MiniAveRoutingAgent(RoutingAgent):
    def __init__(self, unique_id, model, nRobots, position, targets, agentNode, mapChar):
        super().__init__(unique_id, model, nRobots, position, targets, agentNode, mapChar)
        self.newCTPC = 0
        self.oldCTPC = 0

    def computeBid(self):
        self.newCTPC = self.calculateNewCTPC()
        self.oldCTPC = self.calculateOldCTPC()
        # print("\n\n\nI AM ROBOT", self.unique_id,"My values are ", self.newRPC, self.oldRPC)
        value = self.newCTPC - self.oldCTPC
        target = self.path.path[self.path.trackCounter][-1]
        self.bid = Bid(self, value, target)
        self.oldCTPC = self.newCTPC

    def updateAllocation(self):
        self.agentNode = self.path.path[self.path.trackCounter][-1]
        self.path.trackCounter = self.path.trackCounter + 1

    def calculateOldCTPC(self):
        CTPC = 0
        for i in self.path.path[:-1]:
            CTPC += len(i)
        return CTPC

    def calculateNewCTPC(self):
        CTPC = 0
        for i in self.path.path:
            CTPC += len(i)
        return CTPC
