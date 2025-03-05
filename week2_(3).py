class Solution:
    def isAnagram(self,s,t):
        a={}
        s='hello'
        t='eholl'
        c=0
        if len(s)!=len(t):
            print(False)
        else:
            for i in range(len(s)):
                a[i]=s[i]
            for e in range(len(t)):
                if a.get(e) in s:
                    c+=1
            if c==len(s):
                print(True)
            else:
                print(False)