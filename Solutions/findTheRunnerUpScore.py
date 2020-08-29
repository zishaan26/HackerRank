## Find the Runner-Up Score!
## https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arrlist = list(arr)
    max=sorted(arrlist)[len(arrlist) - 1]

    newList = []

    for i in arrlist:
        if i != max:
            newList.append(i)
    
    print(sorted(newList)[len(newList) - 1])