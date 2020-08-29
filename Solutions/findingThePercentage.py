## Finding the percentage
## https://www.hackerrank.com/challenges/finding-the-percentage/problem

def percentage(a, b, c):
    return float((a+b+c)/3)

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    print("%.2f" % percentage(student_marks.get(query_name)[0],student_marks.get(query_name)[1],student_marks.get(query_name)[2]))
