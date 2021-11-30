class Solution:
    def climbStairs(self, n: int) -> int:
        n1 = 1
        n2 = 2
        br = 3 

        if n < 3 :
            return n
        else:
            while(br <= n ):
                n3 = n1 + n2
                n1 = n2
                n2 = n3

                br +=1

            return n3
       
    
        
    