from typing import Optional

"""
prev, current, nextのポインタをとっておく。
current.next = prevで今のノードと前のノードをつなげて逆戻りする。
事前にnextを保持する理由は、current.next = prevにすることによって、current.nextが上書きされて
たどれなくなってしまうため
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 関数を完成させてください
        if head is None: return None
        prev = None
        current = head
        next = head.next
        head.next = None # 最初のheadの部分をちぎらないと、無限ループになる

        while next:
            prev = current
            current = next
            next = current.next
            current.next = prev
        
        head1 = current

        return head1


