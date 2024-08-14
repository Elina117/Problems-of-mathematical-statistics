import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm

# Путь к файлу
excel_file_path = "/Users/elinagalimova/Downloads/ZadanMS208.xls"
# Название листа
sheet_name = "Sheet2"
# Название столбца
column_name = "Z1-4"
df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

data = df[column_name]
data = data.dropna()

xO = 113.25  # правая граница первого интервала
delta = 1  # ширина интервалов
r = 16  # общее число интервалов с учетом двух крайних
H0 = "Нормальное"

# Построение гистограммы
plt.hist(data, bins=int(14/1), density=True, alpha=0.4, color='blue', label='Выборочные данные')

average = np.mean(data)
std = np.std(data)

# Генерация значений для функции плотности нормального распределения
xmin = 113.25
xmax = 130.25
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, average, std)

# Построение графика функции плотности
plt.plot(x, p, 'r', linewidth=2, label='Плотность нормального распределения')

# Оценка моды
mode = data.mode().values[0] #Извлечение значения моды из DataFrame с использованием .values[0] выполняется для получения фактического значения моды, а не представления в виде DataFrame.
plt.axvline(mode, color='b', linestyle='dashed', linewidth=2, label='Оценка моды')

print(f"Мода распределения = {mode}")

plt.xlabel('Значения')
plt.ylabel('Плотность вероятности')
plt.title('График гистограммы и подогнанной нормальной ф. плотности')
plt.legend()
plt.show()