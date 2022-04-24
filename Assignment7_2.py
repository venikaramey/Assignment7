import numpy as np

def movingAverage(inputValue, k):
  z = 1
  output = np.convolve(inputValue, np.ones(k), 'valid') / k
  for i in output:
    print("y{0} = {1:.2f}".format(z, i))
    z += 1

inputValue = np.array([3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150])
k = 3
movingAverage(inputValue, k)