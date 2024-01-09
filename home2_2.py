# 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions

from fractions import Fraction

# Наименьшее общее кратное
def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b

    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1
    return lcm

# Наименьший общий делитель
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

# Функция суммы дробей
def sum_frac(frac1, frac2):
    chs1, znm1 = map(int, frac1.split('/'))
    chs2, znm2 = map(int, frac2.split('/'))
    znm_gnr = lcm(znm1, znm2)
    chs_gnr = chs1 * (znm_gnr / znm1) + chs2 * (znm_gnr / znm2)
    # print(f'Сумма {chs_gnr}/{znm_gnr}')
    # print(gcd(znm_gnr, chs_gnr))
    nod = gcd(znm_gnr, chs_gnr)
    znm_gnr = round(znm_gnr / nod)
    chs_gnr = round(chs_gnr / nod)
    print(f'Сумма {chs_gnr}/{znm_gnr}')

# Функция произведения дробей
def mul_frac(frac1, frac2):
    chs1, znm1 = map(int, frac1.split('/'))
    chs2, znm2 = map(int, frac2.split('/'))
    chs_gnr = chs1 * chs2
    znm_gnr = znm1 * znm2
    # print(f'Произведение {chs_gnr}/{znm_gnr}')
    # print(gcd(znm_gnr, chs_gnr))
    nod = gcd(znm_gnr, chs_gnr)
    znm_gnr = round(znm_gnr / nod)
    chs_gnr = round(chs_gnr / nod)
    print(f'Произведение {chs_gnr}/{znm_gnr}')

# Функция пороверки с помощью Fraction
def frc_opr(frac1, frac2):
    chs1, znm1 = map(int, frac1.split('/'))
    chs2, znm2 = map(int, frac2.split('/'))

    fraction1 = Fraction(chs1, znm1)
    fraction2 = Fraction(chs2, znm2)

    sum_frc = fraction1 + fraction2
    print(f'Сумма:{sum_frc}')

    mlt_frc = fraction1 * fraction2
    print(f'Произведение:{mlt_frc}')

frac1 = input('Введите первую дробь: ')
frac2 = input('Введите вторую дробь: ')
print()
sum_frac(frac1, frac2)
mul_frac(frac1, frac2)
print()

print('Проверка:')
frc_opr(frac1, frac2)

