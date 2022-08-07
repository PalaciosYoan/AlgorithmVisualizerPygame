from Algorithms.BinarySearch import *
from MapCreatorPygame.BinarySearchMapGenerator import *
from Algorithms.InsertionSort import *
from MapCreatorPygame.InsertionSortMapGenerator import *


def main():
    map = BinarySearchMapGenerator()
    print(binarySearch(map, 1))

    insertionMap = InsertionSortMapGenerator()
    insertionSort(insertionMap)

if __name__ == "__main__":
    main()