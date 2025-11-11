import numpy as np


x = np.random.choice([3, 5, 4, 9], p=[0.3, 0.3, 0.4, 0.0], size = [100])
y = np.random.choice([3, 5, 4, 9], p=[0.1, 0.3, 0.6, 0.0], size = (3,5))

print(x)
print(y)