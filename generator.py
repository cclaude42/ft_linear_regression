#!/usr/bin/env python3
import os
import csv
import sys
import matplotlib.pyplot as plt


# Ask for data
dataFile = input("Choose file to save data to : ")

# Check if file exists
if os.path.isfile(dataFile):
    print("Error : file already exists")
    sys.exit()

# Check if file will be CSV
if not dataFile.endswith(".csv"):
    print("Error : file must be a .csv")
    sys.exit()

# Init arrays
x = []
y = []

# Loop while user inputs coordinates
running = True
while running:
    # Get X and Y coordinates
    try:
        print("\nReady to enter new point !")
        x_input = int(input("Enter x value : "))
        y_input = int(input("Enter y value : "))
    except ValueError:
        print("Error : value is not an integer")
        sys.exit()
    # Add to coordinates
    x.append(x_input)
    y.append(y_input)
    # Display current point scatter
    plt.clf()
    plt.plot(x, y, 'o')
    plt.pause(0.01)
    # Prompt for end of input
    if input("\nAre you done ? If yes, type yes, otherwise hit Enter ") == "yes":
        running = False

# Write data to specified file
print("\nWriting data to", dataFile, "...")
with open(dataFile, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        for i in range(len(x)):
            spamwriter.writerow([x[i], y[i]])