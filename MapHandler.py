
class MapHandler():

    def __init__(self, path):
        self.path = path
        self.robotPos = []
        self.targetPos = []

    def readMap(self):
        f = open(self.path, "r")
        height = sum(1 for line in open(self.path))
        self.map = [None] * height
        for i in range(height):
            self.map[i] = list(f.readline().rstrip())
        self.initializeRobotAndTargetPosition()

    def initializeRobotAndTargetPosition(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == "R":
                    self.robotPos.append((i,j))
                if self.map[i][j] == "T":
                    self.targetPos.append((i,j))
