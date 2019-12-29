from functools import reduce
def calculateOneRatio(intArray, func):
    filteredList = list(filter(func,intArray))
    ratio = round(len(filteredList)/len(intArray),6)
    return ratio

def calculateRatios(intArray):
    return [calculateOneRatio(intArray, (lambda x:x>0)),\
        calculateOneRatio(intArray, (lambda x:x<0)),\
            calculateOneRatio(intArray, (lambda x:x==0))]