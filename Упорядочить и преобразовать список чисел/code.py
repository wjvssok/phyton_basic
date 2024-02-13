stroka = input()

n = stroka.split(",")

num = []

for i in range(3):
    num.append(float(n[i]))

num = sorted(num)

b1 = bin(int(round(num[0]))).count('1')
b2 = bin(int(round(num[1]))).count('1')
b3 = bin(int(round(num[2]))).count('1')

a = [b1, b2, b3]
a = sorted(a)
print(a[0], a[1], a[2])