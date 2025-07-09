def fix_parentheses(strng):
    closed = 0
    opened = 0
    for s in strng:
        if s == '(':
            opened += 1
        elif opened == 0:
            closed += 1
        else:
            opened -= 1
    return '('*closed + strng + ')'*opened
