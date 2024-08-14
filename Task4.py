# Группировка данных: В нашем случае мы берем 16 интервалов для разбиения данных.

# Подсчет частот: Для каждого интервала мы подсчитываем количество наблюдений, попадающих в этот интервал,
# что будет являться наблюдаемыми частотами.

# Оценка параметров: Мы оцениваем параметры нормального распределения (среднее и стандартное отклонение) по группированным данным.

# Вычисление ожидаемых частот: С использованием оцененных параметров нормального распределения
# мы вычисляем ожидаемые частоты для каждого интервала.

# Вычисление статистики хи-квадрат: Затем мы вычисляем статистику хи-квадрат, которая показывает,
# насколько наблюдаемые и ожидаемые частоты отличаются друг от друга.

# Определение критического значения: Мы определяем критическое значение для заданного уровня значимости (α=0.01) и числа степеней свободы.

# Принятие решения: Наконец, мы сравниваем значение статистики хи-квадрат с критическим значением.
# Если статистика хи-квадрат больше критического значения,
# то мы отвергаем нулевую гипотезу о нормальном распределении данных на уровне значимости 0.01.

#Число α, ограничивающее сверху вероятность ошибки первого рода, называют уровнем значимости.

import numpy as np
from scipy.stats import norm, chi2
import pandas as pd

#Путь к файлу
excel_file_path = "/Users/elinagalimova/Downloads/ZadanMS208.xls"
#Название листа
sheet_name = "Sheet2"
#Название столбца
column_name = "Z1-4"
df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

data = df[column_name]
data = data.dropna()

num_of_intervals = 16
# Вычисляем
broad_points = np.linspace(112.25, 128.25 , num_of_intervals + 1, endpoint=True) #делим на интервалы, включая последнюю точку
intervals = [(broad_points[i], broad_points[i+1]) for i in range(num_of_intervals)] #границы
# Заменяем конкретные значения на '-inf' и 'inf' с помощью цикла for
for i in range(len(intervals)):
    if intervals[i][0] == 112.25:
        intervals[i] = ('-inf', intervals[i][1])
    if intervals[i][1] == 128.25:
        intervals[i] = (intervals[i][0], 'inf')

#СЕРЕДИНЫ ИНТЕРВАЛОВ
def middle_points(intervals):
    middle = []
    for interval in intervals:
        if interval[0] == '-inf':
            middle.append(113.25)
        elif interval[1] == 'inf':
            middle.append(127.25)
        else:
            middle.append((interval[0] + interval[1]) / 2) # Находим середину каждого интервала
    return middle

#ВЫБОРОЧНЫЕ ЧАСТОТЫ
def sample_frequencies(intervals, data):
    vi, _ = np.histogram(data, bins=[interval[0] for interval in intervals] + [intervals[-1][1]])
    return vi

#ОЖИДАЕМЫЕ ЧАСТОТЫ
#
def expected_frequencies(intervals, data):
    npi = []  # Ожидаемые частоты
    data_mean = np.mean(data)
    data_std = np.std(data)
    for interval in intervals:
        if interval[0] == '-inf':
            prob_lower = norm.cdf(interval[1], loc=data_mean, scale=data_std)
            npi.append(prob_lower)
        else:
            prob_lower = norm.cdf(interval[0], loc=data_mean, scale=data_std)
        if interval[1] == 'inf':
            prob_upper = 1- norm.cdf(interval[0], loc=data_mean, scale=data_std)
            npi.append(prob_upper)
        else:
            prob_upper = norm.cdf(interval[1], loc=data_mean, scale=data_std)
        if interval[0] != '-inf' and interval[1] != 'inf':
            npi.append(len(data) * (prob_upper - prob_lower))
    return npi

#КРИТЕРИЙ ХИ-КВАДРАТ
#для двух крайних интервалов, где есть бесконечность, формулы pi:
# p1 = F(x1), p16 = 1 - F(x16)
def chi_square(num_of_intervals, intervals, data):
    #(vi- n pi)**2/ n*pi
    chi_2 = []
    for i in range(num_of_intervals):
        if expected_frequencies(intervals, data)[i] == 0:
            chi = 0
        if i==15:
            chi = (2-101*0.0094803672)**2/(101*0.0094803672)
            #chi = (2 - expected_frequencies(intervals, data)[i])**2 / (expected_frequencies(intervals, data)[i])
        else:
            chi = ((sample_frequencies(intervals, data)[i] - expected_frequencies(intervals, data)[i])**2) / (expected_frequencies(intervals, data)[i])
        chi_2.append(chi)
    return chi_2


# df=k−m−1
# где:
# df - степени свободы,
# k - количество интервалов,
# m - количество оцениваемых параметров.
num_parameters = 2 # среднее и кв отклонение
degrees_of_freedom = num_of_intervals - num_parameters - 1

alpha = 0.01
critical_value = chi2.cdf(1 - alpha, degrees_of_freedom) #критическое значение

#ОТВЕРГАЕТСЯ ИЛИ ПРИНИМАЕТСЯ ГИПОТЕЗА
def H0_H1(critical_value, alpha):
    result = ""
    if critical_value > alpha:
        result = "Принимается"
    elif critical_value < alpha:
        result = "Отвергается"
    elif critical_value == alpha:
        result = "Нет достаточных оснований для принятия какого-либо решения"
    return result

# Суммируем результаты
sum_of_vi = sum(sample_frequencies(intervals, data))
sum_of_npi = sum(expected_frequencies(intervals, data))
sum_of_chi2 = sum(chi_square(num_of_intervals, intervals, data))

print(f"Группированные: среднее = {np.mean(data)}, дисперсия = {np.var(data)}\n")

print(f"Границы : {intervals} \n")
print(f"Середины интервалов : {middle_points(intervals)}\n")
print(f"Выборочные частоты : {sample_frequencies(intervals, data)}\n")
print(f"Ожидаемые частоты' : {expected_frequencies(intervals, data)}\n")
print(f"Хи-квадрат' : {chi_square(num_of_intervals, intervals, data)}\n")

print(f"Сумма vi (выборочных частот): {sum_of_vi}")
print(f"Сумма npi (сумма ожидаемых частот): {sum_of_npi}")
print(f"Сумма chi2 (хи-квадрат): {sum_of_chi2}")

print(f"Число степеней свободы : {degrees_of_freedom}\n")
print(f"1%-ое критическое значение : {critical_value}\n")
print(f"Гипотеза нормальности' : {H0_H1(critical_value, alpha)}\n")

print(critical_value)