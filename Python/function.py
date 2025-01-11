# def factorial(n):
#     res = 1
#     for i in range(1, n + 1):
#         res *= i
#     return res

# print(factorial(3))
# print(factorial(5))

# def short_story():
#     print("У попа была собака, он её любил")
#     print("gdgf")
#     print("gdfgdfg")
#     short_story()
# short_story()

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(5))

# import math

# q = float(input())
# w = float(input())
# e = float(input())
# r = float(input())

# def distance(x1, y1, x2, y2):
#     a = math.sqrt((y1 - x1)**2 + (y2 - x2)**2)
#     print(a)
# distance(q, w, e, r)

# x = float(input())
# y = int(input())

# def niggative_degree(x, y):
#     if y == 0:
#         return 1
#     else:
#         for i in range(y):
#             c = x * i
#         return(1 / c)

# print(niggative_degree(x, y))

# x = float(input())
# y = abs(int(input()))

# def niggative_degree(x, y):
#     if y == 0:
#         return 1
#     else:
#         return 1 / x * niggative_degree(x, y - 1)

# print(niggative_degree(x, y))