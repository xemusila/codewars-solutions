# def solve(eq):
#     symb = eq
#     for sign in ('*', '+', '-', '/'):
#         symb = symb.split(sign)
#         symb = ' '.join(symb)
#     symb = symb.split()[::-1]
#     print(symb)
#     sorted_symb = sorted(symb, reverse=True)
#     print(sorted_symb)
#     signs = eq
#     for s in sorted_symb:
#         signs = signs.split(s)
#         signs = ' '.join(signs)
#     print(signs)
#     signs = signs.split()[::-1]
#     res = ''
#     print(signs)
#     for i in range(len(symb) - 1):
#         res += symb[i] + signs[i]
#     res += symb[-1]
#     return res

import re

def solve(eq):
    tokens = re.findall(r'\w+|[*+\-/]', eq)
    
    return ''.join(tokens[::-1])
