import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import LinearLocator

file = open("PZ Mon_v_radial(1).dat", "r")
file = file.readlines()   #считывание файла и перевод в тип список
del file[0] #удаление шапки
k = len(file)       #нахождение количества строк в будущей матрице (подсчет строк в исходном файле)
for i in range(0,k):
    file[i] = file[i].rstrip("\n")
    file[i] = file[i].rstrip(" ")
dan = np.empty((k, 1), dtype=list)
for i in range(0, k):   #строки
    dan[i][0] = file[i]    #заполнение массива данными из строки, содержащей исходный файл
    dan[i][0] = dan[i][0].split(" ")
X = [] # здесь будет дата
Y = [] #здесь будут скорости
for i in range(0,k):
    X.append(float(dan[i][0][0]))
    Y.append(float(dan[i][0][1]))
plt.scatter(X,Y) #создание графика
plt.xlabel('MJD') #название оси Х
plt.ylabel('Vr') #название оси У
plt.title('Зависимость радиальной скорости от юлианской даты') #название графика подпись сверху над графиком
plt.show()