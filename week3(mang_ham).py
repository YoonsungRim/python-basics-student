class ListNode():#Linked list를 새로 하나 만들어준다
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class Solution():
    def reverseList(self,head):
        if head.next==None:
            return head
        i=0
        current = head #worker 를 만듦
        while head:
            while current.next and current.next.next: 
                current.next=ListNode(i) 
                current.next = None
                i=i+1
            

