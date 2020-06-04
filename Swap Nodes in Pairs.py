class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        
        left = head.next.next
        newhead = head.next
        head.next.next = head
        head.next = self.swapPairs(left)
        
        return newhead
        
