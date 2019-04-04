from mesa import Agent
from Bid import Bid
from Drawer import Drawer
from Node import *
from Path import *
import threading


class RoutingAgent(Agent):
    def __init__(self,unique_id, model,nRobots,position,targets, agentNode, mapChar):
        super().__init__(unique_id, model)
        self.targetString = "T"
        self.wallString = "#"
        self.nRobots = nRobots
        self.toExpand = []
        self.targets = targets
        self.position = position
        self.path = Path()
        self.agentNode = agentNode
        self.mapChar = mapChar
        self.objNode = None
        self.bid = None
        self.bidList = []
        self.otherRobots = []
        self.readyRobot = []
        self.winnerComputed = False
        self.toDelete = True

    def resetState(self):
        self.bid = None
        self.bidList.clear()

    def printState(self):
        print("\n\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n"
              "I am Agent:", self.unique_id, "My bid is", self.bid, "my targets are:", self.targets,"My bidList is", self.bidList,
              "My path is", self.path.printPath(),
              "\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n\n")

    def step(self):
        #print("I am robot ",self.unique_id,"And my path is",self.path.path)
        self.bid = None
        self.toDelete = True
        self.deleteOldBids()
        self.computeNearTargetPath()

    def deleteOldBids(self):
        for i in self.bidList:
            if not self.checkTargetMember(i.targetNode):
                self.bidList.remove(i)

    def checkTargetMember(self, tg):
        for i in self.targets:
            if tg == i:
                return True
            else:
                return False

    def computeNearTargetPath(self):
        self.winnerComputed = False
        self.constructTree()
        #print("I am agent ", self.unique_id, "and my path is", self.path.printPath())
        if self.bid == None:
            self.computeBid()
            #print("My bid is:", self.bid.toString())
            self.broadCastBid()
            if len(self.bidList) == len(self.otherRobots):
                self.computeRoundWinner()

        #print("I am agent ", self.unique_id, "and my Bid is", self.bid.toString())

    def broadCastBid(self):
        for i in self.otherRobots:
            if not self.bid == None:
                #print("I am robot", self.unique_id, "Sending Bid to ", i.unique_id, "BID:", self.bid.toString())
                i.receiveBid(self.bid)


    def receiveBid(self, bid):
        self.bidList.append(bid)
        if not self.bid == None:
            #print("I am robot", self.unique_id, "receiving Bid from ", bid.bidder.unique_id, "BID:", bid.toString())
            if len(self.bidList) == len(self.otherRobots):
                #print("I am robot", self.unique_id, "ready to compute the winner ", "my bidlist is:", self.bidList)
                self.computeRoundWinner()


    def computeRoundWinner(self):
        if not self.winnerComputed:
            winningBid = 100000000
            winningAgent = None
            self.bidList.append(self.bid)
            for i in self.bidList:
                if i.value < winningBid:
                    winningBid = i.value
                    winningAgent = i.bidder
            #print("I am robot", self.unique_id, "Winner bid: ", winningBid, "Winner agent:", winningAgent.unique_id)
            self.winnerComputed = True
            self.updateWinner(winningAgent)
            self.bidList.clear()
            self.checkWin(winningAgent)

    def checkWin(self, winningAgent):
        if self == winningAgent:
            #print("WINNING AGENT:", winningAgent)
            self.updateAllocation()
            x = self.bid.targetNode.xCoord
            y = self.bid.targetNode.yCoord
            self.bid = None
            self.signTarget(x, y)
            self.sendUpdateMap(x, y)
            drawer = Drawer(self.model.schedule.agents)
            drawer.printMap(self.mapChar)
        else:
            #self.printState()
            self.deletePath()

    def updateWinner(self, winningAgent):
        for i in self.otherRobots:
            #print("I am robot", self.unique_id, "I am sending the winner! ", winningAgent.unique_id, "To agent", i.unique_id)
            i.receiveWinner(winningAgent)

    def receiveWinner(self,winningAgent):
        self.winnerComputed = True
        self.checkWin(winningAgent)



    def deletePath(self):
        if self.toDelete:
            #print("I am robot ", self.unique_id, "And i am deleting my path", self.path.path)
            self.path.path.pop(-1)
        self.toDelete = False

    def sendUpdateMap(self, x, y):
        for i in self.otherRobots:
            #print("I am ", self, "SENDING ", (x,y), "To Robot:", i)
            i.deletePath()
            i.signTarget(x,y)

    def signTarget(self,x , y):
        self.mapChar[x][y] = "t"
        try:
            #print("TARGETS: ", self.targets, "TRYING TO REMOVE:", (x,y))
            self.targets.remove((x, y))
            #print(len(self.targets))
        except:
            pass

    def constructTree(self):
        listPosition = self.getListOfPosition(self.mapChar)
        self.toExpand.append(self.agentNode)
        self.setHeuristic(self.agentNode)
        self.expand(self.agentNode, listPosition, self.mapChar)
        self.path.path.append(self.constructPath(self.objNode,[]))
        self.path.path[self.path.trackCounter].reverse()
        self.toExpand.clear()


    def getListOfPosition(self,mapChar):
        list = []
        for i in range(len(mapChar)):
            for j in range(len(mapChar[i])):
                list.append((i, j))
        return list

    def expand(self, node, listPosition, mapChar):
        self.toExpand.remove(node)
        for i in range(len(node.adjacents)):
            xCoord = node.adjacents[i][0]
            yCoord = node.adjacents[i][1]
            if self.available(listPosition, coord=(xCoord,yCoord)):
                try:
                    value = mapChar[xCoord][yCoord]
                    if not value == self.wallString:
                        child = Node(father=node, xCoord=xCoord, yCoord=yCoord, value=value)
                        node.addChildren(child)
                        self.setHeuristic(child)
                        self.updateFrontier(child)
                except:
                    pass
        for i in range(len(node.children)):
            if self.checkTarget(node.children[i]):
                self.toExpand.clear()
                self.objNode = node.children[i]
        if not len(self.toExpand) == 0:
            self.expand(self.toExpand[0], listPosition, mapChar)

    def available(self,listPosition, coord):
        for i in range(len(listPosition)):
            if listPosition[i] == coord:
                listPosition.remove(coord)
                return True
        return False

    def checkTarget(self,node):
        if node.value == self.targetString:
            return True
        return False

    def constructPath(self,node, path):
        if node == None:
            return path
        if not (node.value == "R"):
            path.append(node)
        return self.constructPath(node.father, path)

    def setHeuristic(self, node):
        heuristic = self.getNearTarget(node.xCoord, node.yCoord)
        node.heuristic = heuristic + len(self.constructPath(node,[]))

    def getNearTarget(self,x,y):
        nearValues = []
        for i in range(len(self.targets)):
            nearValues.append(abs((self.targets[i][0]-x)+(self.targets[i][1]-y)))
        nearValues.sort()
        return nearValues[0]

    def updateFrontier(self, child):
        h = child.heuristic
        for i in range(len(self.toExpand)):
            if self.toExpand[i].heuristic >= h:
                self.toExpand.insert(i,child)
                return
        self.toExpand.append(child)

    def computeBid(self):
        pass

    def updateAllocation(self):
        pass



