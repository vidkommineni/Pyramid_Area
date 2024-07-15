from math import *


# Enter the side length in meters: 1
# Enter the number of layers: 5
# You need 55.83 m^2 of gold foil to cover the pyramid

# assign variables
length = float(input('Enter the side length in meters: '))
layers = int(input('Enter the number of layers: '))

topArea = ((sqrt(3)/4) * (length * layers) ** 2)  # total top area will be same base

sidesArea = (layers * (layers + 1) / 2) * length * length * 3  # sum of all the layers * length^2 * 3 sides
totalArea = sidesArea + topArea

print(f'You need {totalArea: .2f} m^2 of gold foil to cover the pyramid')
