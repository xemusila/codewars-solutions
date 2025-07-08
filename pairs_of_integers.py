from itertools import combinations_with_replacement
def generate_pairs(n):
    x = list(combinations_with_replacement(range(n+1), 2))
    return list(list(i) for i in x)