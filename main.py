
# coding: utf-8

# In[1]:

import matplotlib.plot as plt
import numpy as np


# In[2]:

class Car(object):

    def __init__(self, edge, x, route,speed):
       self.edge = edge
       self.route = route
       self.x = x
       self.speed=speed
       # Visualisation point
       self.vis = plt.plot(0,0, 'ro', markersize=4)[0]

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
             if var<=0.5:
                 self.speed-=1

    def setNewEdge(self):
        del self.route[0]
        if len(self.route) != 0:
            self.edge = route[0]
        else: self.edge = False

    def updateLocation(self):
        newX = self.x + self.speed*timestep
        # Updating visualisation information
        self.vis.set_data(newX,0)
        # Updating location
        self.x = newX

    def distanceRule(self,frontCar):
        difference=frontCar.getx()-self.x
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

totCars = 10
influx = 1 #cars per timestep
timestep = 1 #seconds per timestep
time = 100
maxSpeed = 5

def addNewCars(influx):
    newCars = []
    for i in influx:
        numEdges = random([1,10])
        startEdge = random(network)
        route = [startEdge]
        car = Car(route)
        newCars.append(car)
    return newCars


# In[3]:

if __name__ == '__main__':
# Activate interactive visualisation
    plt.ion()
# Initialise network, for now only one road
    road = Edge((0,0),(100,0))

    # Generate all agents
    cars = []
    for c in range(totCars):
        pass

    for t in range(time):
        cars.append(Car(road, 0, [road], maxSpeed))
            
        for n, car in enumerate(cars):
            car.accelerationRule()
            car.randomizationRule()
            if n != 0:
                frontCar = cars[n-1]
                car.distanceRule(frontCar)
            car.updateLocation()
#             if not car.getLocation() == offMap:
#                 newCarList.append(car)

        plt.pause(0.1)


    averageSpeed = sum([car.getAverageSpeed() for car in cars])/len(cars)


# In[11]:



