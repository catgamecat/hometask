#Task6
meters = float(input('Введите значение в метрах: '))
sm = meters * 100
dm = meters * 10
mm = meters * 1000
miles = meters * 0.000621
print(f'{sm}\n{dm}\n{mm}\n{miles}')

#Task7
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
res = round(num1  / num2, 2)
print(res)

#Task11
a = 3
b = 5
a,b = b,a
print(a, b)

#Task12
#a
a = 1
b = 2
c = 3
a, b, c = c, a, b

#b
c, a, b = b, c, a

#Task13
side_square = 5
p = side_square * 4
radius = 5
diam = radius * 2
print("Периметр квадрата равен:",p,"Диаметр окружности равен:", diam)
print(f"Периметр квадрата равен: {p}\nДиаметр окружности равен: {diam}")
print("Периметр квадрата равен: {}\nДиаметр окружности равен: {}".format(p, diam))
