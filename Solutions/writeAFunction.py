## Write a function
## https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year):
    leap = False
    if year%4 == 0:
        leap = True
        if year%100 == 0:
            leap = year%400 == 0
    else:
        leap = False
    return leap

year = int(input())
print (is_leap(year))
