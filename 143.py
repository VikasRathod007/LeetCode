# 143. Reorder List
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def reorderList(head):
    if not head or not head.next:
        return
    slow = head
    fast = head
    stack = []
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    second = slow.next
    slow.next = None
    while second:
        stack.append(second)
        second = second.next
    current = head
    while stack:
        node = stack.pop()
        node.next = current.next
        current.next = node
        current = node.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
ReorderedList = reorderList(head)
# print(reorderList)
