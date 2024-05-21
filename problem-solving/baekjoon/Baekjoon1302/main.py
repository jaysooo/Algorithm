from collections import OrderedDict

def solution():
    N = int(input())
    books = OrderedDict()
    for i in range(N):
        book = input()
        if book not in books.keys():
            books[book] = 1
        else:
            books[book] +=1
    max_v =0

    for k, v in books.items():

        if max_v < v:
            max_v = v
            max_k = k
    max_books = []
    for k,v in books.items():
        if v == max_v :
            max_books.append(k)
        #print(f"k : {k} \t v: {v}")
    if len(max_books)  > 1:
        for i in range(len(max_books)):
            for j in range(i+1,len(max_books)):
                if max_books[i] > max_books[j]:
                    tmp = max_books[i]
                    max_books[i] = max_books[j]
                    max_books[j] = tmp
    print(max_books[0])
if __name__=="__main__":
    solution()