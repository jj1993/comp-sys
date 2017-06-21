import matplotlib.plot as plt
import numpy as np

class Car(object):
	def __init__(self, edge, x, route,speed):
	   self.edge = edge
       self.route = route
	   self.x = x
	   self.speed=speed
	   # Visualisation point
	   self.vis = plt.plot(0,0, 'ro', markersize=4)[0]

    def getEdge(self):
        return self.edge

    def setNewEdge(self):
        del self.route[0]
        if len(self.route) != 0:
            self.edge = route[0]
        else: self.edge = False

    def setLocation(self, speed):
        newX = x + speed*timestep
		# Updating visualisation information
		self.vis.set_data(newX,0)
		# Updating location
		self.x = newX

class Edge(object):
	def __init__(self, node1, node2):
		x1, y1 = node1
		x2, y2 = node2
		plt.plot((x1,x2),(y1,y2))
		self.node1 = node1
		self.node2 = node2
		self.length = math.sqrt((x2-x1)**2 + (y2-y1)**2)

totCars = 10
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
def distance(car1,car2):
	return abs(car1.x-car2.X)

def newspeed(speed):
	return speed*acceleration

def computeNewLocation(acceleration, car):
	distance = acceleration*timestep
	thisEdge = car.getEdge()
	if thisEdge.length() - car.getLocation() < distance:
		car.setEdge(car.getNewEdge())
	car.setNewLocation()

if __name__ == '__main__':
	# Activate interactive visualisation
	plt.ion()
	# Initialise network, for now only one road
	road = Edge((0,0),(100,0))

	# Generate all agents
	carlist = []
	for c in range(totCars):
		pass

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
			
    	plt.pause(0.1)


	averageSpeed = sum([car.getAverageSpeed() for car in cars])/len(cars)
