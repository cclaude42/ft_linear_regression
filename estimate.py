#!/usr/bin/env python3
import os
import csv
import sys
import matplotlib.pyplot as plt


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
    if not os.path.isfile(dataFile):
        print("Error : data file doesn't exist")
        sys.exit()
    with open(dataFile, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            try:
                x.append(int(row[0]))
                y.append(int(row[1]))
            except ValueError:
                pass
    return x, y

# Loop until user supplies mileage value
def getMileage ():
    waiting_for_input = True
    while (waiting_for_input):
        mileage = input("Type a mileage to see the estimated price : ")
        try:
            mileage = int(mileage)
            waiting_for_input = False
        except ValueError:
            print("Please enter an integer !\n")
        return mileage

def displayEstimate (x, y, theta0, theta1, mileage):
    price = theta0 + (theta1 * mileage)
    plt.title('Relationship between a car mileage and its price', fontdict = {'family':'serif','color':'black','size':16})
    plt.xlabel('Mileage in km', fontdict = {'family':'serif','color':'green','size':13})
    plt.ylabel('Price in $', fontdict = {'family':'serif','color':'green','size':13})
    plt.plot([min(x), max(x)], [theta0 + theta1 * min(x), theta0 + theta1 * max(x)], color='C1', label="f(x) = {0}*x + {1}".format(round(theta1, 2), round(theta0, 2)))
    plt.plot(x, y, 'o', color='C0')
    plt.stem([mileage], [price], bottom=(theta0 + theta1 * max(x)), orientation='vertical', linefmt='--C2', markerfmt='oC2')
    plt.stem([price], [mileage], bottom=min(x), orientation='horizontal', linefmt='--C2', markerfmt='oC2')
    plt.legend()
    plt.show()

##########################################################################
##################                  MAIN                  ################
##########################################################################

# Theta file
thetaFile = './theta.csv'

# Get data
theta0, theta1, dataFile = readTheta(thetaFile)
mileage = getMileage()

# Output estimation based on theta values
print("\nBased on current predictions, a car with a mileage of", mileage, "kilometers would be worth :")
print("$", int(theta0 + (theta1 * mileage)))

if (theta0 == 0 and theta1 == 0):
    print("\n(Without a trained model, estimating won't get us far...)")

if len(sys.argv) == 2 and sys.argv[1] == '--visualize': 
    x, y = readData(dataFile)
    displayEstimate(x, y, theta0, theta1, mileage)