def digit_sum(n):
    #n = abs(n)
    digits = [int(x) for x in str(n)]
    return sum(digits)