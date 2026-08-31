class Solution:
    def nodesBetweenCriticalPoints(self, head: 'Optional[ListNode]') -> List[int]:
        prev = head
        cur = head.next
        idx = 1
        first_idx = -1
        prev_idx = -1
        min_dist = float('inf')
        
        while cur.next:
            if (cur.val > prev.val and cur.val > cur.next.val) or (cur.val < prev.val and cur.val < cur.next.val):
                if first_idx == -1:
                    first_idx = idx
                else:
                    min_dist = min(min_dist, idx - prev_idx)
                prev_idx = idx
            prev = cur
            cur = cur.next
            idx += 1
        
        if prev_idx == first_idx: 
            return [-1, -1]
        
        max_dist = prev_idx - first_idx
        return [min_dist, max_dist]