from Algorithms.BinarySearch import *
from MapCreatorPygame.BinarySearchMapGenerator import *


def main():
    map = BinarySearchMapGenerator()
    print(binarySearch(map, 1))

if __name__ == "__main__":
    main()