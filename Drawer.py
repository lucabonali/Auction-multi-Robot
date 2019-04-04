from colorama import Fore


class Drawer():
    def __init__(self, agent):
        self.colorList = []
        self.agentList = agent
        self.initializeColorList()

    def initializeColorList(self):
        self.colorList.append(Fore.GREEN)
        self.colorList.append(Fore.BLUE)
        self.colorList.append(Fore.RED)
        self.colorList.append(Fore.CYAN)
        self.colorList.append(Fore.LIGHTMAGENTA_EX)
        self.colorList.append(Fore.LIGHTGREEN_EX)
        self.colorList.append(Fore.LIGHTRED_EX)
        self.colorList.append(Fore.GREEN)
        self.colorList.append(Fore.BLUE)
        self.colorList.append(Fore.RED)
        self.colorList.append(Fore.CYAN)
        self.colorList.append(Fore.LIGHTMAGENTA_EX)
        self.colorList.append(Fore.LIGHTGREEN_EX)
        self.colorList.append(Fore.LIGHTRED_EX)
        self.colorList.append(Fore.GREEN)
        self.colorList.append(Fore.BLUE)
        self.colorList.append(Fore.RED)
        self.colorList.append(Fore.CYAN)
        self.colorList.append(Fore.LIGHTMAGENTA_EX)
        self.colorList.append(Fore.LIGHTGREEN_EX)
        self.colorList.append(Fore.LIGHTRED_EX)
        self.colorList.append(Fore.RED)
        self.colorList.append(Fore.CYAN)
        self.colorList.append(Fore.LIGHTMAGENTA_EX)
        self.colorList.append(Fore.LIGHTGREEN_EX)
        self.colorList.append(Fore.LIGHTRED_EX)
        self.colorList.append(Fore.GREEN)
        self.colorList.append(Fore.BLUE)
        self.colorList.append(Fore.RED)
        self.colorList.append(Fore.CYAN)
        self.colorList.append(Fore.LIGHTMAGENTA_EX)
        self.colorList.append(Fore.LIGHTGREEN_EX)
        self.colorList.append(Fore.LIGHTRED_EX)
        self.colorList.append(Fore.RED)
        self.colorList.append(Fore.CYAN)
        self.colorList.append(Fore.LIGHTMAGENTA_EX)
        self.colorList.append(Fore.LIGHTGREEN_EX)
        self.colorList.append(Fore.LIGHTRED_EX)
        self.colorList.append(Fore.GREEN)
        self.colorList.append(Fore.BLUE)
        self.colorList.append(Fore.RED)
        self.colorList.append(Fore.CYAN)
        self.colorList.append(Fore.LIGHTMAGENTA_EX)
        self.colorList.append(Fore.LIGHTGREEN_EX)
        self.colorList.append(Fore.LIGHTRED_EX)


    def colorPaths(self, mapChar):
        for i in self.agentList: # i is the agent iterator
            for j in i.path.path: # j is the track iterator
                for k in range(len(j)): # k is the node iterator inside the i agent and j-th track
                    if not (j[k].value == "T" or j[k].value == "t"):
                        xCoord = j[k].xCoord
                        yCoord = j[k].yCoord
                        mapChar[xCoord][yCoord] = self.colorList[i.unique_id] + "*" + Fore.WHITE


    def printMap(self, mapChar):
        self.colorPaths(mapChar)
        for i in mapChar:
            print("".join(i))

#to draw the map, needs the list of agents and the updated mapchar
'''
drawer = Drawer(self.schedule.agents)
drawer.printMap(self.mapChar)
'''