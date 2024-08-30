import math


def sieve_of_eratosthenes(n):
    prime_numbers = [True] * (n + 1)
    p = 2
    if n == 2:
        return 1

    while (p <= int(math.sqrt(n))):
        for i in range(p * p, n + 1, p):
            prime_numbers[i] = False
        # print(i)
        p += 1
    # print(prime_numbers)

    prime_number = [p for p in range(n // 2, n + 1) if prime_numbers[p] and p > n // 2]
    # print(prime_number)
    return len(prime_number)


# def sieve_of_eratosthenes(n):
#     is_prime = [True] * (n+1)
#     p = 2

#     while ( p * p <= n):
#         if is_prime[p]:
#             for i in range(p * p, n+1,p):
#                 is_prime[i] = False
#         p += 1

#     prime_numbers = [p for p in range(2,n) if is_prime[p]]
#     return prime_numbers


# def isPrimeNumber(n):
#     isPrimeNumber=True
#     if n == 1:
#         return isPrimeNumber
#     else:
#         for i in range(2,n):
#             if n % i == 0:
#                 isPrimeNumber =False
#                 break
#         return isPrimeNumber


# def getPrimeNumberCount(n):
#     start=n
#     end=n * 2
#     count=0
#     for i in range(start+1,end+1):
#         if isPrimeNumber(i):
#             count+=1
#     return count

def main():
    while (True):
        input_str = input()
        if input_str == '0':
            break
        n = int(input_str)
        print(sieve_of_eratosthenes(2 * n))


# test()
main()