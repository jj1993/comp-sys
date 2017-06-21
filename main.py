import matplotlib.pyplot as plt
import numpy as np
import random

class Car(object):

    def __init__(self, edge, route, speed):
       self.edge = edge
       self.route = route
       self.pos = 0
       self.speed=speed
       # Visualisation point
       x, y = edge.getStart()
       self.vis = plt.plot(x, y, 's', markersize=4)[0]

    def getPos(self):
        return self.pos

    def getEdge(self):
        return self.edge

# The three speed rules
    def accelerationRule(self):
        if self.speed < maxSpeed - 1:
           self.speed+=1

    def randomizationRule(self):
        if self.speed > 1:
             if np.random.uniform(0,1) < p:
                 self.speed -= 1

    def distanceRule(self, frontCar):
        hisEdge = frontCar.getEdge()
        if hisEdge == self.edge:
            difference = frontCar.getPos() - self.pos
            print('-  ',round(difference))
        else:
            difference = (
                 self.edge.getLength() - self.pos
                 + frontCar.getPos()
                 )
            print('+  ',round(difference))

        difference = abs(difference)
        if difference + 2 < self.speed:
            self.speed=difference

# Updating locations and moving to new edges
    def setNewEdge(self):
        del self.route[0]
        if len(self.route) != 0:
            self.edge = route[0]
        else: self.edge = False

    def updateLocation(self):
        distance = self.speed*timestep
        if self.pos + distance < self.edge.getLength():
            # Updating visualisation information
            self.pos += distance
            x, y = self.edge.getXY(self.pos)
            self.vis.set_data(x, y)
            return True
        else:
            if len(self.route) == 0:
                self.vis.remove()
                self.pos += distance
                self.edge.removeCar(self)
                return False
            else:
                distance -= self.edge.getLength() - self.pos
                self.pos = distance
                self.edge.removeCar(self)
                self.edge = self.route[0]
                self.edge.addCar(self)
                del self.route[0]
                x, y = self.edge.getXY(self.pos)
                self.vis.set_data(x, y)
                return True

    def getFrontCar(self):
        for car in self.edge.getCars():
            if car.getPos() > self.pos:
                return car
        if len(route) != 0:
            nextCarList = route[0].getCars()
            if len(nextCarList) != 0:
                print("CAR ON DIFFERENT EDGE")
                return nextCarList[-1]
        return False

    def activate(self):
        self.edge.addCar(self)


class Edge(object):
    def __init__(self, node1, node2):
        x1, y1 = node1
        x2, y2 = node2
        plt.plot((x1,x2),(y1,y2))
        self.length = np.sqrt((x2-x1)**2 + (y2-y1)**2)
        self.angle = np.arctan((y2-y1)/(x2-x1))
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
        self.cars = []

    def getLength(self):
        return self.length

    def getStart(self):
        return (self.x1, self.y1)

    def getXY(self, pos):
        x = self.x1 + np.cos(self.angle)*pos
        y = self.y1 + np.sin(self.angle)*pos
        return (x, y)

    def addCar(self, car):
        self.cars.append(car)

    def removeCar(self, car):
        for n, myCar in enumerate(self.cars):
            if myCar == car:
                del self.cars[n]
                return

    def getCars(self):
        return self.cars

# Some constants
totCars = 10
influx = 1 #cars per timestep
timestep = 1 #seconds per timestep
time = 100
maxSpeed = 5
p = 0.5

if __name__ == '__main__':
    # Activate interactive visualisation
    plt.ion()
    # Initialise network, for now only one road
    road1 = Edge((0,0),(100,0))
    road2 = Edge((100,0),(200,-10))
    road3 = Edge((100,0),(200,10))

    # Generate all agents
    cars = []
    activeCars = []
    for c in range(totCars):
        road = random.choice([road2, road3])
        route = [road1, road]
        speed = maxSpeed - 2 + 2*np.random.random()
        cars.append(Car(route[0], route[1:], speed))

    for t in range(time):
        if t%1 == 0 and len(cars) != 0:
            cars[0].activate()
            activeCars.append(cars[0])
            del cars[0]

        newActiveCars = []
        for n, car in enumerate(activeCars):
            # if not (n == 0 and not (t < 10 or t > 25)):
            car.accelerationRule()
            car.randomizationRule()
            if n != 0:
                frontCar = car.getFrontCar()
                if frontCar:
                    car.distanceRule(frontCar)

        for car in activeCars:
            onEdge = car.updateLocation()
            if onEdge:
                newActiveCars.append(car)

        print([round(car.getPos()) for car in newActiveCars])
        activeCars = newActiveCars
        plt.pause(0.5)

    averageSpeed = sum([car.getAverageSpeed() for car in cars])/len(cars)

# In[11]:
