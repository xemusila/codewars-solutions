import random
def generate(length):
    ans = ''
    for i in range(length):
        ans += str(random.randint(0, 1))
    return ans