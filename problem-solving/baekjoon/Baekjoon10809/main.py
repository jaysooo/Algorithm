

def set_test_case():
    input_str = input()
    return input_str


def solution():
    input_str = set_test_case()
    alphabet = [-1] * 26
    for idx,c in enumerate(input_str):
        ascii_char = ord(c) % 97
        if alphabet[ascii_char] == -1 :
            alphabet[ascii_char] = idx
    #print(f"org : {c} ord : {a%97}")


    alphabet=list(map(lambda x: str(x),alphabet))
    print(" ".join(alphabet))


solution()


