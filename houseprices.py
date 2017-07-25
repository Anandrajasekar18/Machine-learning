import numpy as np
n,m=map(int,raw_input().split())
lit=[]
for i in range(m):
    lit.append(map(float,(raw_input().split())))
X=np.array(lit)
x=np.c_[np.ones((m,1)),X[:,0:n]]
y=X[:,n].reshape(m,1)
theta=np.zeros((n+1,1))

lambd=0.3
for i in range(400):
     theta=theta-lambd/m*np.sum((np.tile(np.dot(x,theta)-y,(1,n+1))*x),axis=0).reshape(n+1,1)
T=int(raw_input())
for i in range(T):
    print ("%.2f" %np.dot((np.array(map(float,("1"+" " +raw_input()).split()))).reshape(1,n+1),theta))
