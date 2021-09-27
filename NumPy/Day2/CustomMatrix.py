import numpy as np

a=np.ones((3,3))

a[2,:]=np.zeros((1,3))
a[1,1]=9
print(a)