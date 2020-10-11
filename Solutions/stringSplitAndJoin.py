## String Split and Join
## https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    list=line.split(" ")
    return "-".join(list)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
