# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    x = round(number, ndigits)
    return x


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    res2 = (ticket_number % 1000)
    res1 = (ticket_number - res2) // 1000
    x = str(res1)
    c = str(res2)
    summa1 = 0
    summa2 = 0
    for i in x:
        summa1 += int(i)
    else:
        for i in c:
            summa2 += int(i)
        else:
            if summa1 == summa2:
                return True
            else:
                return False


print(lucky_ticket(123061))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
