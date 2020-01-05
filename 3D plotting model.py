from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.patches 
import numpy as np
import pandas as pd
import seaborn as sns


#Measurement 2
# data = pd.read_excel("Data.xlsx","Measurement 2")
# X2 = data['X2'].values.tolist()
# Y2 = data['Y2'].values.tolist()
# Z2 = data['Z2'].values.tolist()



# fig = plt.figure()
# ax = fig.add_subplot(111,projection = '3d')

# ax.scatter(0, 0, 0, s=50, c = 'green', label='origin')

# ax.scatter(X2, Y2, Z2, c='r', marker='o')
# plt.plot(X2, Y2, Z2,lw='4')
# axes = plt.gca()
# axes.set_xlim([0,700])
# axes.set_ylim([-350,350])
# axes.set_zlim([-350,350])


# ax.set_xlabel('x-axis')
# ax.set_ylabel('y-axis')
# ax.set_zlabel('z-axis')
# plt.legend(loc='best')
# plt.show()
#####################################################

#Measurement 3
# data = pd.read_excel("Data.xlsx","Measurement 3")
# X3_1 = data['X3_1'].values.tolist()
# Y3_1 = data['Y3_1'].values.tolist()
# Z3_1 = data['Z3_1'].values.tolist()

# X3_2 = data['X3_2'].values.tolist()
# Y3_2 = data['Y3_2'].values.tolist()
# Z3_2 = data['Z3_2'].values.tolist()


# fig = plt.figure()
# ax = fig.add_subplot(111,projection = '3d')


# ax.scatter(0, 0, 0, s=50, c = 'green', label='origin')


# ax.scatter(X3_1, Y3_1, Z3_1, c='r', marker='o', label='Bending to top')
# plt.plot(X3_1, Y3_1, Z3_1,lw='2',c='k')


# ax.scatter(X3_2, Y3_2, Z3_2, c='b', marker='v',label='Bend to  right')
# plt.plot(X3_2, Y3_2, Z3_2,lw='2',c='k')

# axes = plt.gca()
# axes.set_xlim([-250,150])
# axes.set_ylim([-250,50])
# axes.set_zlim([-50,250])


# ax.set_xlabel('x-axis')
# ax.set_ylabel('y-axis')
# ax.set_zlabel('z-axis')
# plt.legend(loc='best')
# plt.show()
#####################################################

# Measurement 4
# to simulate the graph using fusion 360. I want a function that 
#input the tangent angle of the tips and reture the radius of the circle
# def getRadius(alpha):
# 	A = np.array(alpha)
# 	return 38961.1301/A

# alpha = [360.0, 180, 90, 60, 45, 30, 0, -30, -62.3]
# print(getRadius(alpha))
#####################################################

# Measurement 5
# data = pd.read_excel("Data.xlsx","Measurement 5")
# X5 = data['RealForce'].values.tolist()
# Y5 = data['Degree'].values.tolist()

# plt.scatter(X5,Y5)

# sns.set_style('white')
# sns.set_style('ticks')
# sns.regplot(X5, Y5)
# plt.scatter(0.5,50, c= 'white', label='--- : Y = 51.73490X-83.47973')

# plt.title('Measurement 5')
# plt.xlabel('Force Applied (N)')
# plt.ylabel('Tangent Angle of the Tip (degree)')
# plt.legend(loc='best')
# plt.show()

#####################################################

#Measurement 6

#print(np.cos(np.deg2rad(60)))

data = pd.read_excel("Data.xlsx","Measurement 6")
X6 = data['X6'].values.tolist()
Y6 = data['Y6'].values.tolist()
Z6 = data['Z6'].values.tolist()

fig = plt.figure()
ax = fig.add_subplot(111,projection = '3d')
ax = Axes3D(fig)
ax.scatter(0, 0, 0, s=50, c = 'green', label='origin')
plt.plot([-154.4935, 680.3744], [0,0], [0,0] , c = 'green', label='backbone')
ax.scatter(X6, Y6, Z6, c='r', marker='o')

#total point
X = []
Y = []
Z = []

for i in range(0,len(X6),1):
	a = 0 #zero angle
	#each measurement
	x = []
	y = []
	z = []
	for j in range (0,25,1): #15degree * 24 = 360degree
		x += [X6[i]]
		y += [Y6[i]*(np.cos(np.deg2rad(j*15)))]
		z += [Y6[i]*(np.sin(np.deg2rad(j*15)))]
		X += [X6[i]]
		Y += [Y6[i]*(np.cos(np.deg2rad(j*15)))]
		Z += [Y6[i]*(np.sin(np.deg2rad(j*15)))]
	ax.scatter(x, y, z, marker='o')

# ax.plot_suface(X, Y, Z, rstride = 4, cstride = 4, color='b')
# Y,Z = np.meshgrid(Y,Z)
# ax.plot_surface(X, Y, Z, rstride = 5, cstride = 5, cmap = plt.get_cmap('rainbow'))


axes = plt.gca()
axes.set_xlim([-170,700])
axes.set_ylim([-500,500])
axes.set_zlim([-500,500])


ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.set_zlabel('z-axis')
plt.legend(loc='best')
plt.show()
#####################################################

#Measurement 7

# data = pd.read_excel("Data.xlsx","Measurement 7")
# X7 = data['X7'].values.tolist()
# Y7 = data['Y7'].values.tolist()
# Z7 = data['Z7'].values.tolist()



# fig = plt.figure()
# ax = fig.add_subplot(111,projection = '3d')

# ax.scatter(0, 0, 0, s=50, c = 'green', label='origin')

# ax.scatter(X7, Y7, Z7, c='r', marker='o')
# plt.plot(X7, Y7, Z7,lw='4')
# axes = plt.gca()
# axes.set_xlim([0,700])
# axes.set_ylim([-100,100])
# axes.set_zlim([-100,100])
# ax.set_xlabel('x-axis')
# ax.set_ylabel('y-axis')
# ax.set_zlabel('z-axis')
# plt.legend(loc='best')
# plt.show()
#####################################################

#Measurement 8
# data = pd.read_excel("Data.xlsx","Measurement 8")
# X8 = data['Weight'].values.tolist()
# Y8 = data['RealForce'].values.tolist()

# plt.scatter(X8,Y8)

# sns.set_style('white')
# sns.set_style('ticks')
# sns.regplot(X8, Y8)
# plt.scatter(0.5,5, c= 'white', label='--- : Y = 1.19620X+2.56683')

# plt.title('Measurement 8')
# plt.xlabel('Force Required to Reach Level(N)')
# plt.ylabel('Loading Weight at the tips (g)')
# plt.legend(loc='best')
# plt.show()