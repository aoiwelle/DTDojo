class CyclicWords(object):
    def getCyclicGroupings(self, list):
        listOfGroups = []
        for x in list:
            if self.getIndexOfOccurrence(listOfGroups, x) == -1:
                listOfGroups.append([x])
        return listOfGroups
    
    def getIndexOfOccurrence(self, groups, valueToTest):
        for y in range(len(groups)):
            firstNode = groups[y][0]
            if len(firstNode) != len(valueToTest):
                continue
            elif firstNode == valueToTest:
                return y
            else:
                for x in range(len(valueToTest)-1):
                    substr = valueToTest[:(len(valueToTest)-1-x)]
                    indexOfSubStr = firstNode.rfind(substr)
                    if indexOfSubStr>0:
                        substr = valueToTest[(len(valueToTest)-1-x):]
                        firstNodeSub = firstNode[:indexOfSubStr]
                        if substr == firstNodeSub:
                            for z in groups[y][1:]:
                                if z == valueToTest:
                                    return y
                            groups[y].append(valueToTest)
                            return y
        return -1

