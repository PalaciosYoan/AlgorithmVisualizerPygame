class InsertionSortMapGenerator(object):
    """
    This class is generate and update Array that we are sorting.
    Flow of the class
    first enter # of integers that will be in the array until type End to end the input
    the array will then start to sort itself
    """
    def __init__(self) -> None:
        # integerArrayInput = input("Please enter integers you want sorted. Type in End to stop inputting integers: ")
        # inputArray = []
        # while integerArrayInput != "End":
        #     inputArray.append(int(integerArrayInput)) 
        #     integerArrayInput = input()
        self.array = [1,3,5,2,10,7,3]
        self.inputArraySize = len(self.array)

    def getArray(self):
        return self.array

    def getArraySize(self):
        return self.inputArraySize

    def swapValuesAtIndices(self, indexOne, indexTwo):
        self.array[indexOne], self.array[indexTwo] = self.array[indexTwo], self.array[indexOne]
    
    def valueAtIndex(self, index):
        return self.array[index]

    

"""
Resources used to help me
https://www.w3schools.com/python/ref_func_input.asp
https://stackoverflow.com/questions/55671872/python-comparison-if-statement-not-working
"""
