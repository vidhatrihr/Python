num = int(input())

# array = []

# for i in range(1, num+1):
#   array.append(str(i))

# print(','.join(array))

array = list(map(str, range(1, num+1)))
print(','.join(array))
