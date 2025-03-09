class ListNode():#Linked list를 새로 하나 만들어준다
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class Solution():
    def reverseList(self,head):
        for i in range(5):
            if not head.next==None: #head.next가 끝이라면: None return
                return None
            current = head #worker 를 만듦
            while current.next and current.next.next: #current의 다음 다음에 수가 있을떄
                current = current.next #current를 한칸 move forward
            current.next=ListNode(i) #current를 새로운 list에 넣는다
            current.next = None #current의 다음을 없애버린다
            
#뭐가 잘못된건가요
            

