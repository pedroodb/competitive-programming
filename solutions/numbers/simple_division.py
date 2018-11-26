import math

def gcd(u, v):
    while v > 0:
        r = u % v
        u = v
        v = r
    return math.fabs(u)

numbers = list(map(int, input().split(" ")))
while not numbers[0] == 0:
    values = list()
    for i in range(1, len(numbers) - 1):
        values.append(numbers[i] - numbers[0])
    res = values[0]
    for i in range(1, len(values)):
        res = gcd(res, values[i])
    print(int(res))
    numbers = list(map(int, input().split(" ")))