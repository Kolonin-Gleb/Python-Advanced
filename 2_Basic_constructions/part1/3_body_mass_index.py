# где масса измеряется в килограммах, а рост — в метрах.

mass = float(input())
height = float(input())


bmi = mass / (height ** 2)

if bmi > 25:
    print("Избыточная масса")
elif bmi < 18.5:
    print("Недостаточная масса")
else:
    print("Оптимальная масса")

# print(bmi)

