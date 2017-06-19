import matplotlib.plot as plt
import numpy as np

<<<<<<< HEAD

class Car(object):
	def __init__(self):
		#NICK TSAKMAKIDIS IS A COMPUTER SCIENTIST
=======
class Car(object):
<<<<<<< HEAD
	def __init__(self):
		#NICK TSAKMAKIDIS IS A COMPUTER SCIENTISThhhhee
=======
	def __init__(self, edge, route):
	   self.edge = edge
      self.route = route
      # test

    def getEdge(self):
        return self.edge

    def setNewEdge(self):
        del self.route[0]
        if len(self.route) != 0:
            self.edge = route[0]
        else: self.edge = False

    def setNewLocation(self, acceleration):
        pass
>>>>>>> 23d671f63195ac45f6ed774e46a41d6a2f1f4175
>>>>>>> 24c6bb875d2356f8a7f86bdf8263020cd799a3b4

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

def accelerationRule(distance,speed):
	# Nagel-Schreckenberg
	safedist=2*speed
	if distance<safedist:
		return distance/safedist
	else
		return 1

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


# NIkoleta
