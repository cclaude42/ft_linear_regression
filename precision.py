#!/usr/bin/env python3
import os
import csv
import sys
import matplotlib.pyplot as plt


# Goal function
def estimatePrice (theta0, theta1, mileage):
    return theta0 + (theta1 * mileage)

# Compute precision
def computePrecision (x, y, theta0, theta1):
    m = len(x)
    errorSum = 0
    for i in range(m):
        error = (estimatePrice(theta0, theta1, x[i]) - y[i]) / y[i]
        if error > 0:
            errorSum += error
        else:
            errorSum -= error
    return errorSum / m

# Get theta values from file (if it exists)
def readTheta (thetaFile):
    theta0 = 0
    theta1 = 0
    dataFile = ""
    if os.path.isfile(thetaFile):
        with open(thetaFile, newline='') as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                if row[0] == 'dataFile':
                    dataFile = row[1]
                if (row[0] == 'theta0'):
                    try:
                        theta0 = float(row[1])
                    except ValueError:
                        print(filename, "is invalid.")
                        sys.exit()
                if (row[0] == 'theta1'):
                    try:
                        theta1 = float(row[1])
                    except ValueError:
                        print(filename, "is invalid.")
                        sys.exit()
    return theta0, theta1, dataFile

# Reading data CSV for x and y values
def readData (dataFile):
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


##########################################################################
##################                  MAIN                  ################
##########################################################################


# Theta file
thetaFile = './theta.csv'

# Check if theta file exists
if not os.path.isfile(thetaFile):
    print("Error : ", thetaFile, " doesn't exist")
    sys.exit()

# Get data
theta0, theta1, dataFile = readTheta(thetaFile)

# Read CSV data
if os.path.isfile(dataFile) and dataFile.endswith(".csv"):
    x, y = readData(dataFile)
    print("Computing error...")
elif os.path.isfile(dataFile):
    print("Error : data file must be a .csv")
    sys.exit()
else:
    print("Error : no data available at", dataFile)
    sys.exit()

# Calculate precision
error = computePrecision(x, y, theta0, theta1)

# Output precision
print("Precision is", 100 - round(error * 100, 2), "% (average error is", round(error * 100, 2), "%")