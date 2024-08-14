import pandas as pd
from scipy import stats
import numpy as np
from scipy.stats import binom

#Путь к файлу
excel_file_path = "/Users/elinagalimova/Downloads/ZadanMS208.xls"
#Название листа
sheet_name = "Sheet2"
#Название столбца
column_name_1 = "Z7A"
column_name_2 = "Z7B"

df_1 = pd.read_excel(excel_file_path, sheet_name=sheet_name)
df_2 = pd.read_excel(excel_file_path, sheet_name=sheet_name)

data_1 = df_1[column_name_1]
data_1 = data_1.dropna()

data_2 = df_2[column_name_2]
data_2 = data_2.dropna()

alpha = 0.05
H1 = "1-ая группа меньше"
def data_size(data_1, data_2):
    size_1 = len(data_1)
    size_2 = len(data_2)
    return size_1, size_2

def avarage_value(data_1, data_2):
    average_1 = np.mean(data_1)
    average_2 = np.mean(data_2)
    return average_1, average_2

def std_deviation(data_1, data_2):
    std_1 = np.std(data_1)
    std_2 = np.std(data_2)
    return std_1, std_2

def std_error_of_mean(data_1, data_2):
    std_error_1 = np.std(data_1) / np.sqrt(len(data_1))
    std_error_2 = np.std(data_2) / np.sqrt(len(data_2))
    return std_error_1, std_error_2

def stat_Student(data_1, data_2, alternative ):
    t_statistic, p_value = stats.ttest_ind(data_1, data_2, alternative=alternative)
    return t_statistic, p_value



def hypothesis(p_value, alpha):
    if p_value < alpha:
        print("Гипотеза о различии математических ожиданий отвергается")
    else:
        print("Гипотеза о различии математических ожиданий принимается")

def critical_region(alpha, dof):
    # Найти критическое значение для заданного уровня значимости и степеней свободы
    t_critical = stats.t.ppf(1-alpha, dof)
    return (t_critical)



print("                                       Group A            Group B")
print(f"Объем наблюдений                            {data_size(data_1, data_2)}   ")
print(f"Среднее                          {avarage_value(data_1, data_2)}")
print(f"Стандартное отклонение           {std_deviation(data_1, data_2)}")
print(f"Станд. ошибка среднего         {std_error_of_mean(data_1, data_2)}\n")

alternative = "less"
t_statistic, p_value = stat_Student(data_1, data_2, alternative )
print(f"Статистика Стьюдента Т  {t_statistic}")

size_1, size_2 = data_size(data_1, data_2)
dof = size_1 + size_2 - 2
critical_region = critical_region(alpha, dof)
print("5%-ая критическая область:", critical_region)

print(f"С критическим уравнем значимости {p_value}")

