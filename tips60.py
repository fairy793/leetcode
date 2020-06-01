# -*- coding: utf-8 -*-
# @Author: liangmengmeng
# @Date:   2020-06-01 11:21:49
# @Desc: leetcode 60数组的全排列
class Solution(object):
    def getPermutation(self, n, k):
    	return "".join(list(map(str,list(itertools.permutations(list(range(1,n+1))))[k-1])))

if __name__ == '__main__':
	import itertools
	print([j for j in range(1,4)])
	print(list(range(1,4)))
	print("".join(list(map(str,list(itertools.permutations(list(range(1,4))))[3]))))
	# print("".join(list(map(str,)))
