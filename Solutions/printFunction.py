## Print Function
## https://www.hackerrank.com/challenges/python-print/problem

from __future__ import print_function

if __name__ == '__main__':
    n = 3
    result = ""
    for number in range(n):
        result = result+str(number+1)    
    print(result)
