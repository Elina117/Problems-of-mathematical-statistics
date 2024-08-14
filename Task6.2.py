import pandas as pd
from scipy.stats import binom
from scipy.special import comb

#Путь к файлу
excel_file_path = "/Users/elinagalimova/Downloads/ZadanMS208.xls"
#Название листа
sheet_name = "Sheet2"
#Название столбца
column_name_before = "Z6IIA"
column_name_after = "Z6IIB"

df_before = pd.read_excel(excel_file_path, sheet_name=sheet_name)
df_after = pd.read_excel(excel_file_path, sheet_name=sheet_name)

data_before = df_before[column_name_before]
data_before = data_before.dropna()

data_after = df_after[column_name_after]
data_after = data_after.dropna()

# Заданный уровень значимости
alpha = 0.05

# Ожидаемый эффект: уменьшение
expected_effect = "Уменьшится"

binary_data = []
for i in range(len(data_before)):
    if data_before[i] > data_after[i]:
        binary_data.append(1) # Эффект есть (уменьшится)
    else:
        binary_data.append(0) # Эффекта нет (увелилилось или не изменилось)

# Частота появления благоприятных событий
frequency = sum(binary_data)/len(binary_data)
print(f"Частота ожидаемого эффекта (уменьшения) = {frequency}, {sum(binary_data)} из {len(binary_data)}")

def sign_test(binary_data, alpha):
    statistic = sum(binary_data)
    p_value = binom.cdf(statistic, len(binary_data), alpha)
    return statistic, p_value

statistic, p_value = sign_test(binary_data, alpha)
m = statistic

# Вычисляем критическое значение для 5%-ой критической области
critical_value = binom.ppf(1 - alpha, len(binary_data), 0.5)
print("5%-ая критическая область:", critical_value)



# Критическое значение по формуле биноминального распределения
n = len(binary_data)
def critical_alpha(n):
    alpha_crit = 0
    p = 0.5
    for k in range(m, n + 1):
        alpha_crit += comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
    return alpha_crit

print("Критическое значение :", critical_alpha(n))

def hypothesis(critical_alpha, alpha):
    if critical_alpha<=alpha:
        print("Гипотеза отвергается")
    else:
        print("Гипотеза принимается")

hypothesis(critical_alpha(len(data_before)), alpha)