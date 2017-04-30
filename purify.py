def purify(n):
    even_num = []
    for i in n:
        if i % 2 == 0:
            even_num.append(i)
    return even_num