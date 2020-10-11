# Lists
# https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())

    commandList = []
    resultList = []

    for i in range(N):
        commandList.append(input())

    for commandStr in commandList:
        command=commandStr.split( )
        cmd=command[0]
        if cmd=='insert':
            resultList.insert(int(command[1]),int(command[2]))
        elif cmd=='print':
            print(resultList)
        elif cmd=='remove':
            resultList.remove(int(command[1]))
        elif cmd=='append':
            resultList.append(int(command[1]))
        elif cmd=='sort':
            resultList=sorted(resultList)
        elif cmd=='pop':
            resultList.pop()
        elif cmd=='reverse':
            resultList=resultList[::-1]
        else:
            pass