import pandas as pd
import numpy as np
from scipy.stats import chi2
from scipy.stats import f

#Путь к файлу
excel_file_path = "/Users/elinagalimova/Downloads/ZadanMS208.xls"
#Название листа
sheet_name = "Sheet2"
#Название столбца
column_name_before = "Z10A"
column_name_after = "Z10B"

df_A = pd.read_excel(excel_file_path, sheet_name=sheet_name)
df_B = pd.read_excel(excel_file_path, sheet_name=sheet_name)

data_A = df_A[column_name_before]
data_A = data_A.dropna()

data_B = df_B[column_name_after]
data_B = data_B.dropna()

alpha = 0.1
x0 = 13
step = 2
num_of_intervals = 7

def size_data(data_A, data_B):
    size_a = len(data_A)
    size_b = len(data_B)
    return size_a, size_b


def intervals(num_of_intervals):
    broad_points = np.linspace(13, 27, num_of_intervals + 1, endpoint=True)  # делим на интервалы, включая последнюю точку
    interv = [(-np.inf, 13.0)] + [(broad_points[i], broad_points[i + 1]) for i in range(num_of_intervals)]  # границы
    return interv


#КОЛИЧЕСТВО ПОПАДАНИЙ В ИНТЕРВАЛЫ
def frequencies_A(data_A, intervals):
    vi = [0] * len(intervals)
    for i, interval in enumerate(intervals):
        for value in data_A:
            if interval[0] <= value <= interval[1]:
                vi[i] += 1
    return vi


def frequencies_B(data_B, intervals):
    vi = [0] * len(intervals)
    for i, interval in enumerate(intervals):
        for value in data_B:
            if interval[0] <= value <= interval[1]:
                vi[i] += 1
    return vi

#ОТНОСИТЕЛЬНЫЕ ЧАСТОТЫ
def otnosit_freq(vi_a, vi_b, size1, size2):
    vi_nA = [freq / size1 for freq in vi_a]
    vi_nB = [freq / size2 for freq in vi_b]
    total_sum_A = sum(vi_nA)
    total_sum_B = sum(vi_nB)
    vi_nA = [freq / total_sum_A for freq in vi_nA]
    vi_nB = [freq / total_sum_B for freq in vi_nB]
    return vi_nA, vi_nB


def stat_hi2(vi_nA, vi_nB, vi_a, vi_b, size1, size2):
    hi2 = []
    for i in range(num_of_intervals):
        vn = vi_a[i] + vi_b[i]
        if vn != 0:
            res_stat = size1 * size2 * (1 / vn) * (vi_nA[i] - vi_nB[i]) ** 2
            hi2.append(res_stat)
        else:
            hi2.append(0)  # Чтобы избежать деления на ноль
    return hi2


def critical_value(alpha, degrees_of_freedom):
    crit_value = 1 - chi2.cdf(16.104816391941387, degrees_of_freedom)
    return crit_value

degrees_of_freedom = num_of_intervals

def critical_region(alpha, degrees_of_freedom):
    crit_value = chi2.ppf(1 - alpha, degrees_of_freedom)
    critical_region = f"значения статистики хи-квадрат больше {crit_value}"
    return critical_region
def hypothesis(alpha_crit, alpha):
    if alpha_crit<=alpha:
        print("Гипотеза отвергается")
    else:
        print("Гипотеза принимается")

print(f" Интервалы: \t\t {intervals(num_of_intervals)}\n")
size1, size2 = size_data(data_A, data_B)
interv = intervals(num_of_intervals)
vi_a = frequencies_A(data_A, interv)
vi_b = frequencies_B(data_B, interv)
vi_nA, vi_nB = otnosit_freq(vi_a, vi_b, size1, size2)

print("Относительные частоты")
print(f"Группа А: {vi_nA}\n Сумма = {sum(vi_nA)}")
print(f"Группа B: {vi_nB}\n Сумма = {sum(vi_nB)}")
hi2 = stat_hi2(vi_nA, vi_nB, vi_a, vi_b, size1, size2)
print(f"Хи-квадрат: {hi2}\n Сумма = {sum(hi2)}")
print(f"Объем: группы А = {size1}, группы B = {size2}\n")

print(f"с критическим уровнем значимости: {critical_value(alpha, degrees_of_freedom)}")

print(f"10%-я критическая область : {critical_region(alpha, degrees_of_freedom)}")
hypothesis(critical_value(alpha, degrees_of_freedom), alpha)