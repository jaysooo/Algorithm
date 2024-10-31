

def set_test_case():
    n = int(input())
    students = []
    for i in range(n):
        students += [input()]
    return students

def solution():
    students = set_test_case()
    len_of_numbers = len(students[0])

    answer = 0
    for i in range(1,len_of_numbers+1):
        unique_no = []
        for s in students:
            unique_no.append(s[-(i):])
        if len(set(unique_no)) == len(students):
            answer = i
            break

    print(answer)

if __name__ == '__main__':
    solution()