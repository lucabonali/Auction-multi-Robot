class Path():
    def __init__(self):
        self.path = []
        self.len = 0
        self.trackCounter = 0


    def printPath(self):
        str = []
        for i in self.path: # for all tracks
            for j in i:
                str.append(("Node:", j.xCoord,j.yCoord))
        return str