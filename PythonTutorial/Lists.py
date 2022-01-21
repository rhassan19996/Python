a = [3, 10, -1]
print(a)
# [3, 10, -1]
a.append(1)
print(a)
# [3, 10, -1, 1]
a.append("hello")
print(a)
# [3, 10, -1, 1, 'hello']
a.append([1, 2])
print(a)
# [3, 10, -1, 1, 'hello', [1, 2]]
a.pop()
a.pop()
print(a)
# [3, 10, -1, 1]
print(a[0])
# 3
print(a[3])
# 1

# assign a new number
a[0] = 100
print(a)

b = ['banana', 'apple', 'Microsoft']
print("Before swap: ")
print(b)
#temp = b[0]
#b[0] = b[1]
#b[1] = temp
#print("After swap")
#print(b)
#shortcut for swap
b[0], b[1] = b[1], b[0]
print(b)


