


class BinarySearchMapGenerator(object):
    """
    This class will generate and update Array that we are searching.
    """
    def __init__(self) -> None:
        self._array = [1,2,3,4,5]
        self._left = 0
        self._right = len(self._array)
        self._mid = len(self._array)//2
    
    def printLeft(self):
        print("left: ",self._left)
    
    def printRight(self):
        print("right: ",self._right)
    
    def printMid(self):
        print("mid:", self._mid)
    
    def getLeft(self):
        return self._left
    
    def getRight(self):
        return self._right
    
    def getMid(self):
        return self._mid
    
    def getArray(self):
        return self._array
    
    def setLeft(self, left):
        self._left = left
    
    def setRight(self, right):
        self._right = right
    
    def setMid(self, mid):
        self._mid = mid
    
