"""
implement a function to check if a linked list is a palindrome
"""


def isPalindrome(head):
    stack = []
    slow = head
    fast = head
    while fast.next.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next
    if fast.next: # odd case
        slow = slow.next
        fast = fast.next
    while slow:
        if slow.val != stack.pop():
            return False
        slow = slow.next
    return True