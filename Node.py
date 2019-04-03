class Node():
    def __init__(self,father,xCoord,yCoord,value):
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.value = value
        self.heuristic = None
        self.adjacents = self.initializeAdjList()
        self.father = father
        self.children = []

    def initializeAdjList(self):
        list = []
        #list.append((self.xCoord - 1, self.yCoord - 1))
        list.append((self.xCoord - 1, self.yCoord ))
        #list.append((self.xCoord - 1, self.yCoord + 1))
        list.append((self.xCoord , self.yCoord + 1))
        #list.append((self.xCoord + 1, self.yCoord + 1))
        list.append((self.xCoord + 1, self.yCoord ))
        #list.append((self.xCoord + 1, self.yCoord - 1))
        list.append((self.xCoord , self.yCoord - 1))
        return list


    def addChildren(self, node):
        self.children.append(node)

