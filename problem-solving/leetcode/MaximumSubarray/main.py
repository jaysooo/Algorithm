class Solution:
    # Brute Force - 
    def get_maximum_sum(self,arr:List[int]):
        start = 0 
        end = len(arr)
        maximum_sum=arr[start]
        while(start<end):
            mid=start+1
            pre_sum=sum(arr[start:mid])
            while(mid<end):
                mid+=1
                if pre_sum < sum(arr[start:mid]):
                    pre_sum = 	sum(arr[start:mid])	
            if maximum_sum < pre_sum:
                maximum_sum=pre_sum
            start+=1

        return maximum_sum
    
    def kadane_algorithm(self,arr:List[int]):
        start = 0
        end = len(arr)
        maximum_sub_array = arr[start]
        start=0
        current_sum = 0
        while(start < end):
            current_sum = max(arr[start],current_sum+arr[start])
            if current_sum > maximum_sub_array:
                maximum_sub_array = current_sum
            start+=1

        return maximum_sub_array


    def maxSubArray(self, nums: List[int]) -> int:
        
        return self.kadane_algorithm(nums)