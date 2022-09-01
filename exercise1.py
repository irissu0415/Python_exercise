# 1.迴圏的練習 - factor
# 輸入一正整數，求其所有的因數。說明：36的因數為1, 2, 3, 4, 6, 9, 12, 18, 36,

number = int(input("請輸入一正整數:"))
number_list = []
for i in range(1, number):
    if number % i == 0:
        number_list.append(i)
    else:
        continue
number_list.append(number)
print(number_list)

# 2.迴圏的練習 - perfect_number
# 一個數字若等於其所有因數的總和，則此數為perfect number。找出100以內所有的完美數。
# 說明：6的因數為1, 2, 3，6 = 1 + 2 + 3，故6為完美數。

number = []
number_list = []
for i in range(1, 100+1):
    factor = []
    for j in range(1, i):
        if i % j == 0:
            factor.append(j)
    
    number_sum = sum(factor)
    if number_sum > 1:
        number.append(i)
        number_list.append(number_sum)

perfect_number = []
for i, j in zip(number, number_list):
    if i == j:
        perfect_number.append(i)

print(perfect_number)

# 3.迴圏的練習 - armstrong
# Armstrong數是指一個三位數的整數，其各位數之立方和等於該數本身。找出所有的Armstrong數。
# 說明：153 = 1 ^ 3 + 5 ^ 3 + 3 ^ 3，故153為Armstrong數。(2 ^ 3 表示 2 的 3 次方, 3 ^ 3 表示 3 的 3 次方)

armstrong_number = []

for i in range(2, 1000):
    n1 = i // 100
    n2 = i // 10 % 10
    n3 = i % 100 % 10
    total_n = n1 ** 3 + n2 ** 3 + n3 ** 3
    if i == total_n and i > 1:
        armstrong_number.append(i)

print(armstrong_number)

# 4.迴圈的練習 - prime
# 輸入一正整數，找出所有小於或等於的質數。

number = int(input("請輸入一正整數:"))
number_list = []
for j in range(2, number + 1):
    for i in range(2, j):
        if j % i == 0:
            break
    else:
        number_list.append(j)

print(number_list)

# 5.迴圈敘述的練習 - interest
# 某人A以10 % 單利投資100000元，某人B則以5 % 複利投資100000元。計算多少年後某人B的投資可以超過某人A，並將此時兩人錢數印出。(27年後)
# 提示：單利公式：P(1 + r * n)；複利公式：P(1 + r) ^ n；P：本金，r：利率，n：多少年(備註︰(1+r) ^ n 表示(1 + r)的n次方)

invest_a = 100000
invest_b = 100000

n = 0
while n >= 0:
    invest_a_cal = invest_a * (1 + 0.1 * n)
    invest_b_cal = invest_b * (1 + 0.05) ** n
    if invest_a_cal < invest_b_cal:
        print(n, "年\nA總金額:", int(invest_a_cal), "元\nB總金額:", int(invest_b_cal), "元")
        break
    else:
        n += 1
