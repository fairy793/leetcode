# -*- coding: utf-8 -*-
# @Author: mengmengliang
# @Date:   2020-05-29 15:27:22
# @Desc:   leetcode 34题 算法思想：二分查找
class Solution(object):
	
    def searchRange(self, nums, target):
    	left = 0
    	right = len(nums)-1

    	left_index = -1
    	right_index = -1

    	if not nums:
    		return[-1,-1]

    	while left <= right:
    		mid = (left + right)//2
    		
    		if (nums[mid] < target):
    			left = mid + 1
    		elif (nums[mid] > target):
    			right = mid-1
    		else:
    			left_index = mid
    			right_index = mid
    			
    			for x in range(mid+1,right+1):
    				if (nums[x]==target):
    					right_index = x
    				else:
    					break
    
    			for y in range(mid,left-1,-1):
    				if(nums[y]==target):
    					left_index = y
    				else:
    					break
			
    			return [left_index,right_index]

        return [-1,-1]


if __name__ == '__main__':
	nums = [2,2]
	target = 2
	object = Solution ()
	print(object.searchRange(nums,target))




        