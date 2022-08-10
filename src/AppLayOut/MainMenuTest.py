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
    stop = threading.Event()
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)

class SelectionScreen(Screen):
    stop = threading.Event()
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
        self.startButton = Button(text = 'Click to start the Algorithm', size_hint = (0.5, 0.25))
        self.startButton.bind(on_press = self.start_second_thread)
        self.styleLayout.add_widget(self.startButton)
        self.add_widget(self.styleLayout)

    def start_second_thread(self, *args):
        self.styleLayout.remove_widget(self.startButton)
        threading.Thread(target=self.insertionSortAlgorithm).start()

    def insertionSortAlgorithm(self, *args):
        for index in range(1,self.insertionMap.getArraySize()):
            traversalIndex = index
            currentIndexForLayout = -1 * (traversalIndex + 1)
            previousIndexForLayout = -1 * traversalIndex
            staticCurrentIndexForLayout = currentIndexForLayout
            numberTimesSwapped = 0
            Clock.schedule_once(partial(self.changeTextAndColor, currentIndexForLayout, previousIndexForLayout),0)
            time.sleep(2)

            #swapping the values mentioned above if the previous value is larger than the current value
            print("before the swap: ", currentIndexForLayout, " " , previousIndexForLayout)
            while traversalIndex > 0 and self.insertionMap.valueAtIndex(traversalIndex - 1) > self.insertionMap.valueAtIndex(traversalIndex):
                Clock.schedule_once(partial(self.swapTextAndChangeTextAndColor, traversalIndex, currentIndexForLayout, previousIndexForLayout),0)
                time.sleep(2)
                traversalIndex -= 1
                currentIndexForLayout += 1
                previousIndexForLayout += 1
                numberTimesSwapped += 1
            Clock.schedule_once(partial(self.changeColor, staticCurrentIndexForLayout, numberTimesSwapped),0)
            print("After the swap: ", currentIndexForLayout, " " , previousIndexForLayout)
            if self.stop.is_set():
                return
            time.sleep(1)
        Clock.schedule_once(self.changeTextAndButton, 0)
        if self.stop.is_set():
                return


    @mainthread
    def changeToSelectionScreen(self, *args):
        self.manager.current = 'Selection Screen'
    
    @mainthread
    def changeTextAndColor(self, currentIndexForLayout, previousIndexForLayout, *args):
        self.styleLayout.children[0].text = "Comparing these two values: " + self.insertionLayout.children[previousIndexForLayout].text + " and " + self.insertionLayout.children[currentIndexForLayout].text
        self.insertionLayout.children[previousIndexForLayout].color = (0,1,0,1)
        self.insertionLayout.children[currentIndexForLayout].color = (0,1,0,1)
    
    @mainthread
    def swapTextAndChangeTextAndColor(self, traversalIndex, currentIndexForLayout, previousIndexForLayout, *args):
        self.insertionLayout.children[previousIndexForLayout].color = (0,1,0,1)
        self.insertionLayout.children[currentIndexForLayout].color = (0,1,0,1)
        self.styleLayout.children[0].text = "Swapping these two values: " + self.insertionLayout.children[previousIndexForLayout].text + " and " + self.insertionLayout.children[currentIndexForLayout].text
        self.insertionMap.swapValuesAtIndices(traversalIndex - 1, traversalIndex)
        self.insertionLayout.children[previousIndexForLayout].text, self.insertionLayout.children[currentIndexForLayout].text = self.insertionLayout.children[currentIndexForLayout].text, self.insertionLayout.children[previousIndexForLayout].text

    @mainthread
    def changeColor(self, staticCurrentIndexForLayout, numberOfTimesSwapped, *args):
        if numberOfTimesSwapped != 0:
            while numberOfTimesSwapped >= 0:
                self.insertionLayout.children[staticCurrentIndexForLayout].color = (1,1,1,1)
                staticCurrentIndexForLayout += 1
                numberOfTimesSwapped -= 1
        else:
            self.insertionLayout.children[staticCurrentIndexForLayout].color = (1,1,1,1)
            self.insertionLayout.children[staticCurrentIndexForLayout + 1].color = (1,1,1,1)
        
    
    @mainthread
    def changeTextAndButton(self, *args):
        self.styleLayout.children[0].text = "Finished! Click on the button to go back to the selection menu"
        self.startButton.text = "Go back to Selection Menu"
        self.styleLayout.add_widget(self.startButton)
        self.startButton.bind(on_press = self.changeToSelectionScreen)

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