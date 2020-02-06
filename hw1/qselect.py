import random
def qselect(k, inputArr):

    if inputArr == []:
        return []
        
    pivot = inputArr[random.randint(0, len(inputArr) - 1)]
    left = [x for x in inputArr if x < pivot]
    right = [x for x in inputArr if x > pivot]

    lenLeft = len(left)
    leftOvers = len(inputArr) - len(right)

    if lenLeft > k-1:
        return qselect(k, left)
    elif leftOvers <= k-1:
        return qselect(k-leftOvers, right)
    return pivot
