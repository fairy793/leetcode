# -*- coding: utf-8 -*-
# @Author: liangmengmeng
# @Date:   2020-06-01 16:32:26
# @Desc: leetcode tips 1 映射成一个字典方便查找
class Solution(object):
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		if len(nums)<=1:
		    return False
		else:
		    index = range(len(nums))
		    dictList = dict(zip(nums,index))
		    i = 0
		    while i <len(nums):
		        if (target - nums[i] in dictList and i!=dictList[target - nums[i]]):
		            return [i,dictList[target - nums[i]]]
		        else:
		            i+=1
if __name__ == '__main__':
	object = Solution()
	nums = [2, 7, 11, 15]
	target = 9
	print(object.twoSum(nums,target))