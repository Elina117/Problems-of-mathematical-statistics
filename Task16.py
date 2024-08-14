import pandas as pd
import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt

#Путь к файлу
excel_file_path = "/Users/elinagalimova/Downloads/ZadanMS208.xls"
#Название листа
sheet_name = "Sheet2"
#Название столбца
column_name_before = "Z14,15,16_x"
column_name_after = "Z14,15,16_y"

df_A = pd.read_excel(excel_file_path, sheet_name=sheet_name)
df_B = pd.read_excel(excel_file_path, sheet_name=sheet_name)

data_X = df_A[column_name_before]
X_data = data_X.dropna()

data_Y = df_B[column_name_after]
Y_data = data_Y.dropna()

# Вычисление коэффициента корреляции
correlation = np.corrcoef(X_data, Y_data)[0, 1]
print("Коэффициент корреляции между прочностью и коэффициентом текучести:", correlation)

# Вычисление средних значений
mean_X = np.mean(X_data)
mean_Y = np.mean(Y_data)

# Вычисление стандартных отклонений
std_X = np.std(X_data)
std_Y = np.std(Y_data)

# Фиксированное значение переменной Y
Y_fixed = 81

# Вычисление соответствующего значения X по уравнению линии регрессии
X_fixed = mean_X + correlation * (std_X / std_Y) * (Y_fixed - mean_Y)

# Создание массива значений переменной Y для построения линии регрессии
Y_values = np.linspace(min(data_Y), max(data_Y), 100)
# Вычисление значений X для каждого значения Y
X_line_regression = mean_X + correlation * (std_X / std_Y) * (Y_values - mean_Y)

# Уравнение регрессии в указанном формате
regression_equation = f"X = {correlation:.3f}Y + {mean_X - correlation * (std_X / std_Y) * mean_Y:.3f}"

# Вывод уравнения регрессии
print("Уравнение регрессии для X при Y = 81:")
print(regression_equation)

# Вывод конкретного прогноза X при Y = 81
print(f"Прогноз X при Y = {Y_fixed}: {X_fixed:.3f}")

# Построение графика
plt.scatter(data_Y, data_X, color='blue', label='Данные')
plt.plot(Y_values, X_line_regression, color='red', label='Линия регрессии')
plt.plot(Y_fixed, X_fixed, 'ro', label=f'Прогноз X при Y={Y_fixed}')

plt.xlabel('Коэффициент текучести (Y)')
plt.ylabel('Прочность (X)')
plt.title('График линии регрессии')
plt.legend()
plt.grid(True)
plt.show()