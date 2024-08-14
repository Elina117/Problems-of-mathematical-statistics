import pandas as pd
import numpy as np

#Путь к файлу
excel_file_path = "/Users/elinagalimova/Downloads/ZadanMS208.xls"
#Название листа
sheet_name = "Sheet2"
#Название столбца
column_name = "Z1-4"
df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

data = df[column_name]
data = data.dropna()

#Объем данных
def data_size(data):
    size = len(data)
    return size

#Среднее значение
def avarage_value(data):
    average = np.mean(data)
    return average

#Медиана
def median_value(data):
    median = np.median(data)
    return median

#Дисперсия - смещенная
def variance_value(data):
    variance = np.var(data)
    return variance

#Дисперсия - несмещенная
def variance_smesh(data):
    variance = (np.var(data)*data_size(data))/(data_size(data)-1)
    return variance

#Стандартное отклонение
def std_deviation(data):
    std = np.std(data)
    return std

#Минимальное значение
def min_value(data):
    min_v = min(data)
    return min_v

#Максимальное значение
def max_value(data):
    max_v = max(data)
    return max_v

#Размах выборки
def range_of_data(data):
    rng_data = np.ptp(data)
    return rng_data

#Ассиметрия
def skewness_value(data):
    skewness = np.mean((data - avarage_value(data)) ** 3) / (std_deviation(data) ** 3)
    return skewness

#Эксцесс
def kurtosis_value(data):
    kurtosis = np.mean((data - avarage_value(data)) ** 4) / (std_deviation(data) ** 4) - 3
    return kurtosis

print("Объем наблюдений:", data_size(data))
print("Среднее значение:", avarage_value(data))
print("Медиана:", median_value(data))
print("Дисперсия смещенная:", variance_value(data))
print("Дисперсия несмещенная:", variance_smesh(data))
print("Стандартное отклонение:", std_deviation(data))
print("Минимальное значение:", min_value(data))
print("Максимальное значение:", max_value(data))
print("Размах (широта) выборки:", range_of_data(data))
print("Асимметрия:", skewness_value(data))
print("Эксцесс:", kurtosis_value(data))
