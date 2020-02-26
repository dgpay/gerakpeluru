import math
import matplotlib.pyplot as plt
#Gerak Peluru Tanpa dan memikirkan Hambatan Udata(D)

g=9.806
ax=0
ay=-g
m=150
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
#NUMERIK TANPA HAMBATAN UDARA
i=0.01
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
    i=i+0.01

#ANALITIK PEMBVADING
t=0.01
x0=0
y0=0
analitik1x.append(x0)
analitik1y.append(y0)

while(t<=T):
    x=round(vx,2)*t
    y=(round(vy,2)*t)+(0.5*ay*(t**2))
    
    analitik1x.append(round(x,2))
    analitik1y.append(round(y,2))
    t=t+0.01
#NUMERIK DENGAN HAMBATAN UDARA
v=math.sqrt(vx**2+vy**2)
ax=-(D/m)*v*vx
ay=-g-(D/m)*v*vy

i=0.01
x=0
y=0
numerik2x.append(x)
numerik2y.append(y)
vxt=vx
vyt=vy
while(i<=T):
    vxt=vxt+(ax*dt)
    vyt=vyt+(ay*dt)
    x=x+(vxt*dt)
    y=y+(vyt*dt)
    numerik2x.append(round(x,2))
    numerik2y.append(round(y,2))
    i=i+0.01



plt.plot(numerik1x,numerik1y,'r')
plt.plot(numerik2x,numerik2y,'b')
plt.plot(analitik1x,analitik1y,'y')

plt.show()