

call_count = 0
def set_test_case():
    n = int(input())
    t = []
    for i in range(n):
        t.append(input())

    return t


def recursion(s, l, r):
    global call_count
    call_count +=1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    global  call_count
    call_count = 0
    return recursion(s, 0, len(s)-1)


def solution():
    global call_count
    test_case = set_test_case()
    for t in test_case:
        print(f"{isPalindrome(t)} {call_count}")


if __name__ == '__main__':
    solution()
