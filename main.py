import matplotlib.plot as plt
import numpy as np
import random

class Car(object):
	def __init__(self, edge, route):
		self.edge = edge
        self.route = route

    def getEdge(self):
        return self.edge

    def setNewEdge(self):
        del self.route[0]
        if len(self.route) != 0:
            self.edge = route[0]
        else: self.edge = False

    def setNewLocation(self, acceleration):
        pass

class Edge(object):
	def __init__(self, start, end):
        x1, y1 = start
        x2, y2 = end
		self.start = start
        self.end = end
        self.length = sqrt((x2-x1)**2 + (y2-y1)**2)
        self.cars = []

    def getLength(self):
        return self.length

    def addCar(self, car):
        cars.append(car)

    def getCars(self):
        return self.cars

influx = 1 #cars per timestep
timestep = 1 #minutes per timestep
network = [Edge((0,0),())]

def addNewCars(influx):
	newCars = []
	for i in influx:
		numEdges = random.randrange(1,10)
		startEdge = random.choice(network)
		route = [startEdge]
		car = Car(startEdge, route)
		newCars.append(car)
	return newCars

def accelerationRule(distance):
	# Nagel-Schreckenberg
	return

def computeNewLocation(acceleration, car):
	distance = acceleration*timestep
	thisEdge = car.getEdge()
	if thisEdge.length() - car.getLocation() < distance:
		car.setNewEdge()
	car.setNewLocation()

for t in time:
	cars += addNewCars(influx)
	newCarList = []
	for n, car in enumerate(cars):
		myLocation = car.getLocation()
		hisLocation = cars[n+1].getLocation()
		distance = hisLocation - myLocation
		acceleration = accelerationRule(distance)
		car.setLocation() = computeNewLocation(acceleration, car)
		if car.getEdge():
			newCarList.append(car)

averageSpeed = sum([car.getAverageSpeed() for car in cars])/len(cars)
