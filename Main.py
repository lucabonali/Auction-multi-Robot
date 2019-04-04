from MapHandler import *
from Auction import Auction

def startRouting(path):
    mapp = MapHandler(path)
    mapp.readMap()
    auction = Auction(path)
    for i in range(len(mapp.targetPos) +1):
        print(i,"^ STEP////////////////////////////////////////////")
        auction.step()
        print("END", i, "^ STEP//////////////////////////////////////////")


startRouting("Map2.txt")
