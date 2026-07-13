import numpy as np
a=np.array([0,1,2,3,4,5])
a

mask=(a%2==0)
a[mask]=-1
print(a)

a=np.array([10,20,35,40,55])
print(np.sum(a))
print(np.mean(a))
print(np.min(a))
print(np.max(a))

np.all(a<30)

np.all(a<60)

np.any(a<30)

a=np.array([10,20,35,40,55])
b=np.where(a%2!=0,-1,1)
b

array([ 1,  1, -1,  1, -1])
a=np.array([100,210,50,140,155])
b=np.sort(a)
b

array([ 50, 100, 140, 155, 210])
a=np.array([100,210,50,140,155])
a.sort()
b=a.argsort()
a

array([ 50, 100, 140, 155, 210])
a=np.arange(1,13).reshape(4,3)
b=np.arange(2,14).reshape(4,3)
print(a, "\n", "\n", b)

a+b

a-b

import numpy as np
a=np.arange(1,13).reshape(4,3)
b=np.arange(2,14).reshape(4,3)
a*b

a=np.array([1,2,3,4,5])
a
np.arange(5)
a=np.ones(5)
a
