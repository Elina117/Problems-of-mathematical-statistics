import pandas as pd
import numpy as np
import scipy.stats as stats

# Путь к файлу
excel_file_path = "/Users/elinagalimova/Downloads/ZadanMS208.xls"
# Название листа
sheet_name = "Sheet2"
# Название столбца
column_name = "Z11"
df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

data = df[column_name]
data = data.dropna()

mean = np.mean(data)
variance = np.var(data)
size = len(data)
std_error = np.std(data) / np.sqrt(len(data))

Q = 0.9
alpha = 1 - Q
degrees_of_freedom = size - 1
t_quantile = stats.t.ppf(1 - alpha, degrees_of_freedom)
upper_bound = mean + t_quantile * std_error


print(f"Выборочное среднее: {mean}")
print(f"Дисперсия: {variance}")
print(f"Объем выборки: {size}")
print(f"Стандартная ошибка среднего: {std_error}")

print(f"Верхняя граница 90%-го доверительного интервала для среднего всей совокупности: [{upper_bound}]")

