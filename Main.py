from MapHandler import *
from Auction import Auction

def startRouting(path):
    mapp = MapHandler(path)
    mapp.readMap()
    auction = Auction(path)

    for i in range(len(mapp.targetPos)):
        print("\n\n",i, "^ STEP////////////////////////////////////////////\n\n")
        auction.step()
        #print("\n\nSTATE OF AGENTS AT THE END OF ROUND ", i ,"\n\n\n")
        for j in auction.schedule.agents:
            j.resetState()
            #j.printState()
    print(auction.schedule.agents[0].targets)


startRouting("Map.txt")
