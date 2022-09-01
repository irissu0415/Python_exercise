# 1.函數的練習-power
# 寫一函數power(x, n)用來計算x的n次方。說明：power (5,3)即計算5^3。

def power(x, n):
    return x ** n


num_1 = int(input("請輸入底數:"))
num_2 = int(input("請輸入指數:"))
print("ans:", power(num_1, num_2))


# 2.函數的練習-is_prime
# 寫一函數is_prime(n)用來判斷n是否為質數。

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        else:
            return True


number = int(input("請輸入數字:"))
print(is_prime(number))

# 3.函數的練習-prime
# 寫一函數get_prime(n)用來找出第n個質數。


def prime(k):
    for i in range(2, k):
        if k % i == 0:
            return False
    else:
        number_list.append(k)


def get_prime(n):
    x = 2
    while x > 1:
        prime(x)
        x += 1
        if len(number_list) == n:
            print(number_list[n-1])
            break


number_list = []
number = int(input("請輸入一正整數:"))
get_prime(number)

# 4.函數的練習-mersenne_prime
# 寫一函數is_mersenne_prime(n)用來判斷n是否為Mersenne質數。撰寫一程式找出前5個Mersenne質數。
# 提示：若質數滿足2^P-1=n (p為正整數)，則n為Mersenne Prime。說明：當p=3時，2^3-1=7，故7為Mersenne Prime。


def is_mersenne_prime(n):
    def prime(k):
        for i in range(2, k):
            if k % i == 0:
                return False
        else:
             return True

    for j in range(2, n):
        prime(n)
        num_cal = (2 ** j) - 1
        if prime(n) is True:
            if num_cal == n:
                number_list.append(n)
                break
            elif num_cal < n:
                j += 1
            else:
                return False
        else:
            return False


number_list = []

x = 2
while x > 1:
    is_mersenne_prime(x)
    x += 1
    if len(number_list) == 5:
        print(number_list)
        break


# 5.遞迴函數的練習-factorial_recursive
# 寫一遞迴函數factorial (n)用來計算1*2*3*…*n的值。提示：factorial (n) = n * factorial(n-1)，factorial(1)=1

def factorial(n):
    if n == 1:
        return 1
    elif n == 2:
        return n * (n - 1)
    else:
        return n * factorial(n-1)


data = int(input("輸入欲計算數:"))
print(factorial(data))