# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 21:05:45 2023

@author: dalib
"""

import os
import copy
import itertools
from PySide6.QtGui import QAction
import pyqtgraph as pg
from WeatherStation.App.DataReaders import HtmlReader
from WeatherStation.App.PrettyData import PrettyData


uiFile = "MainWindow.ui"

if os.path.dirname(__file__) != "":
    uiFile = "\\" + uiFile

uiclass, baseclass = pg.Qt.loadUiType(os.path.dirname(__file__) + uiFile)

class MainWindow(uiclass, baseclass):
    '''Class for controlling the MainWindow UI'''
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        self.reader = HtmlReader.HTMLReader("")
        self.data = PrettyData(self.reader)
        self.graphs = [self.temperatureGraph, self.windGraph, self.pressureGraph]
        #Dropdown menu
        self.setUpDropDownMenu()
        #Plot styles
        self.setUpPlots()
        #Make plots pretty
        pg.setConfigOptions(antialias=True)
        
    def setUpDropDownMenu(self):
        '''Creates a drop down menu populated with actions'''
        self.menuBar = self.menuBar()
        self.dropList = self.menuBar.addMenu("Data") 
        #Populate the action menu with filenames of loaded data
        self.currPath = os.path.dirname(__file__)
        filenames = os.listdir( self.currPath + "/Data")
        for filename in itertools.islice(filenames, 0, 24):
            self.dropList.addAction(filename)
        self.dropList.triggered[QAction].connect(self.onChosenFile)

    def setUpPlots(self):
        '''Set up plots style (labels, background etc.)'''
        self.labelStyle = {'color':'k', 'font-size':'20px'}
        self.plotPen = pg.mkPen(color=(255, 0, 0), width = 3)
        #Set background and labels for all graphs in view
        for graph in self.graphs:
            graph.setBackground('w')
            graph.showGrid(x=True, y=True)
            graph.setLabel('bottom', 'Time', **self.labelStyle)
    
    def updatePlots(self):
        '''Updates all plots on the ui'''
        self.setCurrentPlotTitles()
        self._updateTemperatureGraph()
        self._updateWindGraph()
        self._updatePressureGraph()
    
    def setCurrentPlotTitles(self):
        '''Set the graph title based on the data chosen'''
        currentTitle = self.data.dataTable["CityName"]
        #Set the graphs title based on the city name
        for graph in self.graphs:
            if len(currentTitle) == 1:
                graph.setTitle(currentTitle[0], color='k', size='20pt')
            else:
                graph.setTitle("", color='k', size='20pt')
            
    def readData(self, filename):
        '''Reads the data chosen from the drop down menu'''
        self.data.updateReader(self.currPath + "/Data/" + filename)
        self.data.updateDataTable()
    
    def onChosenFile(self, action):
        '''Retrives and displays the chosen data'''
        self.readData(action.text())
        self.updatePlots()

    def _refineLabels(self, labels, spreadFactor):
        '''Refines the time labels so that they fit nicely on to the plot'''
        for i, values in enumerate(labels):
            if not i % spreadFactor:
                splitLabel = values.split(",")
                if len(splitLabel) == 2:
                    labels[i] = splitLabel[1]
            else:
                labels[i] = ""
        return labels
        
    def _updateTemperatureGraph(self):
        '''Updates the temperature graph'''
        #Update x and y axis data
        #Thin out the time data string so they do not overlap when displayed
        timeStamps = []
        if "Time" in self.data.dataTable.keys():
            timeStamps = copy.deepcopy(self.data.dataTable["Time"])
            
        refinedTimeStamps = self._refineLabels(timeStamps, 8)
        timeStampTuple= tuple(enumerate(refinedTimeStamps))
        labels = list(dict(timeStampTuple).keys())
        #X axis data
        xAxis = self.temperatureGraph.getAxis("bottom")
        xAxis.setTicks([timeStampTuple])
        #Y axis data
        temperature = []
        if "Temperature" in self.data.dataTable.keys():
            temperature = self.data.dataTable["Temperature"]
        #Update plot
        self.temperatureGraph.clear()
        self.temperatureGraph.setLabel('left', 'Temperature [°C]', **self.labelStyle)
        self.temperatureGraph.plot(labels, temperature, pen=self.plotPen, symbol="o")
        
    def _updateWindGraph(self):
        '''Updates the wind graph'''
        #Update x and y axis data
        #refine the x axis labels so they do not overlap on the plot
        timeStamps = []
        if "Time" in self.data.dataTable.keys():
            timeStamps = copy.deepcopy(self.data.dataTable["Time"])
            
        refinedTimeStamps = self._refineLabels(timeStamps, 8)
        timeStampTuple= tuple(enumerate(refinedTimeStamps))
        labels = list(dict(timeStampTuple).keys())
        #X axis data
        xAxis = self.windGraph.getAxis("bottom")
        xAxis.setTicks([timeStampTuple])
        #Y axis data
        windSpeed = []
        if "Time" in self.data.dataTable.keys():
            windSpeed = self.data.dataTable["Wind speed"]
        #Update plot
        self.windGraph.clear()
        self.windGraph.setLabel('left', 'Wind speed [km/h]', **self.labelStyle)
        self.windGraph.plot(labels, windSpeed, pen=self.plotPen, symbol="o")
        
    def _updatePressureGraph(self):
        '''Updates the humidity graph'''
        #Update x and y axis data
        #refine the x axis labels so they do not overlap on the plot
        timeStamps = []
        if "Time" in self.data.dataTable.keys():
            timeStamps = copy.deepcopy(self.data.dataTable["Time"])
            
        refinedTimeStamps = self._refineLabels(timeStamps, 8)
        timeStampTuple= tuple(enumerate(refinedTimeStamps))
        labels = list(dict(timeStampTuple).keys())
        #X axis data
        xAxis = self.pressureGraph.getAxis("bottom")
        xAxis.setTicks([timeStampTuple])
        #Y axis data
        pressure = []
        if "Pressure" in self.data.dataTable.keys():
            pressure = self.data.dataTable["Pressure"]
        #Update plot
        self.pressureGraph.clear()
        self.pressureGraph.setLabel('left', 'Pressure [hPa]', **self.labelStyle)
        self.pressureGraph.plot(labels, pressure, pen=self.plotPen, symbol="o")
