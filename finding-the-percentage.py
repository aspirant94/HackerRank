def find_the_percentage(query_name, student_marks):
    ls = list(student_marks[query_name])
    x = 0
    i = 0
    for ele in ls:
        x = x + ele
        i = i + 1
    result = x / i
    print("%.2f" % result)


if __name__ == '__main__':

    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *lines = input().split(' ')
        scores = list(map(float, lines))
        student_marks[name] = scores
    query_name = input()
    find_the_percentage(query_name, student_marks)


