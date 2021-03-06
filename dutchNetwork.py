import numpy as np
import random
import copy
import pandas
import matplotlib.pyplot as plt

class Car(object):
    def __init__(self, edge, route, speed):
        self.edge = edge
        edge.addCar(self)
        self.route = route
        self.pos = 0
        self.speed = speed
        self.age = 0
        self.aveSpeed = 0

    def getPos(self):
        return self.pos

    def getEdge(self):
        return self.edge

# The three speed rules
    def accelerationRule(self):
        if self.speed <= maxSpeed - maxSpeed/steps:
            self.speed += maxSpeed/steps

    def randomizationRule(self):
        var = np.random.uniform(0, 1)
        if self.speed > maxSpeed/steps:
            if var < p:
                self.speed -= maxSpeed/(steps)

    def distanceRule(self, frontCar):
        hisEdge = frontCar.getEdge()
        if hisEdge == self.edge:
            difference = frontCar.getPos() - self.pos
            # print(difference)
        else:
            difference = (
                 self.edge.getLength() - self.pos + frontCar.getPos())
        if 2*(difference + 2) < self.speed:
            self.speed = difference
            if self.speed < 0:
                self.speed = 0

# Updating locations and moving to new edges
    def setNewEdge(self):
        del self.route[0]
        if len(self.route) != 0:
            self.edge = self.route[0]
        else:
            self.edge = False

    def update(self, timestep):
        self.aveSpeed = (self.aveSpeed*self.age + self.speed)/(self.age + 1)
        self.age += 1

        distance = self.speed*timestep
        if self.pos + distance < self.edge.getLength():
            # Updating visualisation information
            self.pos += distance
            return True
        else:
            if len(self.route) == 0:
                self.pos += distance
                self.edge.removeCar(self)
                return False
            else:
                distance -= abs(self.edge.getLength() - self.pos)
                self.pos = distance
                self.edge.removeCar(self)
                self.edge = self.route[0]
                self.edge.addCar(self)
                del self.route[0]
                return True

    def getFrontCar(self):
        cars = self.edge.getCars()
        for n, car in enumerate(cars):
            if car == self:
                if n > 0:
                    return cars[n-1]
                break
        if len(self.route) != 0:
            nextCarList = self.route[0].getCars()
            if len(nextCarList) != 0:
                return nextCarList[-1]
        return False

    def activate(self):
        self.edge.addCar(self)
        updateSpeed(self)

    def getAverageSpeed(self):
        return self.aveSpeed


class Edge(object):
    def __init__(self, node1, node2, length):
        self.length = length
        self.node1 = node1
        self.node2 = node2
        self.cars = []

    def getLength(self):
        return self.length

    def addCar(self, car):
        self.cars.append(car)

    def update(self):
        self.cars = sorted(self.cars, key=lambda car: -car.getPos())

    def getStart(self):
        return self.node1

    def getEnd(self):
        return self.node2

    def removeCar(self, car):
        for n, myCar in enumerate(self.cars):
            if myCar == car:
                del self.cars[n]
                break
        else: print("Error: car was not removed")

    def getCars(self):
        return self.cars

    def resetCars(self):
        self.cars = []

# ==============
# Some constants
# ==============
totCars = 5000  # number of cars initiated in simulation
maxSpeed = 5   # maximum speed (m/s)
p = 0.1         # change of slowing down every speed update
interval = 0.4   # time steps between cars
steps = 5.0     # number of speed steps as interpreted from the CA model


def chooseRandomRoute(network, startNode, numEdges):
    route = []
    rNode = random.choice(network)
    lastNode = rNode.getStart()
    while True:
        options = []
        for edge in network:
            startNode = edge.getStart()
            if lastNode == startNode:
                options.append(edge)
        route.append(random.choice(options))
        lastNode = route[-1].getEnd()
        if len(route) == numEdges:
            break
    return route


def addNewCars(totCars, network):
    # Generate all agents
    cars = []
    for c in range(totCars):
        startNode = random.choice(network).getStart()
        numEdges = random.choice(range(4))+1
#        if c%100 == 0: print('Routing cars ',c+100)
        route = chooseRandomRoute(network, startNode, numEdges)
        speed = 0
        cars.append(Car(route[0], route[1:], speed))
    return cars


def updatePositions(cars, timestep, network):
    newCars = []
    # Locations are updated on every timestep
    for car in cars:
        onEdge = car.update(timestep)
        if onEdge:
            newCars.append(car)

    [edge.update() for edge in network]
    return newCars


def updateSpeed(car):
    car.accelerationRule()
    car.randomizationRule()
    frontCar = car.getFrontCar()
    if frontCar:
        car.distanceRule(frontCar)
    return


def runSimulation(cars, network):
    # Activate interactive visualisation

    activeCars = []
    t = 0
    while len(cars) > 0 or len(activeCars) > 0:
        # Speeds are updated on the end of every second!
        timeToNewCar = round(interval - t % interval, 2)
        if timeToNewCar < 1e-2:
            timeToNewCar = round(interval, 2)
        timeToSpeedUpdate = round(1 - t % 1, 2)
        if timeToSpeedUpdate < 1e-2:
            timeToSpeedUpdate = 1

        if timeToSpeedUpdate <= timeToNewCar:
            # First travel remaining distance
            timestep = timeToSpeedUpdate
            t += timestep
            activeCars = updatePositions(activeCars, timestep, network)
            # Then update speeds
            [updateSpeed(car) for car in activeCars]
            if timeToSpeedUpdate == timeToNewCar and len(cars) != 0:
                # Sometimes speed is updated while new car is added!
                activeCars.append(cars[0])
                cars[0].activate()
                del cars[0]
        else:
            # First travel remaining distance
            timestep = timeToNewCar
            t += timestep
            activeCars = updatePositions(activeCars, timestep, network)
            # Then add new car
            if len(cars) != 0:
                activeCars.append(cars[0])
                cars[0].activate()
                del cars[0]
        t = round(t, 2)
    return


if __name__ == "__main__":
    # edges = [[(0,10),(250,0), 250],
    # [(0,-10),(250,0), 250],
    # [(250,0),(500,0), 250]]
    edges = pandas.read_csv("dutchhighway.csv", sep=';', header=None).values
    edges += [(end, start, length) for start, end, length in edges]
    network = [Edge(start, end, float(length)) for start, end, length in edges]

    # Generate all agents
    probs = [0]#, .15]
    fluxes = [2, 1, .55, .45, .35, .2, .1, .05]
    data = []
    variances = []
    for p in probs:
        line = []
        lineVar = []
        for interval in fluxes:
            l = []
            for i in range(5):
                cars = addNewCars(totCars, network)
                runSimulation(copy.copy(cars), network)
                averageSpeed = sum([car.getAverageSpeed() for car in cars])/len(cars)
                l.append(averageSpeed)
                [edge.resetCars() for edge in network]
            var = np.std(l)/np.sqrt(len(l))
            averageSpeed = sum(l)/len(l)
            print(averageSpeed)
            lineVar.append(var)
            line.append(averageSpeed)
        data.append(line)
        variances.append(lineVar)

    print(data)
    for var, line in zip(variances, data):
        plt.errorbar(fluxes, line, var)
    plt.legend(probs)
    plt.gca().invert_xaxis()
    plt.xlabel('Time in between cars (s)')
    plt.ylabel('Average speed (m/s)')
    plt.show()
