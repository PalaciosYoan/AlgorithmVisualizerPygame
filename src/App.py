from Algorithms.BinarySearch import *
from MapCreatorPygame.BinarySearchMapCreator import *


def main():
    map = BinarySearchMapGenerator()
    print(binarySearch(map, 3))

if __name__ == "__main__":
    main()