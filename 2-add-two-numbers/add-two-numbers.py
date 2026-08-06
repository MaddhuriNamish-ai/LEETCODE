class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = cur = ListNode()
        carry = 0
        while l1 or l2 or carry:
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry, val = divmod(s, 10)
            cur.next = ListNode(val)
            cur = cur.next
            l1 = l1 and l1.next
            l2 = l2 and l2.next
        return dummy.next