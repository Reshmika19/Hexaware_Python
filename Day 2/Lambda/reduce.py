# Scenario 4: Calculating volume using reduce() and lambda

from functools import reduce

dimensions = [2, 3, 5]  

volume = reduce(lambda x, y: x * y, dimensions)

print("Box dimensions:", dimensions)
print("Total Volume:", volume)
