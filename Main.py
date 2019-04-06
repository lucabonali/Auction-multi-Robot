from MapHandler import *
from Auction import Auction


def startAuction(auction, mapp):
    for i in range(len(mapp.targetPos)):
        print("\n\n", i, "^ STEP////////////////////////////////////////////\n\n")
        auction.step()
        for j in auction.schedule.agents:
            j.resetState()


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


def startRouting(path):
    mapp = MapHandler(path)
    mapp.readMap()
    auction = Auction(path)
    startAuction(auction, mapp)
    computeTotalCost(auction.schedule.agents)
    computeMaxPathCost(auction.schedule.agents)
    computeCumulativeAverageTargetCost(auction.schedule.agents,len(mapp.targetPos))




startRouting("Map2.txt")
