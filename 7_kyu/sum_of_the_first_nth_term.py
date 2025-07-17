# https://www.codewars.com/kata/555eded1ad94b00403000071/train/python

def series_sum(n):
    ans = sum(1/i for i in range(1, 3*n+1, 3))
    return f'{ans:.2f}'