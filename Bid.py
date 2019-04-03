class Bid():
    def __init__(self, bidder, value, targetNode):
        self.value = value
        self.bidder = bidder
        self.targetNode = targetNode

    def toString(self):
        return ("Bidder",self.bidder.unique_id, "Value:", self.value, "target Node:", self.targetNode.xCoord, self.targetNode.yCoord)