# -*- coding: utf-8 -*-
# @Author: liangmengmeng
# @Date:   2020-06-01 16:39:48
# @Desc:
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tempDict = {}
        start = 0
        maxlength = 0
        for i in range(len(s)):
            if s[i] in tempDict and tempDict[s[i]]>=start:
                start = tempDict[s[i]] +1
            tempDict[s[i]] = i
            maxlength = max(maxlength,i-start+1)
            
        return maxlength
if __name__ == '__main__':
	object = Solution()
	s = "abcabcbb"
	print(object.lengthOfLongestSubstring(s))