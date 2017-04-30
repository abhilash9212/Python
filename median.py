def median(n):
    mid = sorted(n)
    if len(mid) % 2 != 0:
        return mid[((len(mid)+1)/2)-1]
    else:
        return float(sum(mid[(len(mid)/2)-1:(len(mid)/2)+1]))/2.0