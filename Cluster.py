from math import sqrt


class Cluster():
    def __init__(self, targets, minThreshold):
        self.targets = targets
        self.clusters = []
        self.minThreshold = minThreshold

    def calculateDistances(self):
        others = self.targets
        for i in self.targets:
            for j in self.targets:
                i.distances.append((j,self.calcDistance(i,j)))

    def calcDistance(self, i, j):
        airDistance = int(sqrt((i.x-j.x)**2+(i.y-j.y)**2))
        actualPath = self.calculatePath(i,j)
        #if  actualPath == airDistance:
        #    return airDistance
        return airDistance
    def calculatePath(self,i , j):
        return 0

    def formClusters(self):
        cont = 0
        for i in self.targets:
            if not i.inCluster:
                self.clusters.append([i])
                i.inCluster = True
                for j in self.targets:
                    if i.getTargetDistance(j) < self.minThreshold and i != j:
                        self.clusters[cont].append(j)
                        j.inCluster = True
                cont += 1
        self.toString()
        return self.clusters

    def toString(self):
        for i in self.clusters:
            print(self.clusters.index(i),"^ Cluster: ")
            for j in i:
                print("Target",(j.x,j.y))
