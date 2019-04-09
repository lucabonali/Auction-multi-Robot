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

    def getMinTargetDistance(self):
        minD = 1000
        for i in self.distances:
            print(i[1])
            if i[1] <= minD and i[1] != 0:
                minD = i[1]
        return minD

