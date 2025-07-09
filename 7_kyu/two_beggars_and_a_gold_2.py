def distribution_of(golds):
    sums = [0, 0]
    while golds:
        i = 0
        while i < 2 and golds:
            sums[i] += golds.pop(-(golds[0] < golds[-1]))
            i += 1
    return sums