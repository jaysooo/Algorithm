
goldBucket=[]
goldDetailBucket=[5,2,1,4,3,1]
goldBucket.append(goldDetailBucket)

def getMaxGold(bucket):
    maxGoldIdx=0
    for i,v in enumerate(bucket):
        if bucket[maxGoldIdx]<v:
            maxGoldIdx=i
    
    return maxGoldIdx

def devideBucket(bucket,idx):
    bucket_0=[]
    bucket_1=[]
    bucket_2=[]

    if (idx ==0):
        bucket_1=bucket[idx]
        bucket_2=bucket[1:]
    elif (idx == len(bucket)):
        bucket_1=bucket[idx]
        bucket_2=bucket[:len(bucket)-1]
    else:
        bucket_1=bucket[:idx-1]
        bucket_2=bucket[idx+1:]

    bucket_0.append(bucket_1)
    bucket_0.append(bucket_2)
    return bucket_0

def solution(bucket):
    