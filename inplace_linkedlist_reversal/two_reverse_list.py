from linked_list import LinkedList
from linked_list import LinkedListNode
from reverse_list import reverse
            
# time O(n), space O(1)
def reverse_between(head, left, right):
    # if list empty or left position same as right, return original list 
    if not head or left == right: 
        return head
    
    # create dummy node to handle edge case when left = 1
    dummy = LinkedListNode(0)
    dummy.next = head 
    previous = dummy 
    
    # move previous to node just before left position 
    for _ in range(left - 1):
        print("previous: ", previous.data)
        previous = previous.next
    
    # current node is node at left position 
    current = previous.next
    
    # reverse portion of list between left and right positions 
    for _ in range(right - left):
        next_node = current.next # assign next node 
        print("next_node: ", next_node.data)
        current.next = next_node.next # update current's next pointer 
        # print("current.next: ", current.next.data)
        next_node.next = previous.next 
        # print("next_node.next: ", next_node.next.data)
        previous.next = next_node
        # print("previous.next: ", previous.next.data)
    
    # return updated head of list 
    return dummy.next 

def traverse_linked_list(head):
    current, nxt = head, None
    while current:
      nxt = current.next
      current = nxt

def main():
    input_list = [
        [1, 2, 3, 4, 5, 6, 7],
        [6, 9, 3, 10, 7, 4, 6],
        [6, 9, 3, 4],
        [6, 2, 3, 6, 9],
        [6, 2]
    ]
    left = [1, 3, 2, 1, 1]
    right = [5, 6, 4, 3, 2]

    for i in range(len(input_list)):

        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input_list[i])

        print(i + 1, ".\tOriginal linked list: ", end="")
        LinkedList.print_list_with_forward_arrow(input_linked_list.head)
        print("\n\tleft:", left[i], ", right:", right[i])

        if left[i] <= 0:
            print("\n\tThe expected 'left' and 'right' to have \
            value from 1 to length of the linked list only.")
        else:
            result = reverse_between(input_linked_list.head, left[i], right[i])
            print("\n\tReversed linked list: ", end="")
            LinkedList.print_list_with_forward_arrow(result)
        print("\n", "-"*100, sep="")


if __name__ == '__main__':
    main()