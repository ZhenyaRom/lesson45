def is_prime(func):
    def wrapper(*args, **kwargs):
        summa = func(*args, **kwargs)
        if summa < 2:
            return summa
        elif summa > 2:
            for i in range(2, abs(summa) - 1):
                if summa % i == 0:
                    print('Составное')
                    return summa
        print('Простое')
        return summa
    return wrapper

@is_prime
def sum_three(one, two, three):
    return one + two + three

result = sum_three(2, 3, 6)
print(result)
