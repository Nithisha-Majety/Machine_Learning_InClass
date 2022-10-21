import numpy as n
#Q1 Random numbers array
a=n.random.randint(1,20,15)
print(a)
#Q2 Reshaping the array
a1=a.reshape(3,5)
print(a1.shape)
print(a1)
#Q3 Finding max value in each row and replacing with 0
m=n.amax(a1,axis=1)
m=m[:,None]
a2=n.where(a1==m,0,a1)
print(a2)