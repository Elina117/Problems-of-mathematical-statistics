import pandas as pd
from scipy import stats
import numpy as np
from scipy.stats import ttest_ind

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
data_X = data_X.dropna()

data_Y = df_B[column_name_after]
data_Y = data_Y.dropna()

n = len(data_Y)
df = n-2
alpha = 0.025
def avarage_value(data_X, data_Y):
    average_X = np.mean(data_X)
    average_Y = np.mean(data_Y)
    return average_X, average_Y

def variance_value(data_X, data_Y):
    variance_X = np.var(data_X)
    variance_Y = np.var(data_Y)
    return variance_X, variance_Y

def size_value(data_X, data_Y):
    size_X = len(data_X)
    size_Y = len(data_Y)
    return size_X, size_Y
def correlation_coefficient(data_X, data_Y):
    correlation = np.corrcoef(data_X, data_Y)[0, 1]
    return correlation

def correlation_coefficient_viboroch(data_X, data_Y):
    n = len(data_X)
    variance_X = np.var(data_X)
    variance_Y = np.var(data_Y)
    average_X = np.mean(data_X)
    average_Y = np.mean(data_Y)
    sum = 0
    for i in range(1, n):
        sum += (data_X[i] - average_X)*(data_Y[i] - average_Y)
    r = ((1/n)*sum)/(np.sqrt(variance_X) * np.sqrt(variance_Y))
    return r

def preobr_student(r, df):
    t = (r * np.sqrt(df))/(np.sqrt(1 - r*r))
    return t

def critical_region(df, alpha):
    t_critical = stats.t.ppf(1 - alpha, df)
    return t_critical

def student_stats(t, df):
    t_statistic = stats.t.cdf(t, df)
    return t_statistic

def alpha_crit(stud_stat):
    alpha_cr = 2*(1 - stud_stat)
    return alpha_cr

def hypothesis(alpha_crit, alpha):
    if alpha_crit<=alpha:
        print("Гипотеза независимости отвергается")
    else:
        print("Гипотеза независимости принимается")


print(f"Среднее {avarage_value(data_X, data_Y)}")
print(f"Дисперсия:  {variance_value(data_X, data_Y)}")
print(f"Объем выборки {size_value(data_X, data_Y)}")
print(f"Коэффициент корреляции,r  {correlation_coefficient(data_X, data_Y)}")
r = correlation_coefficient_viboroch(data_X, data_Y)
t = preobr_student(r, df)
stud_stat = student_stats(t, df)
alpha_crit = alpha_crit(stud_stat)
print(f"Преобразование Стьюдента {t}")
print(f"2.5%-я критическая область {critical_region(df, alpha)}")
hypothesis(alpha_crit, alpha)
print(f"С критическим уровнем значимости {alpha_crit}")
r_cor = correlation_coefficient_viboroch(data_X, data_Y)


