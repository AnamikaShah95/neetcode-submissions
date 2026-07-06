class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next
            
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
            
        curr = head
        dummy = Node(0)
        copy_curr = dummy
        
        while curr:
            copy_curr.next = curr.next
            copy_curr = copy_curr.next
            
            curr.next = curr.next.next
            curr = curr.next
            
        return dummy.next