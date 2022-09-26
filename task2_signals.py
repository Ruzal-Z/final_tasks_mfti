import matplotlib.pyplot as plt
import numpy as np

def fun_signal(f):
    arr = np.array(f)
    plt.plot(arr)

    arr1 = np.zeros(len(arr))
    for i in range(len(arr)):
        if i < 10:
            arr1[i] = sum(arr[0: i + 1]) / (i + 1)
        else:
            arr1[i] = sum(arr[i - 9: i + 1]) / 10

    plt.plot(arr1)
    plt.show()
#создаем массивы из данных файлов, в данном случае по очереди будут открываться графики.
fun_signal(f = np.loadtxt('signals/signal01.dat', float))
fun_signal(f = np.loadtxt('signals/signal02.dat', float))
fun_signal(f = np.loadtxt('signals/signal03.dat', float))

