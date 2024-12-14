# Capitals = {'Russia' : 'Moscow', 'Ukraine' : 'Kiev', 'USA' : "Washington"}
# Capitals = dict(Russia = 'Moscow', Ukraine = 'Kiev', USA = "Washington")
# Capitals = dict([('Russia' : 'Moscow'), (Ukraine = 'Kiev'), (USA = 'Washington')])

# A = {'ab' : 'ba', 'aa' : 'aa'}
# A['ac'] = 'element'

# key = 'ac'
# if key in A:
#     del A[key]

# request = dict(Name = 'Lebovsky', Age = '35', City = 'Los Angeles')
# print(request)

# text = input().split()
# dictionary = dict()

# for i in text:
#     dictionary[i] = dictionary.get(i, 0) + 1
#     print(dictionary[i] - 1, end=' ')

number = int(input())
dic = dict()
for i in range(number):
    list = input().split()
    dic[list[0]] = list[1]
print(dic)

findWord = input()
# for a in dic:
print(dic.get(findWord, 0))

for i in dic:
    if findWord == dic[i]:
        print(dic.get(i, 0))