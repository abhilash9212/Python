def factorial(x):
    x = range(1, x+1)
    factorial = 1
    if x == 1:
        return x
    elif x != 1:
        for i in x:
            factorial = factorial * i
    return factorial
    