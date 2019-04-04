from MapHandler import *
from Auction import Auction


def startAuction(auction, mapp):
    for i in range(len(mapp.targetPos)):
        print("\n\n", i, "^ STEP////////////////////////////////////////////\n\n")
        auction.step()
        # print("\n\nSTATE OF AGENTS AT THE END OF ROUND ", i ,"\n\n\n")
        for j in auction.schedule.agents:
            j.resetState()
            # j.printState()


def computeCost(agents):
    cost = 0
    for i in agents:
        for j in i.path.path:
            for k in j:
                cost += 1
    return cost



def startRouting(path):
    mapp = MapHandler(path)
    mapp.readMap()
    auction = Auction(path)
    startAuction(auction, mapp)
    cost = computeCost(auction.schedule.agents)




startRouting("MapEasy")
