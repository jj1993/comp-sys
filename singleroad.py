
# coding: utf-8

# In[1]:

import matplotlib.pyplot as plt
import numpy as np


# In[2]:

class Car(object):

    def __init__(self, edge, x, route, speed):
       self.edge = edge
       self.route = route
       self.x = x
       self.speed=speed
       # Visualisation point
       self.vis = plt.plot(0,0, 's', markersize=4)[0]

    def accelerationRule(self):
        if self.speed < maxSpeed:
           self.speed+=1

    def getx(self):
        return self.x

    def getEdge(self):
        return self.edge

    def randomizationRule(self):
        var=np.random.uniform(0,1)
        if self.speed >=1:
             if var<=p:
                 self.speed-=1

    def setNewEdge(self):
        del self.route[0]
        if len(self.route) != 0:
            self.edge = route[0]
        else: self.edge = False

    def updateLocation(self):
        self.x += self.speed*timestep
        if self.x < self.edge.getLength():
            # Updating visualisation information
            self.vis.set_data(self.x,0)
            return True
        else:
            self.vis.remove()
            return False

    def distanceRule(self,frontCar):
        difference = frontCar.getx()-self.x - 2
        if difference<self.speed:
           self.speed=difference


class Edge(object):
    def __init__(self, node1, node2):
        x1, y1 = node1
        x2, y2 = node2
        plt.plot((x1,x2),(y1,y2))
        self.node1 = node1
        self.node2 = node2
        self.length = np.sqrt((x2-x1)**2 + (y2-y1)**2)

    def getLength(self):
        return self.length

# Some constants
totCars = 10
influx = 1 #cars per timestep
timestep = 1 #seconds per timestep
time = 100
maxSpeed = 5
p = 0.5

def addNewCars(influx):
    newCars = []
    for i in influx:
        numEdges = random([1,10])
        startEdge = random(network)
        route = [startEdge]
        car = Car(route)
        newCars.append(car)
    return newCars

if __name__ == '__main__':
    # Activate interactive visualisation
    plt.ion()
    # Initialise network, for now only one road
    road1 = Edge((0,0),(100,0))

    # Generate all agents
    cars = []
    activeCars = []
    for c in range(totCars):
        speed = maxSpeed - 2 + 2*np.random.random()
        cars.append(Car(road, 0, [road], speed))

    for t in range(time):
        if t%1 == 0 and len(cars) != 0:
            activeCars.append(cars[0])
            del cars[0]

        newActiveCars = []
        for n, car in enumerate(activeCars):
            # if not (n == 0 and not (t < 10 or t > 25)):
            car.accelerationRule()
            car.randomizationRule()
            if n != 0:
                frontCar = activeCars[n-1]
                car.distanceRule(frontCar)
            onEdge = car.updateLocation()
            if onEdge:
                newActiveCars.append(car)

        activeCars = newActiveCars
        plt.pause(0.5)


    averageSpeed = sum([car.getAverageSpeed() for car in cars])/len(cars)

# In[11]:
