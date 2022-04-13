# --------------------增加点数-------------------- #
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 增加点数
rw = RandomWalk(50_000)
rw.fill_walk()

plt.style.use('seaborn-dark')
fig, ax = plt.subplots()
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers,
	cmap=plt.cm.Blues, edgecolors='none', s=1)


# 隐藏坐标轴
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False) 


# 突出起点和终点
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
	 edgecolors='none', s=100)

plt.show()