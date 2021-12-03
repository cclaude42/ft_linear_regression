#!/usr/bin/env python3
import os
import csv
import sys
import matplotlib.pyplot as plt

# Goal function
def estimatePrice (theta0, theta1, mileage):
    return theta0 + (theta1 * mileage)

# Theta0 formula : sum of errors
def meanError0 (x, y, theta0, theta1):
    m = len(x)
    adjustedSum = 0
    for i in range(m):
        adjustedSum += (estimatePrice(theta0, theta1, x[i]) - y[i])
    return adjustedSum / m

# Theta1 formula : sum of errors multiplied by x
def meanError1 (x, y, theta0, theta1):
    m = len(x)
    adjustedSum = 0
    for i in range(m):
        adjustedSum += (estimatePrice(theta0, theta1, x[i]) - y[i]) * x[i]
    return adjustedSum / m

# Iterating towards local minimum
def gradientDescent (x, y):
    theta0 = 0
    theta1 = 0
    for i in range(nIterations):
        tmpTheta0 = theta0 - learningRate * meanError0(x, y, theta0, theta1)
        tmpTheta1 = theta1 - learningRate * meanError1(x, y, theta0, theta1)
        theta0 = tmpTheta0
        theta1 = tmpTheta1
    return theta0, theta1

# Normalization (all values between 0 and 1) for calculations
def normalize (lst):
    normalized = []
    for elem in lst:
        normalized.append( (elem - min(lst)) / (max(lst) - min(lst)) )
    return normalized

# Reading data CSV for x and y values
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

# Saving theta values for estimate.py to use
def writeData (theta0, theta1):
    with open(thetaFile, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow(['theta0', theta0])
        spamwriter.writerow(['theta1', theta1])


##########################################################################
##################                  MAIN                  ################
##########################################################################


dataFile = input("Input file to save data to :")

# Check if file exists
if os.path.isfile(dataFile):
    print("Error : file already exists")
    sys.exit()

# Check if file will be CSV
if not s.endswith(".csv"):
    print("Error : file must be a .csv")
    sys.exit()

# # Normalize vectors
# normedX = normalize(x)
# normedY = normalize(y)

# # Perform the gradient descent
# theta0, theta1 = gradientDescent(normedX, normedY)

# # Denormalize theta values
# theta0 = theta0 * (max(y) - min(y)) + min(y)
# theta1 = theta1 * (max(y) - min(y)) / (max(x) - min(x))

# # Save theta values
# writeData(theta0, theta1)
# print("Done training !")
# print("Data saved at ", thetaFile)

# # Display results
# plt.title('Relationship between a car mileage and its price', fontdict = {'family':'serif','color':'black','size':16})
# plt.xlabel('Mileage in km', fontdict = {'family':'serif','color':'green','size':13})
# plt.ylabel('Price in $', fontdict = {'family':'serif','color':'green','size':13})
# plt.plot(x, y, 'o')
# plt.plot([min(x), max(x)], [theta0 + theta1 * min(x), theta0 + theta1 * max(x)])
# plt.show()

# for i in range(10):
#     plt.plot(i * 10000, i * 1000, 'x')
#     plt.pause(0.01)
#     s = input()
#     plt.clf()