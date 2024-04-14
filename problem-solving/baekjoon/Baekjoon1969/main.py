def get_hamming_distance(dna1,dna2,m):
    hamming_distance = 0

    for i in range(m):
        if dna1[i] != dna2[i]:
            hamming_distance += 1

    return hamming_distance

def get_test_case():
    input_str= input().split(" ")
    h,m = int(input_str[0]),int(input_str[1])
    dna_list = ['' for x in range(h)]
    for i in range(h):
        dna_list[i] = input()
    return h,m,dna_list


def solution():
    H,M,DNA_list = get_test_case()
    min_dna = ''
    for i in range(M):
        alphabet_count = [0 for x in range(26)]
        for dna in DNA_list:
            ch = ord(dna[i])
            alphabet_count[ch % 65] +=1
        max_count = max(alphabet_count)
        org_ch = alphabet_count.index(max_count) + 65
        dna_char = chr(org_ch)
        min_dna += dna_char
    min_hamming_distance_sum = 0
    for dna in DNA_list:
        min_hamming_distance_sum+= get_hamming_distance(dna,min_dna,M)
    print(f"{min_dna}\n{min_hamming_distance_sum}")


if __name__ == '__main__':
    solution()
