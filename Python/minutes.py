number = int(input())
if number > 1440:
    print("Время больше суток, программа слишком тупая чтоб это обработать")
elif number < 0:
    print("Зачем вводить отрицательные числа, мы же сутки считаем")
else:
    print(number // 60, number % 60)
