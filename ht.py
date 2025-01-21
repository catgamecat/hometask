#Task1
num_1 = float(input("Введите первое число: "))
num_2 = float(input("Введите второе число: "))
num_3 = float(input("Введите третье число: "))
sum_num = num_1 + num_2 + num_3
prod_num = num_1 * num_2 * num_3
print("Сумма ваших чисел:",(sum_num))
print("Произведение ваших чисел:",(prod_num))
print(f"Сумма ваших чисел: {sum_num}")
print(f"Произведение ваших чисел: {prod_num}")
print("Сумма ваших чисел: {}".format(sum_num))
print("Произведение ваших чисел: {}".format(prod_num))

#Task2
salary = float(input("В этом месяце вы заработали: "))
credit = float(input("Уплачено кредитной задолженности: "))
utility_bills = float(input("Потрачено на коммунальные услуги: "))
rest = salary - credit - utility_bills
print("Остаток:",(rest))
print(f"Остаток: {rest}")
print("Остаток: {}".format(rest))

#Task3
d1 = float(input("Введите длину первой диагонали: "))
d2 = float(input("Введите длину второй диагонали: "))
s = 0.5 * d1 * d2
print("Площадь ромба равна: ", s)
print(f'Площадь ромба равна {s}')
print("Площадь ромба равна: {}".format(s))

#Task4
print(f'To be\nor not\nto be')

#Task5
print(f'''"Life is what happens\n\twhen\n\t\tyou're busy making other plans"\n\t\t\t\t\t\t\t\tJohn Lennon''')
