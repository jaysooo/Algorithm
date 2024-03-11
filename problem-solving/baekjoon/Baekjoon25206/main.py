# input string 의 문자열을 파싱하고 아래 자료구조를 만든다
# subject / credits / grade
# 학점의 총합 = sum(credits)
# 전공 평점 = credits * grade / sum(credits)

def get_grade_score(grade):
    score = 0.0
    if grade == 'A+':
        score = 4.5
    elif grade == 'A0':
        score = 4.0
    elif grade == 'B+':
        score = 3.5
    elif grade == 'B0':
        score = 3.0
    elif grade == 'C+':
        score = 2.5
    elif grade == 'C0':
        score = 2.0
    elif grade == 'D+':
        score = 1.5
    elif grade == 'D0':
        score = 1.0
    else:
        score = 0.0

    return float(score)


def solution() :
    total_credits = 0.0
    term_grade = []
    total_score = 0.0
    for i in range(20):
        input_str = input().split(" ")
        subject = input_str[0]
        credit = float(input_str[1])
        grade = input_str[2]
        if grade == 'P' :
            continue

        score = get_grade_score(grade)
        total_credits += credit
        term_grade.append((subject,credit,grade,score))
        total_score += credit * score
    if total_score > 0:
        print(f"{(total_score/total_credits):.6f}")
    else:
        print(f"{(total_score):.6f}")



if __name__ == '__main__':
    solution()