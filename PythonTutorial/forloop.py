a = ['banana', 'apple', 'microsoft']

for items in a:
    print(a)

b = [20, 10, 5]
total = 0
for i in b:
    total += i
print(total)

print(list(range(1, 8)))

total3 = 0
for i in range(1, 8):
    if i % 3 == 0:
        total3 += i
print(total3)

total4 = 0
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        total4 += i
print(total4)

total5 = 0
given_list = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
j = len(given_list) - 1

while given_list[j] < 0:
    total5 += given_list[j]
    j -= 1
print(total5)
