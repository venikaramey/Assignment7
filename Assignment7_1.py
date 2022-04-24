import numpy as np
def alexTheoVander(iVector, n, increasing = False):
  if increasing:
    oMatrix = np.matrix([x**i for x in iVector for i in range(n)]).reshape(iVector.size, n)
  else:
    oMatrix = np.matrix([x**(n-i-1) for x in iVector for i in range(n)]).reshape(iVector.size, n)
  return oMatrix

iVector = np.array([1, 3, 5, 7, 9])
n = 5
oMtarix_asc = alexTheoVander(iVector, n, True)
print(oMtarix_asc)

oMtarix_desc = alexTheoVander(iVector, n, False)
print(oMtarix_desc)