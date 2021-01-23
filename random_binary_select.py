import random

def randomBinaryItemSelect(iterations, items):
    itemsAmount = {}

    for _ in range(iterations):
        itemIndex = random.randint(0, len(items) - 1)
        itemSelected = items[itemIndex]

        if itemSelected in itemsAmount:
            itemsAmount[itemSelected] += 1
        else:
            itemsAmount[itemSelected] = 1

    return itemsAmount


def getItemsSelectedPercentages(itemsSelected):
    itemsCount = 0
    itemsDict = {}
    
    for value in itemsSelected.values():
        itemsCount += value

    for key, val in itemsSelected.items():
        itemsDict[key] = "{:.2f}".format((val / itemsCount) * 100) + "%"

    return itemsDict

coin = ["heads", "tails"]

coinFlipped10 = randomBinaryItemSelect(10, coin)
coinFlipped100 = randomBinaryItemSelect(100, coin)
coinFlipped1000 = randomBinaryItemSelect(1000, coin)
coinFlipped1000000 = randomBinaryItemSelect(1000000, coin)

print("Coin flipped 10 times resulted in:", getItemsSelectedPercentages(coinFlipped10))
print("Coin flipped 100 times resulted in:", getItemsSelectedPercentages(coinFlipped100))
print("Coin flipped 1000 times resulted in:", getItemsSelectedPercentages(coinFlipped1000))
print("Coin flipped 1000000 times resulted in:", getItemsSelectedPercentages(coinFlipped1000000), "\n")


marbles = ["red", "red", "red", "red", "white", "red", "red", "red", "red", "red"]

marbleGrabbed10 = randomBinaryItemSelect(10, marbles)
marbleGrabbed100 = randomBinaryItemSelect(100, marbles)
marbleGrabbed1000 = randomBinaryItemSelect(1000, marbles)
marbleGrabbed1000000 = randomBinaryItemSelect(1000000, marbles)

print("Marble grabbed 10 times resulted in:", getItemsSelectedPercentages(marbleGrabbed10))
print("Marble grabbed 100 times resulted in:", getItemsSelectedPercentages(marbleGrabbed100))
print("Marble grabbed 1000 times resulted in:", getItemsSelectedPercentages(marbleGrabbed1000))
print("Marble grabbed 1000000 times resulted in:", getItemsSelectedPercentages(marbleGrabbed1000000))