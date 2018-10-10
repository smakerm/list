sign = 1
sum = 0
n = 1
while n <= 100000:
    sum += sign * 1 / (2 * n -1)
    sign *= -1
    n += 1

print(sum, sum * 4)

