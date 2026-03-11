import matplotlib.pyplot as plt
x=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70]
y1=[10,20,30,40,50,60,70,80,90,100]
y2=[10,12,15,16,18,21,34,45,53,64]
plt.plot(x,y1,linestyle='dashed' ,marker='D')
plt.plot(x,y2,linestyle='dashed' ,marker='D')
plt.title('velocity-Time Graph')
plt.xlabel('Time(s)')
plt.ylabel('Velocity')
plt.xlim(5,25)
plt.ylim(10,100)
plt.ledgend()
plt.show()