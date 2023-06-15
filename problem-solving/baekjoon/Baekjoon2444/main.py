

def solution():
    N = int(input())
    space_cnt = N-1
    star_cnt = 1
    cursor = 1
    star_array = [''] * (2*N-1)

    while(cursor <= N):
        line = (' ' * space_cnt) + ('*' * star_cnt)
        star_array[cursor-1] = line
        star_array[(len(star_array)-cursor)] = line
        # print(line)
        space_cnt -= 1
        star_cnt += 2
        cursor += 1
    for i in star_array:
        print(i)


if __name__ == '__main__':
    solution()
