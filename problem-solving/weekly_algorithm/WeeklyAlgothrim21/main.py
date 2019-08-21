from itertools import compress, product


items=[4, 2, -3, -1, 0, 4]
# def combinations(items):
#     return ( set(compress(items,mask)) for mask in product(*[[0,1]]*len(items)) )


# def combine(inp):
#     return combine_helper(inp, [], [])

# def combine_helper(inp, temp, ans):
#     for i in range(len(inp)):
#         current = inp[i]
#         remaining = inp[i + 1:]
#         temp.append(current)
#         ans.append(tuple(temp))
#         combine_helper(remaining, temp, ans)
#         temp.pop()
#     return ans

def solution(inp):
    ans=set()
    for i in range(0,len(inp)+1):
        for j in range(i+1,len(inp)+1):
            if sumIsZero(inp[i:j]):
                ans.add(tuple(inp[i:j]))
    print(ans)
    
def sumIsZero(inp):
    return True if sum(inp) == 0 else False

solution(items)
