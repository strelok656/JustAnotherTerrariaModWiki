# A = int(input())
# B = int(input())

# B += 1

# for i in range(A, B):
#     print(i)

# n = int(input())

# if n <= 9:
#     if n == 9:
#         print(1)
#         print(12)
#         print(123)
#         print(1234)
#         print(12345)
#         print(123456)
#         print(1234567)
#         print(12345678)
#         print(123456789)
#     if n == 8:
#         print(1)
#         print(12)
#         print(123)
#         print(1234)
#         print(12345)
#         print(123456)
#         print(1234567)
#         print(12345678)
#     if n == 7:
#         print(1)
#         print(12)
#         print(123)
#         print(1234)
#         print(12345)
#         print(123456)
#         print(1234567)
#     if n == 6:
#         print(1)
#         print(12)
#         print(123)
#         print(1234)
#         print(12345)
#         print(123456)
#     if n == 5:
#         print(1)
#         print(12)
#         print(123)
#         print(1234)
#         print(12345)
#     if n == 4:
#         print(1)
#         print(12)
#         print(123)
#         print(1234)
#     if n == 3:
#         print(1)
#         print(12)
#         print(123)
#     if n == 2:
#         print(1)
#         print(12)
#     if n == 1:
#         print(1)

# n = int(input())
# ladder = ""

# if n <= 9:
#     for i in range(1, n + 1):
#         ladder += str(i)
#         print(ladder)
# else:
#     print("You are dibil")

i = 1
while i <= 10:
    print(i ** 2)
    i += 1

n = int(input())
length = 0
while n > 0:
    n //= 10
    length += 1
print(length)