import math
import matplotlib.pyplot as plt
import numpy as np
#Gerak Peluru Tanpa memikirkan Hambatan Udata(D)

g=9.806
ax=0
ay=-g
m=0.15
v0=50
deg=35
D=0.0013
dt=0.01
pi=3.14

theta = deg*pi/180

#test waktu
T=2*v0*math.sin(theta)/(g)
N=T/dt
det=T/(N-1)
print(round(T,2))
print(round(N,2))
print(det)

vy = v0*math.sin(theta) #vy(1)
vx = v0*math.cos(theta) #konstant
print('vy',vy)
print('vx',vx)

numerik1x=[]
numerik1y=[]
numerik2x=[]
numerik2y=[]
analitik1x=[]
analitik1y=[]
analitik2x=[]
analitik2y=[]
#NUMERIK TANPA HAMBATAN UDARA
i=dt
x=0
y=0
numerik1x.append(x)
numerik1y.append(y)
vxt=vx
vyt=vy
while(i<=T):
    vxt=vxt+(ax*dt)
    vyt=vyt+(ay*dt)
    x=x+(vxt*dt)
    y=y+(vyt*dt)
    numerik1x.append(round(x,2))
    numerik1y.append(round(y,2))
    i=i+dt
print('total waktu numerik tanpa hambatan',i)
#ANALITIK PEMBVADING TANPA HAMBATAN UDARA
t=dt
x0=0
y0=0
analitik1x.append(x0)
analitik1y.append(y0)

while(t<=T):
    x=x0+(round(vx,2)*t)+(0.5*ax*(t**2)) #bisa rubah jadi x0*round(vx,2)*t
    y=y0+(round(vy,2)*t)+(0.5*ay*(t**2))
    
    analitik1x.append(round(x,2))
    analitik1y.append(round(y,2))
    t=t+dt
print('total waktu analitik tanpa hambatan',t)
#NUMERIK DENGAN HAMBATAN UDARA
g=9.806


i=dt
x=0
y=0

numerik2x.append(x)
numerik2y.append(y)
v = math.sqrt((np.power(vx,2)+np.power(vy,2)))
ax2 = -(D/m)*v*vx
ay2 = -g-(D/m)*v*vy
while (i<=T) :

    vy = vy + (ay2 * dt)
    vx = vx + (ax2 * dt)
    y = y + (vy * dt)
    x = x + (vx * dt)
    numerik2x.append(x)
    numerik2y.append(y)
    if(y<0):        #kenapa gak pake waktu jadi if(i>=5.89):
        break       #                                break
    else:           #Karena nanti pada detik ke 4.50 keatas y nya sudah minus sehingga 
        i=i+dt      #grafik tidak berakhir di y=0 jadi anggep ajah si peluru berhenti ditanah itu pada (y=0)
print('total waktu numerik hambatan',i)

#ANALITIK PEMBVADING DENGAN HAMBATAN UDARA
vy = v0*math.sin(theta) #vy(1)
vx = v0*math.cos(theta) #konstant
t=dt
x0=0
y0=0
analitik2x.append(x0)
analitik2y.append(y0)

while(t<=T):
    v = math.sqrt((np.power(vx,2)+np.power(vy,2)))
    ax = -(D/m)*v*vx
    ay = -g-(D/m)*v*vy
    x=x0+(round(vx,2)*t)+(0.5*ax*(t**2)) #bisa rubah jadi x0*round(vx,2)*t
    y=y0+(round(vy,2)*t)+(0.5*ay*(t**2))
    
    analitik2x.append(round(x,2))
    analitik2y.append(round(y,2))
    if(y<0):
        break
    else:
        t=t+dt
print('total waktu analitik hambatan',t)

#print(numerik1x)
#print(numerik1y)
#print(analitik1x)
#print(analitik1y)
#print(numerik2x)
#print(numerik2y)
plt.plot(numerik1x,numerik1y,'r')
plt.plot(numerik2x,numerik2y,'b')
plt.plot(analitik1x,analitik1y,'g')
plt.plot(analitik2x,analitik2y,'black')
plt.show()