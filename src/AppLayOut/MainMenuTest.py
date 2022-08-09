import threading
import time
from functools import partial

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from kivy.uix.label import Label
from kivy.properties import NumericProperty
from kivy.clock import Clock, mainthread
from Algorithms.InsertionSort import *
from MapCreatorPygame.InsertionSortMapGenerator import *



class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)

class SelectionScreen(Screen):
    def __init__(self, **kwargs):
        super(SelectionScreen, self).__init__(**kwargs)
        screenLayout = BoxLayout(orientation = 'horizontal')
        binarySearchButton = Button(text = "Binary Search")
        binarySearchButton.bind(on_press=self.pressed)
        screenLayout.add_widget(binarySearchButton)
        insertionSortButton = Button(text = "Insertion Sort")
        insertionSortButton.bind(on_press=self.changeToInsertionSort)
        screenLayout.add_widget(insertionSortButton)
        
        self.add_widget(screenLayout)
    
    def pressed(self, instance):
        print(instance.text)
    
    def changeToInsertionSort(self, *args):
        self.manager.current = 'Insertion Sort'

class InsertionSortScreen(Screen):
    stop = threading.Event()
    def __init__(self, **kwargs):
        super(InsertionSortScreen, self).__init__(**kwargs)
        self.insertionMap = InsertionSortMapGenerator()
        self.styleLayout = GridLayout(rows = 3)
        self.insertionLayout = BoxLayout(orientation = 'horizontal')
        for element in self.insertionMap.getArray():
            self.insertionLayout.add_widget(Label(text = str(element)))
        #self.add_widget(insertionLayout)
        self.styleLayout.add_widget(self.insertionLayout)
        insertionSortDescription = Label(text = "Insertion Sort Method", size_hint = (0.5, 0.25))
        self.styleLayout.add_widget(insertionSortDescription)
        startButton = Button(text = 'Hello World', size_hint = (0.5, 0.25))
        startButton.bind(on_press = self.start_second_thread)
        self.styleLayout.add_widget(startButton)
        self.add_widget(self.styleLayout)

    def start_second_thread(self, *args):
        threading.Thread(target=self.pressed).start()

    def pressed(self, *args):
        for index in range(1,self.insertionMap.getArraySize()):
            traversalIndex = index
            currentIndexForLayout = -1 * (traversalIndex + 1)
            previousIndexForLayout = -1 * traversalIndex
            Clock.schedule_once(partial(self.changeTextAndColor, currentIndexForLayout, previousIndexForLayout),0)
            time.sleep(1)
            print("Comparing these two values Layout", self.insertionLayout.children[previousIndexForLayout].text, self.insertionLayout.children[currentIndexForLayout].text)
            #print("Comparing these two values Print", self.insertionMap.valueAtIndex(traversalIndex - 1), self.insertionMap.valueAtIndex(traversalIndex))

            #swapping the values mentioned above if the previous value is larger than the current value
            while traversalIndex > 0 and self.insertionMap.valueAtIndex(traversalIndex - 1) > self.insertionMap.valueAtIndex(traversalIndex):
                print("Swapping these two values Print:", self.insertionMap.valueAtIndex(traversalIndex - 1), self.insertionMap.valueAtIndex(traversalIndex))
                #print("Swapping these two values Layout", self.insertionLayout.children[previousIndexForLayout].text, self.insertionLayout.children[currentIndexForLayout].text)
                Clock.schedule_once(partial(self.swapTextAndChangeTextAndColor, traversalIndex, currentIndexForLayout, previousIndexForLayout),0)
                time.sleep(1)
                traversalIndex -= 1
                currentIndexForLayout += 1
                previousIndexForLayout += 1
            Clock.schedule_once(partial(self.changeColor, currentIndexForLayout, previousIndexForLayout),0)
            time.sleep(1)

    @mainthread
    def changeTextAndColor(self, currentIndexForLayout, previousIndexForLayout, *args):
        self.styleLayout.children[1].text = "Comparing these two values: " + self.insertionLayout.children[previousIndexForLayout].text + " and " + self.insertionLayout.children[currentIndexForLayout].text
        self.insertionLayout.children[previousIndexForLayout].color = (0,1,0,1)
        self.insertionLayout.children[currentIndexForLayout].color = (0,1,0,1)
    
    @mainthread
    def swapTextAndChangeTextAndColor(self, traversalIndex, currentIndexForLayout, previousIndexForLayout, *args):
        self.insertionLayout.children[previousIndexForLayout].color = (0,1,0,1)
        self.insertionLayout.children[currentIndexForLayout].color = (0,1,0,1)
        self.styleLayout.children[1].text = "Swapping these two values: " + self.insertionLayout.children[previousIndexForLayout].text + " and " + self.insertionLayout.children[currentIndexForLayout].text
        self.insertionMap.swapValuesAtIndices(traversalIndex - 1, traversalIndex)
        self.insertionLayout.children[previousIndexForLayout].text, self.insertionLayout.children[currentIndexForLayout].text = self.insertionLayout.children[currentIndexForLayout].text, self.insertionLayout.children[previousIndexForLayout].text

    @mainthread
    def changeColor(self, currentIndexForLayout, previousIndexForLayout, *args):
        self.insertionLayout.children[previousIndexForLayout].color = (1,1,1,1)
        self.insertionLayout.children[currentIndexForLayout].color = (1,1,1,1)
        
