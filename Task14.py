import pandas as pd
from scipy.stats import chi2
import numpy as np

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

n = len(data_X)
alpha = 0.05
r = 5
s = 3
df = (r-1)*(s-1)
def board_points():
    broad_points_X = np.linspace(118.05, 126.05 , 5 + 1, endpoint=True) #делим на интервалы, включая последнюю точку
    intervals_X = [(broad_points_X[i], broad_points_X[i+1]) for i in range(5)]

    broad_points_Y = np.linspace(80.05, 86.05 , 3 + 1, endpoint=True) #делим на интервалы, включая последнюю точку
    intervals_Y = [(broad_points_Y[i], broad_points_Y[i+1]) for i in range(3)]


    intervals_X.insert(0, (float('-inf'), 118.05))
    intervals_X.append((126.05, float('inf')))

    intervals_Y.insert(0, (float('-inf'), 80.05))
    intervals_Y.append((86.05, float('inf')))

    return intervals_X, intervals_Y



def table(intervals_X, intervals_Y ):
    combination_matrix = np.zeros((len(intervals_X), len(intervals_Y)))

    # Заполнение матрицы
    for index_x, interval_x in enumerate(intervals_X):
        for index_y, interval_y in enumerate(intervals_Y):
            count = 0
            for x, y in zip(data_X, data_Y):
                if interval_x[0] <= x <= interval_x[1] and interval_y[0] <= y <= interval_y[1]:
                    count += 1
            combination_matrix[index_x, index_y] = count

    # Сложение отдельно каждой строки матрицы
    row_sums = np.sum(combination_matrix, axis=1)

    # Сложение отдельно каждого столбца матрицы
    column_sums = np.sum(combination_matrix, axis=0)

    # Сумма всех значений матрицы
    sum_all = np.sum(combination_matrix)

    return row_sums, column_sums, sum_all, combination_matrix


intervals_X, intervals_Y = board_points()
row_sums, column_sums, sum_all, combination_matrix = table(intervals_X, intervals_Y )

# Вычисление ожидаемых частот
expected_matrix = np.outer(row_sums, column_sums) / sum_all

# Вычисление статистики критерия сопряженности хи-квадрат
chi_squared_statistic = np.sum((combination_matrix - expected_matrix)**2 / expected_matrix)
# Вычисление критического значения
critical_value = 1 - chi2.cdf(alpha, df)

def hypothesis(alpha_crit, alpha):
    if alpha_crit<=alpha:
        print("Гипотеза независимости отвергается")
    else:
        print("Гипотеза независимости принимается")

def critical_region(alpha, degrees_of_freedom):
    crit_value = chi2.ppf(1 - alpha, degrees_of_freedom)
    critical_region = f"значения статистики хи-квадрат больше {crit_value}"
    return critical_region

def critical_value(alpha, df):
    # Вычисление критического значения
    critical_value = 1 - chi2.cdf(alpha, df)
    return critical_value

print("Сумма по строкам:", row_sums)
print("Сумма по столбцам:", column_sums)
print("Сумма всех значений матрицы:", sum_all)
# Вывод матрицы
print("Матрица сочетаний ij:")
print(combination_matrix)

print("Статистика критерия сопряженности хи-квадрат:", chi_squared_statistic)
print("Степень свободы:", df)
critical_reg = critical_region(alpha, df)
critical_val = critical_value(alpha, df)
print("5%-я критическая область:", critical_reg)
hypothesis(critical_val, alpha)
print("Критическое значение:", critical_val)

