#задача_1
var_1 = 123
var_2 = "Python"
var_3 = (1, 2, 3)
print(f"{var_1}, {var_2}, {var_3}")

while True:
    var_num = input("input number: ")
    if var_num.isdigit():
        print(f"Your number is: {var_num}")
        break
    print("Try again!")

var_str = input("input string: ")
print(f"Your string is: {var_str}")

#задача_2
while True:
    time_in_sec = input("input time in seconds: ")
    if time_in_sec.isdigit():
        time_in_sec = int(time_in_sec)
        hours = time_in_sec // 3600
        minutes = time_in_sec // 60 - hours * 60
        seconds = time_in_sec % 60
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        break
    print("Try again!")

#задача_3
while True:
    n = input("input number n: ")
    if n.isdigit() and int(n) > 0:
        print(f"{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}")
        break
    print("Try again!")

#задача_4
while True:
    n = input("input number: ")
    temp_var = 0
    if n.isdigit() and int(n) > 0:
        n = int(n)
        while n > 0:
            if n % 10 > temp_var:
                temp_var = n % 10
            n = n // 10
        print(f"Maximum digit is: {temp_var}")
        break
    print("Try again!")

#задача 5-6
money = float(input("Введите значение выручки: "))
costs = float(input("Введите значение издержек: "))
if money - costs > 0:
    print(f"Компания отработала с прибылью, рентабельность: {(money / costs - 1)* 100:.2f}%")
    guys = int(input("Введите число сотрудников: "))
    print(f"Прибыль на каждого сотрудника: {(money - costs) / guys:.2f}")
elif money - costs < 0:
    print(f"Убыток компании: {- money + costs}")
else:
    print(f"Без прибыли и убытка")

#задача 7
a = float(input("Введите результат пробежки в первый день: "))
b = float(input("Введите целевую дистанцию: "))
count = 1
while True:
    if a * 1.1 < b:
        count += 1
        a = a * 1.1
    else:
        print(f"Целевой результат будет получен на: {count + 1} день")
        break


