## Write a function
## https://www.hackerrank.com/challenges/write-a-function/problem

def is_leap(year):
    leap = False
    if year%4 == 0:
        leap = True
        if year%100 == 0:
            if year%400 == 0:
                leap = True
            else:
                leap = False
    else:
        leap = False
    # Write your logic here
    
    return leap

year = 1988
print (is_leap(year))