import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import f

#Путь к файлу
excel_file_path = "/Users/elinagalimova/Downloads/ZadanMS208.xls"
#Название листа
sheet_name = "Sheet2"
#Название столбца
column_name_before = "Z9A"
column_name_after = "Z9B"

df_A = pd.read_excel(excel_file_path, sheet_name=sheet_name)
df_B = pd.read_excel(excel_file_path, sheet_name=sheet_name)

data_A = df_A[column_name_before]
data_A = data_A.dropna()

data_B = df_B[column_name_after]
data_B = data_B.dropna()

alpha = 0.01
def size_data(data_A, data_B):
    n1 = len(data_A)
    n2 = len(data_B)
    return n1, n2

def dispercia(data_A, data_B):
    disp1 = np.var(data_A)
    disp2 = np.var(data_B)
    return disp1, disp2

def statistic_Fishera(disp1, disp2):
    fisher = max(disp1, disp2)/min(disp1, disp2)
    return fisher

def critical_alpha(df1, df2, fisher):
    alpha_crit = 2 - stats.f.cdf(fisher, df1, df2) - stats.f.sf(fisher, df2, df1)
    return alpha_crit

def hypothesis(alpha_crit, alpha):
    if alpha_crit<=alpha:
        print("Гипотеза H0: s(a) = s(b) отвергается")
    else:
        print("Гипотеза H0: s(a) = s(b) принимается")

def critical_region(alpha, df1, df2):
    f_critical_lower = f.ppf(alpha/2, df1, df2)
    f_critical_upper = f.ppf(1 - alpha/2, df1, df2)
    return f_critical_lower, f_critical_upper

def free_stepen(size1, size2):
    df1 = size1 - 1
    df2 = size2 - 1
    return df1, df2


size1, size2 = size_data(data_A, data_B)
disp1, disp2 = dispercia(data_A, data_B)
fisher = statistic_Fishera(disp1, disp2)
df1, df2 = free_stepen(size1, size2)
f_critical_lower, f_critical_upper = critical_region(alpha, df1, df2)
alpha_crit = critical_alpha(df1, df2, fisher)


print("                          Прибор А       Прибор В")
print(f"Объем выборки               n1 ={size1}   n2 = {size2} ")
print(f"Дисперсия      s1^2 = {disp1}, s2^2 = {disp2}")

print(f"Статистика Фишера: Ф = {fisher}")
print(f"1%-я критическая область: {f_critical_lower} > T < {f_critical_upper}")
hypothesis(alpha_crit, alpha)
print(f"С критическим уровнем значимости: a(crit) = {alpha_crit}")