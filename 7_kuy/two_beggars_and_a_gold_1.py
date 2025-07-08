def distribution_of(golds):
    sums = [0, 0]
    while golds:
        i = 0
        while i < 2 and golds:
            if golds[0] >= golds[-1]:
                sums[i] += golds[0]
                golds = golds[1:]
            else:
                sums[i] += golds[-1]
                golds = golds[:-1]
            i += 1
    return sums
        