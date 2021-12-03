import os
import csv
import sys

# Theta file
filename = './theta.csv'

# Init at 0
theta0 = 0
theta1 = 0

# Get theta values from file (if it exists)
if os.path.isfile(filename):
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
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


# Loop until user supplies mileage value
waiting_for_input = True
while (waiting_for_input):
    mileage = input("Type a mileage to see the estimated price : ")

    try:
        mileage = int(mileage)
        waiting_for_input = False
    except ValueError:
        print("Please enter an integer !\n")

# Output estimation based on theta values
print("\nBased on current predictions, a car with a mileage of", mileage, "kilometers would be worth :")
print("$", int(theta0 + (theta1 * mileage)))

if (theta0 == 0 and theta1 == 0):
    print("\n(Without a trained model, estimating won't get us far...)")