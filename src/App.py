from Algorithms.BinarySearch import *
from MapCreatorPygame.BinarySearchMapGenerator import *


def main():
    map = BinarySearchMapGenerator()
    print(binarySearch(map, 2))

if __name__ == "__main__":
    main()