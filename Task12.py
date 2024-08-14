import pandas as pd
import numpy as np
import scipy.stats as stats

# Путь к файлу
excel_file_path = "/Users/elinagalimova/Downloads/ZadanMS208.xls"
# Название листа
sheet_name = "Sheet2"
# Название столбца
column_name = "Z12"
df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

data = df[column_name]
data = data.dropna()

size = len(data)
variance = np.var(data)

Q = 0.95
alpha = 1 - Q


# Вычисляем нижнюю и верхнюю границы доверительного интервала
upper_bound = (size * variance) / stats.chi2.ppf(alpha/2, df=size-1)
lower_bound = (size * variance) / stats.chi2.ppf(1 - alpha/2, df=size-1)

print(f"Объем выборки: {size}")
print(f"Дисперсия: {variance}")
print(f"95%-ая Двусторонняя для дисперсии: {lower_bound}, {upper_bound}")