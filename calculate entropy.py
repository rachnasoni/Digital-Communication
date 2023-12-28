#DC exp 5 entropy
import numpy as np
import math
p=[]
h=0
k=0
n=int(input("enter number of probabilities "))
for i in range(0,n):
  v=float(input("enter probability "))
  p.append(v)
print("probabilities=",p)
for j in p:
  Hk= j*math.log2(1/float(j))
  k=k+j
  h=h+Hk
  print(Hk)
if k==1:
  print("total entropy= ",h)
else:
  print("enter valid probabilities")
