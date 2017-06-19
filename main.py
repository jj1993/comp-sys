import matplotlib.plot as plt
import numpy as np


class Car(object):
	def __init__(self):
		#NICK TSAKMAKIDIS IS A COMPUTER SCIENTISThhhhee

class Edge(object):
	def __init__(self):
		(...)

influx = 1 #cars per timestep
timestep = 1 #minutes per timestep
network = [Edge((0,0),())]

def addNewCars(influx):
	newCars = []
	for i in influx:
		numEdges = random([1,10])
		startEdge = random(network)
		route = [startEdge, …, …, …]
		car = Car(route)
		newCars.append(car)
	return newCars

def accelerationRule(distance):
	# Nagel-Schreckenberg
	return

def computeNewLocation(acceleration, car):
	distance = acceleration*timestep
	thisEdge = car.getEdge()
	if thisEdge.length() - car.getLocation() < distance:
		car.setEdge(car.getNewEdge())
	car.setNewLocation()

for t in time:
	cars += addNewCars(influx)
	newCarList = []
	for n, car in enumerate(cars):
		myLocation = car.getLocation()
		hisLocation = cars[n+1].getLocation()
		distance =hisLocation - myLocation
		acceleration = accelerationRule(distance)
		car.setLocation() = computeNewLocation(acceleration, car)
		if not car.getLocation() == offMap:
			newCarList.append(car)

averageSpeed = sum([car.getAverageSpeed() for car in cars])/len(cars)
