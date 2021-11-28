
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0 
        end = len(nums)-1
        mid = 0  
        while(start <= end ):
            mid = ( start + end ) //2 
            if nums[mid]==target:
                return mid
            elif nums[mid] <= target:  # search right partitiion
                start = mid+1
            else:               # search left partition
                end = mid-1

        if nums[mid] < target:
            return mid+1
        else:
            return mid

# def searchInsert(nums,target):
#     start = 0 
#     end = len(nums)-1
#     mid = 0  
#     while(start <= end ):
#         mid = ( start + end ) //2 
#         if nums[mid]==target:
#             return mid
#         elif nums[mid] <= target:  # search right partitiion
#             start = mid+1
#         else:
#             end = mid-1
    
#     if nums[mid] < target:
#         return mid+1
#     else:
#         return mid

# def main():
#     T=[1,3,5,10]
#     print(searchInsert(T,15))
    
# main()