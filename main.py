# Load the decimal package to reconfigure the defauly precision 
# of the decimal type as float doesn't have the capabilities
from decimal import getcontext, Decimal

def getpi(n):
    """
    Take input 'n' and returns Pi upto n values.

    USAGE:

    print(getpi(4))

    OUTPUT:

    3.1415
    """
    # Set precision to be two decimals more than required
    getcontext().prec = n + 2
    # Initialize variable to zero for the loop
    pi = 0
    # Calculate each iteration of the BBP expansion
    for i in range(n):
        t1 = Decimal(4 / (8*i + 1))
        t2 = Decimal(2 / (8*i + 4))
        t3 = Decimal(1 / (8*i + 5))
        t4 = Decimal(1 / (8*i + 6))
        iteration = Decimal((t1 - t2 - t3 - t4) / 16**i)
        pi = pi + iteration
    return round(pi, n)

# Take input for the precision requirement
n = input("Enter precision required: \n")
# Set precision based on input
precision = int(n)
# Check the validity of the input and test the function
if isinstance(precision, int):
    print("\nPrecision Required: {0}".format(precision))
    print(getpi(precision))
else:
    print("Couldn't parse entered value. Try again.")