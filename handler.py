import re


class FactHandler:

    # In other languages it's called a constructor

    # def __init__(self)

    # Take all available options from the input file

    # Also sets options as keys with their corresponding -
    # facts (True|False) as values in a dictionary then
    # returns the dictionary

    def getOptions(self, col1):
        options = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        listString = "".join(list(map("".join, col1)))
        optDict = {}
        for x in options:
            if x in listString:
                optDict[x] = False
        return optDict

    #  Goes though the dictionary and change all the given options' -
    # facts from False to true then return the updated fact dictionary

    def validateAvailableOptions(self, col1):
        col2 = list(map("".join, col1))
        factDict = self.getOptions(col1)
        r = re.compile(r"=[A-Z]*$")
        newlist = list(filter(r.match, col2))
        if len(newlist) == 1:
            for key in newlist[0]:
                if key in factDict:
                    factDict[key] = True
        return factDict

