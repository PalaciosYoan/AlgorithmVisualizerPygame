
def updateVisual(mapArr):
    mapArr.printRight()
    mapArr.printLeft()
    mapArr.printMid()

def binarySearch(mapArr, target):
    right, left = mapArr.getRight(), mapArr.getLeft()
    array = mapArr.getArray()
    updateVisual(mapArr)
    #checking base case
    if right < left:
        return -1


    mid = left + (right - left) // 2
    mapArr.setMid(mid)
    # If element is present at the middle itself
    if array[mid] == target:
        return mid

    # If element is smaller than mid, then it
    # can only be present in left subarray
    if array[mid] > target:
        mapArr.setLeft = left
        mapArr.setRight = mid-1

    # Else the element can only be present
    # in rightt subarray
    else:
        mapArr.setLeft(mid+1)
        mapArr.setRight(right)

    return binarySearch(mapArr, target)