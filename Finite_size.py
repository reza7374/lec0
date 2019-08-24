import numpy as np
import matplotlib.pyplot as plt
w_p = np.loadtxt('/home/reza/Downloads/data1.txt') # w_p by size and probability
P_inf= np.loadtxt('/home/reza/Downloads/datap.txt')
p=w_p[:,0]
# plt.plot(p,w_p[:,1:])
# plt.show()
p_c=0.593 #  by plot
L=[16,32,64,128]
k=np.zeros(4)
s=np.size(p)
pp=np.zeros((s,4))
pl=np.zeros((s,4))
for i in range(1,5):
    j=0
    while(j<s):
        if w_p[j,i]>=0.285 and w_p[j,i]<=0.315:
            k[i-1]=w_p[j,0]
            break
        j+=1
k-=p_c
k=abs(k)
# plt.loglog(L,k)
# plt.show()
G=np.polyfit(np.log(L),np.log(k),1)
# print(G)
# [-0.74834851 -1.2036094 ] result of G
for j in range(4):
        pp[:,j]=(p-p_c)*((L[j])**(-G[1]))
plt.plot(pp,w_p[:,1:])
plt.show()
plt.plot(P_inf[:,0],P_inf[:,1:])
plt.show()
for j in range(4):
        pl[:,j]=(P_inf[:,0]-p_c)*((L[j])**(-G[1]))
plt.plot(pl,P_inf[:,1:])
plt.show()
