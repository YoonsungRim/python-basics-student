class Solution:
    def intersection(self,li1, li2):
        a=[]
        if len(li1)<=len(li2):
            for i in range(len(li1)):
                  if li1[i] in li2:
                        if li1[i] in a:
                            continue
                        else:
                            a.append(li1[i])
        else:
            for i in range(len(li2)):
                    if li2[i] in li1:
                        if li2[i] in a:
                            continue
                        else:
                            a.append(li2[i])

        return a