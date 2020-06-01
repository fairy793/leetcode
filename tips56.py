# -*- coding: utf-8 -*-
# @Author: liangmengmeng
# @Date:   2020-06-01 11:22:06
# @Desc:   合并区间 数组为2*n 思路是首先根据列表横向的第一个元素对数组进行排序，
#          然后比较第二个元素的大小

class Solution:
    def merge(self, intervals):
    	result = []
    	intervals.sort(key = lambda ele:ele[0])
    	for ele in intervals:
    		print(result)
    		if not result or ele[0] > result[-1][1]:
    			result.append(ele)
    		else:
    			result[-1][1] = max(ele[1],result[-1][1])
    	return result
    		


if __name__ == '__main__':
	intervals = [[1,3],[3,6],[5,10],[9,18]]
	object = Solution()
	print(object.merge(intervals))

