class Target():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.distances = []
        self.inCluster = False

    def getTargetDistance(self, otherTarget):
        for i in self.distances:
            if i[0] == otherTarget:
                return i[1]


