# -*- coding: utf-8 -*-
# @Author: liangmengmeng
# @Date:   2020-05-29 17:53:44
# @Desc:  leetcoode 58题 easy 字符串的分割

def lengthOfLastWord(s):
        """
        :type s: str
        :rtype: int
        """
        wordlist = s.split()
        if wordlist:
            return len(wordlist[-1])
        return 0



if __name__ == '__main__':
	s = "Hello world"
	print(lengthOfLastWord(s))
