import pandas as pd
import numpy as np
import scipy.stats as stats

# Путь к файлу
excel_file_path = "/Users/elinagalimova/Downloads/ZadanMS208.xls"
# Название листа
sheet_name = "Sheet2"
# Название столбца
column_name = "Z13"
df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

data = df[column_name]
data = data.dropna()

size = len(data)
num_kondicion = sum(data > 118.5)
dolya_kondicion = num_kondicion/size
std_error = np.sqrt(dolya_kondicion * (1 - dolya_kondicion) / size)

Q = 0.975
alpha = 1 - Q
degrees_of_freedom = size - 1
t_quantile = stats.norm.ppf(1 - alpha, size, dolya_kondicion)

def tocno_board(Q, size, dolya_kondicion):
    p_lower_bound = stats.binom.ppf(Q, size, dolya_kondicion )
    return p_lower_bound / size
def pribliz_borad(dolya_kondicion, t_quantile, std_error):
    lower_bound = dolya_kondicion - t_quantile * std_error
    return lower_bound

print(f"Объем выборки: {size}")
print(f"Число кондиционных: {num_kondicion}")
print(f"Доля кондиционных: {dolya_kondicion}")
print(f"Станд. ошибка среднего: {std_error}")
print(f"97.5%-я нижняя граница\n(приближенная) > {pribliz_borad(dolya_kondicion, t_quantile, std_error)}\n(точная) > {tocno_board(Q, size, dolya_kondicion)}")