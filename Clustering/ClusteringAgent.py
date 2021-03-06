from math import sqrt

from mesa import Agent

from Node import Node
from Path import Path


class ClusteringAgent(Agent):

    def __init__(self, unique_id, model, targets, agentNode, mapChar):
        super().__init__(unique_id, model)
        self.unique_id = unique_id
        self.targetString = "T"
        self.wallString = "#"
        self.toExpand = []
        self.targets = targets
        self.path = Path()
        self.agentNode = agentNode
        self.mapChar = mapChar
        self.objNode = None

    def step(self):
        if not len(self.targets) == 0:
            self.constructTree()
            agentNode = self.objNode
            self.agentNode = self.objNode
            self.mapChar[agentNode.xCoord][agentNode.yCoord] = "t"
            print("I am ", self.unique_id, "i am deleting:", self.targets)
            self.removeTarget(self.objNode.xCoord, self.objNode.yCoord)
            print("I am ", self.unique_id, "My list is now:", self.targets)
        else:
            pass

    def constructTree(self):
        listPosition = self.getListOfPosition(self.mapChar)
        self.toExpand.append(self.agentNode)
        self.setHeuristic(self.agentNode)
        self.expand(self.agentNode, listPosition, self.mapChar,0)
        self.path.path.append(self.constructPath(self.objNode, []))
        self.path.path[self.path.trackCounter].reverse()
        self.toExpand.clear()

    def getListOfPosition(self, mapChar):
        list = []
        for i in range(len(mapChar)):
            for j in range(len(mapChar[i])):
                list.append((i, j))
        return list

    def expand(self, node, listPosition, mapChar, rec):
        if not rec >= 500:
            self.toExpand.remove(node)
            for i in range(len(node.adjacents)):
                xCoord = node.adjacents[i][0]
                yCoord = node.adjacents[i][1]
                if self.available(listPosition, coord=(xCoord, yCoord)):
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
                self.expand(self.toExpand[0], listPosition, mapChar, rec+1)

    def available(self, listPosition, coord):
        for i in range(len(listPosition)):
            if listPosition[i] == coord:
                listPosition.remove(coord)
                return True
        return False

    def checkTarget(self, node):
        if node.value == self.targetString:
            return True
        return False

    def constructPath(self, node, path):
        if node is None:
            return path
        if not (node.value == "R"):
            path.append(node)
        return self.constructPath(node.father, path)

    def setHeuristic(self, node):
        heuristic = self.getNearTarget(node.xCoord, node.yCoord)
        node.heuristic = heuristic + len(self.constructPath(node, []))

    def getNearTarget(self, x, y):
        nearValues = []
        for i in range(len(self.targets)):
            nearValues.append(sqrt((self.targets[i].x - x) ** 2 + (self.targets[i].y - y) ** 2))
        nearValues.sort()
        return nearValues[0]

    def updateFrontier(self, child):
        h = child.heuristic
        for i in range(len(self.toExpand)):
            if self.toExpand[i].heuristic >= h:
                self.toExpand.insert(i, child)
                return
        self.toExpand.append(child)

    def removeTarget(self, xCoord, yCoord):
        for i in self.targets:
            if i.x == xCoord and i.y == yCoord:
                self.targets.remove(i)
