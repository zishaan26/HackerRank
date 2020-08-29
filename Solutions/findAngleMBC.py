## Find Angle MBC
## https://www.hackerrank.com/challenges/find-angle/problem

import math

AB,BC=int(input()),int(input())

hypotenuse=math.hypot(AB,BC)
result=round(math.degrees(math.acos(BC/hypotenuse)))

degreeSymbol=chr(176)         

print(result,degreeSymbol, sep='')