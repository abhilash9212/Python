def is_prime(x):
    #i = range(2, x-1)
    if x <=1:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        else:
            return True