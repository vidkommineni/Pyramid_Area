from math import *

# Enter the side length in meters: 1
# Enter the number of layers: 5
# You need 55.83 m^2 of gold foil to cover the pyramid


length = float(input('Enter the side length in meters: '))
layers = int(input('Enter the number of layers: '))
sidesArea = 0
topArea = 0
totalArea = 0

for i in range(layers):
    sidesArea = layers * length * length * 3
    topArea = ((sqrt(3)/4) * (length * layers) ** 2) - ((sqrt(3)/4) * (length * (layers-1)) ** 2)
    totalArea += sidesArea + topArea
    layers -= 1

print(f'You need {totalArea:.2f} m^2 of gold foil to cover the pyramid')


