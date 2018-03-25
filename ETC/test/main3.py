M=5
A=[1,2,3,4,0]
N = len(A)
count = [0] * (M + 1)
maxOccurence = 0
index = -1
for i in range(N):
    if count[A[i]] > 0:
        tmp = count[A[i]]
        if tmp >= maxOccurence:
            maxOccurence = tmp
            index = i
        count[A[i]] = tmp + 1
    else:
        count[A[i]] = 1

print(index)       
print(A[index])