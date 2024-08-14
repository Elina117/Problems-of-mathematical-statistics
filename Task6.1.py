# Одновыборочный вариант. Имеется одна выборка. Требуется проверить
# гипотезу, что некоторое фиксированное событие происходит чаще, чем
# противоположное к этому событию утверждение
import pandas as pd
from scipy.stats import binom
from scipy.special import comb

#Путь к файлу
excel_file_path = "/Users/elinagalimova/Downloads/ZadanMS208.xls"
#Название листа
sheet_name = "Sheet2"
#Название столбца
column_name = "Z6I"
df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

data = df[column_name]
data = data.dropna()

## КРИТЕРИЙ ЗНАКОВ

p0 = 0.2
alpha = 0.05

data_A = [x for x in data if x == 'A']
data_B = [x for x in data if x == 'B']

n = len(data)

#функция критерия знаков
def sign_test(data_A, alpha, n):
    statistic = len(data_A)
    p_value = binom.cdf(statistic, n, alpha)
    return statistic, p_value

statistic, p_value = sign_test(data_A, alpha, n)
m = statistic


# Частота появления А
frequency_A = sum(1 for x in data if x == 'A') / len(data)
print(f"Частота появления А = {frequency_A}, {len(data_A)} из {len(data)}")

# Находим критические значения для критерия знаков
critical_region = binom.ppf(1 - alpha, n, 0.2)


print("Критическая область (правая граница):", critical_region)



# Критическое значение по формуле бинарного распределения
def critical_alpha(n, p0):
    alpha_crit = 0
    for k in range(m, n+1):
        alpha_crit += comb(n, k) * (p0 ** k) * ((1 - p0) ** (n - k))
    return alpha_crit

print("Критическое значение :", critical_alpha(len(data), p0))


# Принятие решения по гипотезе
def hypothesis(critical_alpha, alpha):
    if critical_alpha<=alpha:
        print("Гипотеза отвергается")
    else:
        print("Гипотеза принимается")

hypothesis(critical_alpha(len(data_A), p0), alpha)

