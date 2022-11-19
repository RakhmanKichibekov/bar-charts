import numpy as np
import matplotlib.pyplot as plt


def diagram(array, max, k):
    index = np.arange(2)
    bw = 0.4
    for i in range(2, k):
        bw = bw * 1 / 1.27
    plt.axis([-0.05, 2, 0, max + 1])
    plt.title('Столбиковые диаграммы', fontsize=20)
    for i in range(0, k):
        values = [int(array[i][0]), int(array[i][2])]
        plt.bar(index + i * bw, values, bw)

    plt.xticks(index + 1.4 * (k/3)* bw, ['A', 'B'])
    plt.show()


Fin = open("1.txt")
s = Fin.readlines()
count = len(s)
a = []
array = []
for i in range(count):
    a.append([""] * 1)
for i in range(len(s)):
    a[i] = s[i].split(" ")
for i in range(0, count):
    array.append(s[i])

k = 6  # Количество столбцов
s = []
for i in range(0, k):
    s.append(int(array[i][0]))
    s.append(int(array[i][2]))
max = 0
for i in range(0, len(s)):
    if (s[i] > max):
        max = s[i]

diagram(array, max, k)
