#496. Next Greater Element I
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
        answerlist=[]
        for i in nums1:
            for j in nums2:
                if i!=j:
                    continue
                else: #i==j
                    for k in nums2[nums2.index(j)+1:]:
                        if len(nums2)-1 == nums2.index(j): #만약 j가 리스트의 마지막 요소라면:
                            answerlist.append(-1)
                            break
                        else:
                            if i<k:
                                answerlist.append(k)
                                break
                            else:
                                continue
        return answerlist
