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

# Вычисляем эмпирическую функцию распределения (ЭФР)
sorted_data = np.sort(data)
empirical_cdf = np.arange(1, len(sorted_data) + 1) / len(sorted_data)

# Оцениваем параметры нормального распределения
std = np.std(data)
average = np.mean(data)

# Вычисляем теоретическую функцию распределения для нормального распределения
theoretical_cdf = norm.cdf(sorted_data, average, std)

# Вычисляем максимальное расхождение
max_deviation = np.max(np.abs(empirical_cdf - theoretical_cdf))
print(f'Максимальное расхождение между эмпирической и гипотетической функциями распределения: {max_deviation}')

# Строим график
plt.step(sorted_data, empirical_cdf, label='Эмпирическая ф.р.', where='post')
plt.plot(sorted_data, theoretical_cdf, label='Гипотетическая ф.р.')
plt.legend()
plt.xlabel('x')
plt.ylabel('Fn')
plt.title('График эмпирической ф.р., совмещенный с графиком ф.р. гипотетического р.')
plt.show()
