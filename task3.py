import matplotlib.pyplot as plt
import numpy as np

f_start = np.genfromtxt('start.dat')
matrix = np.zeros([len(f_start), len(f_start)])
matrix[0][0] = 1
matrix[0][len(f_start) - 1] = -1

for i in range(1, len(f_start)):
    matrix[i][i] = 1
    matrix[i][i - 1] = -1

def changeGraph(f_start,matrix):
    return f_start - matrix.dot(f_start) / 2
plt.ion()

for i in range(255):
    f_start = changeGraph(f_start, matrix)

    plt.clf()
    plt.plot(f_start)

    plt.xlim(0, 50)
    plt.ylim(0, 10)

    plt.draw()
    plt.gcf().canvas.flush_events()

plt.ioff()
plt.show()


