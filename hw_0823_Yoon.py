#1791
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int: #edges = [[1,2],[5,1],[1,3],[1,4]]

        intB = edges[0][0] #1
        intC = edges[0][1] #2
        if intB in edges[1]: #[5,1]
            for i in edges[1:]:
                d= intB in i
                if d == False:
                    break
            return intB

        elif intC in edges[1]:
            for i in edges[1:]:
                e= intC in i
                if e == False:
                    break
            return intC
        
        #남은 하나는 아직 하는중이에요..