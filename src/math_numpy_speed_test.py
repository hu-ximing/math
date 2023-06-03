import math
import numpy as np
import time

# math

result = 0
start_time = time.time()

for i in range(1000000):
    result += math.sqrt(i) * math.cos(i**math.pi) * math.asin(1 / (i + 1))

print("--- %s seconds ---" % (time.time() - start_time))
print(result)

# numpy

result = 0
start_time = time.time()

for i in range(1000000):
    result += np.sqrt(i) * np.cos(i**np.pi) * np.arcsin(1 / (i + 1))

print("--- %s seconds ---" % (time.time() - start_time))
print(result)
