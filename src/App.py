
from Algorithms.BinarySearch import *
from MapCreatorPygame.BinarySearchMapGenerator import *
from Algorithms.InsertionSort import *
from MapCreatorPygame.InsertionSortMapGenerator import *
from AppLayOut.MainMenuLayOut import *

insertionMap = InsertionSortMapGenerator()
insertionSort(insertionMap)

if __name__ == "__main__":
    helloKivy = HelloKivy()
    helloKivy.run()
    #main()