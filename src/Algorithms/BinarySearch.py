
def updateVisual(mapArr):
    mapArr.printRight()
    mapArr.printLeft()
    mapArr.printMid()

def binarySearch(mapArr, target):
    while mapArr.getLeft() <= mapArr.getRight():
        updateVisual(mapArr=mapArr)
        mapArr.setMid((mapArr.getRight() + mapArr.getLeft()) // 2)

        # If x is greater, ignore left half
        if mapArr.getArrayAtMid() < target:
            mapArr.setLeft(mapArr.getMid() + 1)

        # If x is smaller, ignore right half
        elif mapArr.getArrayAtMid() > target:
            mapArr.setRight(mapArr.getMid() + 1)

        # means x is present at mid
        else:
            return mapArr.getMid()

    # If we reach here, then the element was not present
    return -1