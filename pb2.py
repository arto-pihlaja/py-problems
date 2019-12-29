def findIndices(intList, target):
    # Find two int in the list that add to target
    for i in range(0,len(intList)):
        for j in range(i+1, len(intList)):
            if intList[i] + intList[j] == target:
                return (i, j)