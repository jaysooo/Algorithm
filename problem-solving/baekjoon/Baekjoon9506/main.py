



def get_prime_numbers(n):
    numbers = []
    s = 1
    while(s < n ):
        if n % s == 0 :
            numbers += [s]
        s +=1

    return numbers



def solution():

    while(True):
        t = int(input())
        if t == -1:
            break

        result = get_prime_numbers(t)
        if sum(result) == t:
            print(f"{t} = {' + '.join(list(map(str,result)))}")
        else:
            print(f"{t} is NOT perfect.")



if __name__ == '__main__':
    solution()