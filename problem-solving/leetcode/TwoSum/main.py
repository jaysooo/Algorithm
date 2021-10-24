

#Runtime: 60 ms, faster than 83.47% of Python3 online submissions for Two Sum.
#Memory Usage: 15.3 MB, less than 42.38% of Python3 online submissions for Two Sum.


class Solution:


    # Brute Force - 가장 단순한 접근 -> time complexity : (n2), space complexity : o(1)
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        target_indices = []

        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    target_indices+=[i,j]
                    return target_indices

        return target_indices


    # Two - pass Hash Table -> time complexity : (n), space complexity : o(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        target_indices = []
        # 자료구조를 해시 맵으로 생성
        for idx,va in enumerate(nums):
            hash_map[va]=idx
        
        # look up 
        for idx,va in enumerate(nums):
            minus_value = target - va
            if minus_value in hash_map and hash_map[minus_value] != idx:
                target_indices+=[idx,hash_map[minus_value]]        
                break
        
        return target_indices


    # One pass hash Table -> time complexity : (n), space complexity : o(n) 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}

        for idx,va in enumerate(nums):
            minus_value = target-va
            if minus_value in hash_map:
                return [idx,hash_map[minus_value]]
            
            hash_map[va]=idx

    def test(self):
        nums = [2,1,94,3,-2]
        target = 92
        result = self.twoSum(nums,target)
        print(result)



if __name__ == '__main__':
    s = Solution()
    s.test()
