import time

from Clustering.TargetClustering import TargetClustering
from MapHandler import *

def computeTotalCost(agents):
    cost = 0
    for i in agents:
        cost += len(i.path.path[-1])
    print("TOTAL COST OF ROUTING:",cost)


def computeMaxPathCost(agents):
    maxCost = 0
    maxAgent = None
    for i in agents:
        costAgent = len(i.path.path[-1])
        if maxCost < costAgent:
            maxCost = costAgent
            maxAgent = i.unique_id
    print("MAXIMUM COST AGENT:",maxAgent," WITH COST: ",maxCost)


def computeCumulativeAverageTargetCost(agents, mTargets):
    sumCTPC = 0
    for i in agents:
        for j in i.path.path:
            sumCTPC += len(j)
    avgCTPC = sumCTPC % mTargets
    print("AVERAGE TARGET PATH COST:", avgCTPC)


def moveOneStep(mapp, xCoord, yCoord):
    if not (mapp[xCoord][yCoord] == "R"):
        mapp[xCoord][yCoord] =  "R"
    return mapp

def deleteOldPosition(mapp,xCoord,yCoord):
    if mapp[xCoord][yCoord] == "R":
        mapp[xCoord][yCoord] = "*"
    return mapp

def moveAlongPaths(agents, step, mapp):
    nodeToMove = []
    nodeToDelete = []
    for i in agents:
        try:
            nodeToMove.append(i.path.path[-1][step])
            nodeToDelete.append(i.path.path[-1][step-1])
        except:
            pass
    for i in nodeToMove:
        mapp = moveOneStep(mapp,i.xCoord,i.yCoord)
    for i in nodeToDelete:
        mapp = deleteOldPosition(mapp, i.xCoord, i.yCoord)

    printMap(mapp)

def printMap(mapp):
    for i in mapp:
        print("".join(i))


def getMaxLenght(agents):
    maxL = 0
    for i in agents:
        leng = len(i.path.path[-1])
        if leng > maxL:
            maxL = leng
    return maxL


def move(mapp, agents):
    printMap(mapp.map)
    for i in mapp.robotPos:
        mapp.map = deleteOldPosition(mapp.map, i[0], i[1])
    for i in range(getMaxLenght(agents)):
        print("\n\n\n\n\n\n\n\n",i,"step")
        moveAlongPaths(agents, i, mapp.map)
        time.sleep(1.5)


def startClusteringRouting(mapp,targetClustering):
    targetClustering.step()
    targetClustering.step()
    targetClustering.step()
    targetClustering.step()

def startRouting(path):
    mapp = MapHandler(path)
    mapp.readMap()
    targetClustering = TargetClustering(mapp.map, mapp.targetPos)
    agents = targetClustering.agents
    startClusteringRouting(mapp, targetClustering)
    #computeTotalCost(agents)
    #computeMaxPathCost(agents)
    #computeCumulativeAverageTargetCost(auction.schedule.agents,len(mapp.targetPos))


    print("\n\n\n\n\n\n\n\nAllocation Terminated, start moving along the paths...\n\n\n\n\n\n\n\n\n\n")
    #time.sleep(3)
    print("\n\n\n\n")
    #move(mapp, agents)


startRouting("MapEasyWOR")
