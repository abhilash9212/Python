def remove_duplicates(n):
    fresh = []
    for i in n:
        if i not in fresh:
            fresh.append(i)
    return fresh