import math


def subtractProductAndSum(n):
    product = 1
    sum = 0
    while n > 0:
        product *= n % 10
        sum += n % 10
        n = math.floor(n/10)
    return product-sum