class MyApp(App):
    def on_stop(self):
        self.root.stop.set()

    def build(self):
        windowManager = ScreenManagement(transition = FadeTransition())
        windowManager.add_widget(SelectionScreen(name = 'Selection Screen'))
        windowManager.add_widget(InsertionSortScreen(name = 'Insertion Sort'))
        return windowManager

#https://stackoverflow.com/questions/57487117/some-troubles-using-screen-manager-without-kv-file
#https://stackoverflow.com/questions/31639452/kivy-access-child-id
#https://stackoverflow.com/questions/63867627/how-do-i-update-the-text-in-label-widget-within-the-for-loop
#https://github.com/kivy/kivy/wiki/Working-with-Python-threads-inside-a-Kivy-application


"""
    def pressed(self, instance):
        for index in range(1,self.insertionMap.getArraySize()):
            traversalIndex = index
            currentIndexForLayout = -1 * (traversalIndex + 1)
            previousIndexForLayout = -1 * traversalIndex
            self.insertionLayout.children[previousIndexForLayout].color = (0,1,0,1)
            self.insertionLayout.children[currentIndexForLayout].color = (0,1,0,1)
            self.styleLayout.children[1].text = "Comparing these two values: " + self.insertionLayout.children[previousIndexForLayout].text + " and " + self.insertionLayout.children[currentIndexForLayout].text
            print("Comparing these two values Layout", self.insertionLayout.children[previousIndexForLayout].text, self.insertionLayout.children[currentIndexForLayout].text)
            print("Comparing these two values Print", self.insertionMap.valueAtIndex(traversalIndex - 1), self.insertionMap.valueAtIndex(traversalIndex))

            #swapping the values mentioned above if the previous value is larger than the current value
            while traversalIndex > 0 and self.insertionMap.valueAtIndex(traversalIndex - 1) > self.insertionMap.valueAtIndex(traversalIndex):
                print("Swapping these two values Print:", self.insertionMap.valueAtIndex(traversalIndex - 1), self.insertionMap.valueAtIndex(traversalIndex))
                print("Swapping these two values Layout", self.insertionLayout.children[previousIndexForLayout].text, self.insertionLayout.children[currentIndexForLayout].text)
                self.insertionMap.swapValuesAtIndices(traversalIndex - 1, traversalIndex)
                self.insertionLayout.children[previousIndexForLayout].text, self.insertionLayout.children[currentIndexForLayout].text = self.insertionLayout.children[currentIndexForLayout].text, self.insertionLayout.children[previousIndexForLayout].text
                self.insertionLayout.children[previousIndexForLayout].color = (1,1,1,1)
                self.insertionLayout.children[currentIndexForLayout].color = (1,1,1,1)
                traversalIndex -= 1
                currentIndexForLayout += 1
                previousIndexForLayout += 1
"""