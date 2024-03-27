from linked_list import LinkedList, LinkedListNode
def reverse_k_groups(head, k):
    dummy = LinkedListNode(0) # initialize dummy node 
    dummy.next = head # set next pointer to head 
    pointer = dummy # set pointer equal to dummy, use for traversal 
    
    while pointer != None: # while loop runs until pointer becomes None 
        tracker = pointer # initialize tracker to pointer, keeps track of number of nodes in current group in list 
        for i in range(k): 
            if tracker == None:
                break
            tracker = tracker.next
        if tracker == None:
            break

        previous, current = LinkedList.reverse_link_list(pointer.next, k)
        LinkedList.print_list_with_forward_arrow(previous)
        
        last_node_reversed_group = pointer.next
        last_node_reversed_group.next = current
        pointer.next = previous
        pointer = last_node_reversed_group
        print('\n')
        LinkedList.print_list_with_forward_arrow(dummy.next)
    return dummy.next

def main():
    input_list = [1, 2, 3, 4, 5, 6, 7, 8]
    k = 3
    input_linked_list = LinkedList()
    input_linked_list.create_linked_list(input_list)

    print("Linked list: ", end=" ")
    LinkedList.print_list_with_forward_arrow(input_linked_list.head)
    print('\n')
    result = reverse_k_groups(input_linked_list.head, k)
    print('\n')
    LinkedList.print_list_with_forward_arrow(result)

if __name__ == '__main__':
    main()