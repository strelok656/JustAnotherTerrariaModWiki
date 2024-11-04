number = int(input())
if number > (10**10):
    print("Комплексы с размерами?")
elif number % 4 == 0 and number % 100 > 0:
    print("YES")
elif number % 400 == 0:
    print("YES")
elif number < 0:
    print("Любитель отрицательных чисел тут нашелся")
else:
    print("NO")