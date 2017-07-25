# import numpy as np
# phy=np.array([15,12,8,8,7,7,7,6,5,3])
# his=np.array([10,25,17,11,13,17,20,13,9,15]).reshape((10,1))
# x=np.c_[np.ones((phy.size,1)),phy]
# theta=np.zeros((2,1))
# lambd=0.00001
# for i in range(1000):
#      theta=theta-(lambd/his.size)*np.sum((np.tile(np.dot(x,theta)-his,(1,2))*x),axis=0).reshape(2,1)
# print theta
import numpy as np
x=np.array([15,12,8,8,7,7,7,6,5,3])
y=np.array([10,25,17,11,13,17,20,13,9,15])
sx=np.sum(x)
sy=np.sum(y)
sxy=np.sum(x*y)
sx2=np.sum(x**2)
sy2=np.sum(y**2)
n=np.size(x)
r=round((sxy-(sx*sy)/n)/(np.sqrt(sx2-(sx)**2/n)*np.sqrt(sy2-(sy)**2/n)),3)
stdx=np.sqrt(sx2-(sx)**2/n)
stdy=np.sqrt(sy2-(sy)**2/n)
print stdy/stdx