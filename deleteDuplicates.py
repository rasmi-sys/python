# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        cur = head
        while cur:
            while cur.next and cur.next.val==cur.val:
                cur.next=cur.next.next
            cur=cur.next
        return head

# Build linked list: 1 -> 1 -> 2
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)

# Call function
result = Solution().deleteDuplicates(head)

# Print result
while result:
    print(result.val)
    result = result.next