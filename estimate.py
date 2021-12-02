import os
import csv

filename = './theta.csv'

theta0 = 0
theta1 = 0

if os.path.isfile(filename):
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            if (row[0] == 'theta0'):
                theta0 = int(row[1])
            if (row[0] == 'theta1'):
                theta1 = int(row[1])

waiting_for_input = True

while (waiting_for_input):
    mileage = input("Type a mileage to see the estimate price : ")

    try:
        mileage = int(mileage)
        waiting_for_input = False
    except ValueError:
        print("Please enter an integer !\n")

print(theta0 + (theta1 * mileage))