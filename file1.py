from math import *


def main(b, a, n):
    summ = 0
    for i in range(1, n + 1):
        for c in range(1, a + 1):
            for j in range(1, b + 1):
                summ += (65 - c**2 - i / 95) ** 2 + 75 * log(j, 2) ** 6
    return summ
print(main(1, 2, 3))

