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

'''
    print(0 ,"^ STEP////////////////////////////////////////////")
    auction.step()
    print("\n\nSTATE OF AGENTS AT THE END OF ROUND 0\n\n\n")
    for i in auction.schedule.agents:
        i.resetState()
        i.printState()
    print(0, "^END STEP////////////////////////////////////////////")
    print(1, "^ STEP////////////////////////////////////////////")
    print("\n\nSTATE OF AGENTS AT THE END OF ROUND 1\n\n\n")
    auction.step()
    for i in auction.schedule.agents:
        i.resetState()
        i.printState()

    print(2, "^ STEP////////////////////////////////////////////")
    auction.step()
    print("\n\nSTATE OF AGENTS AT THE END OF ROUND 2\n\n\n")
    for i in auction.schedule.agents:
        i.resetState()
        i.printState()
    print(2, "^ STEP////////////////////////////////////////////")

    print(3, "^ STEP////////////////////////////////////////////")
    auction.step()
    print("\n\nSTATE OF AGENTS AT THE END OF ROUND 3\n\n\n")
    for i in auction.schedule.agents:
        i.resetState()
        i.printState()
    print(3, "^ STEP////////////////////////////////////////////")

'''
startRouting("Map2.txt")
