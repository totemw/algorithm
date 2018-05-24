class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def reverse(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

    def has_circle(self, head):
        slow = head
        fast = head
        while slow and fast:
            fast = fast.next
            slow = slow.next
            if fast:
                fast = fast.next
            if fast == slow:
                break
        if fast and slow and fast == slow:
            return True
        else:
            return False


class DListNode:
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None

    def reverse(self, head):
        curt = None
        while head:
            curt = head
            head = curt.next
            curt.next = curt.prev
            curt.prev = head
        return curt

