#HOMEWORK#
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        z=0
        y=0
        list(s)
        list(t)
        if len(s)!=len(t):
            return(False)
        else:
            for i in range(len(s)):
                if s[i-1]in t:
                    if s.count(s[i-1])==t.count(s[i-1]):
                        z=z+1
            for i in range(len(t)):
                if t[i-1]in s:
                    if t.count(t[i-1])==s.count(t[i-1]):
                        y=y+1
            if z and y==len(s):
                return(True)
            else:
                return(False)
yoon=Solution()
yoon.isAnagram('aacc','ccac')
#저의 최선입니다.. ㅠ