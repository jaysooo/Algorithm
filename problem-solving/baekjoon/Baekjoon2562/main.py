def solution():
    bucket = []
    for i in range(0,9):
        num = int(input())
        bucket +=[num]
    max_num = max(bucket)
    seq = bucket.index(max_num)+1
    print(max_num)
    print(seq)

        
solution()