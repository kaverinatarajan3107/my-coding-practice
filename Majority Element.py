''' Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        f=floor(len(nums)/2)
        s=set(nums)
        for i in s:
            c=nums.count(i)
            if c > f:
                return i
            

        
