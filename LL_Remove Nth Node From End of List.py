class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first=head
        second=head
        
        while n>0:
            first = first.next
            n-=1
        if first ==None:
            head=head.next
            return head
        
        while first and first.next!=None:
            first=first.next
            second = second.next
        
        second.next = second.next.next
        return head
