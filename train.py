import os
import csv

dataFile = 'data.csv'
learningRate = 0.01
nIterations = 10


def estimatePrice (theta0, theta1, mileage):
    return theta0 + (theta1 * mileage)

def mean0 (x, y, theta0, theta1):
    m = len(x)
    adjustedSum = 0
    for i in range(m):
        adjustedSum += estimatePrice(theta0, theta1, x[i]) - x[i]
    return adjustedSum / m

def mean1 (x, y, theta0, theta1):
    m = len(x)
    adjustedSum = 0
    for i in range(m):
        adjustedSum += (estimatePrice(theta0, theta1, x[i]) - x[i]) * x[i]
    print(adjustedSum)
    return adjustedSum / m

def gradientDescent (x, y):
    theta0 = 1
    theta1 = 1
    for i in range(nIterations):
        print(theta0, theta1)
        tmpTheta0 = theta0 - learningRate * mean0(x, y, theta0, theta1)
        tmpTheta1 = theta1 - learningRate * mean1(x, y, theta0, theta1)
        theta0 = tmpTheta0
        theta1 = tmpTheta1
    return theta0, theta1

def readData ():
    x = []
    y = []
    with open(dataFile, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            try:
                x.append(int(row[0]))
                y.append(int(row[1]))
            except ValueError:
                pass
    return x, y



if os.path.isfile(dataFile):
    x, y = readData()
else:
    print("Error : no data available")
    sys.exit()

theta0, theta1 = gradientDescent(x, y)

print(theta0, theta1)