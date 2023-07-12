

def is_palindrome(word):

    cursor = 0
    reversed = []
    for i in range(len(word)-1, -1, -1):
        reversed += [word[i]]

    if ''.join(reversed) == word:
        return 1
    else:
        return 0


def solution():
    input_str = input()
    print(is_palindrome(input_str))


solution()
