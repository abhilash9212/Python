def count(sequence, item):
    seq = list(sequence)
    value = 0
    for i in range(0, len(seq)):
        if seq[i] == item:
            value = value + 1
    return value