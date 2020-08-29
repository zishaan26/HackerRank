## Nested Lists
## https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    studentsName = []
    studentsScore = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        studentsName.append(name)
        studentsScore.append(score)

    secondLastScore=sorted(list(set(studentsScore)))[1]

    secondLastScoreStudentsName = []

    for i,studentScore in enumerate(studentsScore):
        if studentScore == secondLastScore:
            secondLastScoreStudentsName.append(studentsName[i])
    
    for name in sorted(secondLastScoreStudentsName):
        print(name)
