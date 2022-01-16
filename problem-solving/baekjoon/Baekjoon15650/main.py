STACK = []
VISIT = []
N,M=0,0

# 사전 순  출력. 중복 출력 X 

CACHE = {}
def input_test_case():
	input_str= input().split(" ")
	N,M = int(input_str[0]),int(input_str[1])

	return N,M
# N 4,2  / 1,2,3,4 
def combinations(NUM,CNT):
	global VISIT,STACK,N,M,CACHE
	if CNT==M:
		parsed_map = map(lambda x: str(x),STACK)
		k = "".join ( [str(x) for x in sorted(STACK)] )
		if k not in CACHE:
			print(" ".join(parsed_map))
			CACHE[k]=True
		
		return 0
		
	for i in range(1,N+1):
		if NUM == i or VISIT[(i-1)]:
			continue

		STACK.append(i)
		VISIT[i-1]=True
		combinations(i,CNT+1)
		STACK.pop()
		VISIT[(i-1)]=False

def solution():
	global VISIT,STACK,N,M 
	N,M=input_test_case()
	
	VISIT = [False]* N
	combinations(0, 0)
	
def main():
	solution()
	

main()