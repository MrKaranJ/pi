from decimal import getcontext, Decimal

def getpi(n):
    print(3.14)
    getcontext().prec = n + 2
    pi = 0
    for i in range(n):
        t1 = Decimal(4 / (8*i + 1))
        t2 = Decimal(2 / (8*i + 4))
        t3 = Decimal(1 / (8*i + 5))
        t4 = Decimal(1 / (8*i + 6))
        iteration = Decimal((t1 - t2 - t3 - t4) / 16**i)
        pi = pi + iteration
    print(pi)

n = input("Enter precision required: \n")
precision = int(n)
if isinstance(precision, int):
    print("Precision Required: {0}".format(precision))
    getpi(precision)
else:
    print("Couldn't parse entered value. Try again.")