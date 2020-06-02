# -*- coding: utf-8 -*-
# @Author: liangmengmeng
# @Date:   2020-06-02 10:22:21
# @Desc:
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        if (len(nums)<3):
        	return result
        elif (nums[0]+nums[1]>0):
        	return result
        else:
        	for i in range(len(nums)):
        		if nums[i]>0:
        			break
        		if i>0 and nums[i-1] == nums[i]:
        			continue
        		target = 0-nums[i]
        		start = i+1
        		end = len(nums)-1
        		while start <end:
        			if nums[start] + nums[end] == target:
        				result.append([nums[i],nums[start],nums[end]])
        				while start <end and nums[start] == nums[start+1]:
        					start+=1
        				while start<end and nums[end-1] == nums[end] and end <len(nums)-1:
        					end-=1
        				start+=1
        				end-=1
        				if(end>=len(nums)-1):
        					end = len(nums)-1
        			elif nums[start]+nums[end]<target:
        				start+=1
        			else:
        				end-=1
        	return result
