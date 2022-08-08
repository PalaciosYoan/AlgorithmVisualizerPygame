def showUpdatedVisual(array):
    print("Current Array: ", array.getArray())

def showSortedVisual(array):
    print("Sorted Array: ", array.getArray())

def insertionSort(array):
    for index in range(1,array.getArraySize()):
        #showing current array in terminal
        showUpdatedVisual(array)

        traversalIndex = index
        print("Comparing these two values", array.valueAtIndex(traversalIndex - 1), array.valueAtIndex(traversalIndex))

        #swapping the values mentioned above if the previous value is larger than the current value
        while traversalIndex > 0 and array.valueAtIndex(traversalIndex - 1) > array.valueAtIndex(traversalIndex):
            print("Swapping these two values:", array.valueAtIndex(traversalIndex - 1), array.valueAtIndex(traversalIndex))
            array.swapValuesAtIndices(traversalIndex - 1, traversalIndex)
            traversalIndex -= 1

    showSortedVisual(array)