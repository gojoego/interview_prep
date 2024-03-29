from linked_list import LinkedList, LinkedListNode
# time O(n), space O(1)
def reverse_k_groups(head, k):
    dummy = LinkedListNode(0) # initialize dummy node 
    dummy.next = head # set next pointer to head 
    pointer = dummy # set pointer equal to dummy, use for traversal 
    
    while pointer != None: # while loop runs until pointer becomes None 
        print("\tIdentifying a group of", k, "nodes:")
        print("\t\tptr:", pointer.data)
        
        tracker = pointer # initialize tracker to pointer, keeps track of number of nodes in current group in list 
        
        print("\t\tCurrent group: ", end = "")
        
        # traverse k nodes to check if there are enough nodes to reverse 
        for i in range(k): 
            if tracker == None:
                break
            tracker = tracker.next
            print(tracker.data, end = " ") if tracker else print("", end = "")

        # if there are not enough nodes to reverse, break out of loop 
        if tracker == None:
            print("\n\t\tThe above group contains less than", k, "nodes, so we can't reverse it.\n")
            break
        
        print("\n\t\tThe above group of",k,"nodes can be reversed.\n")
        print("\tReversing the current group of", k, "nodes:") 
        
        previous, current = LinkedList.reverse_link_list(pointer.next, k) # reverse current group of k nodes
        
        print("\t\tReversed group: ", end = "")
        
        LinkedList.print_list_with_forward_arrow(previous)
        
        # connect reversed group to rest of linked list 
        last_node_reversed_group = pointer.next
        last_node_reversed_group.next = current
        pointer.next = previous
        pointer = last_node_reversed_group
        print("\t\t", end = "")
        LinkedList.print_list_with_forward_arrow(dummy.next)
        
        print("\n\n")
    
    return dummy.next

def main():
    input_list = [[1, 2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 2, 8, 7, 7], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7], [1]]
    k = [3, 2, 1, 7, 1]

    for i in range(len(input_list)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input_list[i])

        print(i + 1, ".\tLinked list: ", end=" ")
        LinkedList.print_list_with_forward_arrow(input_linked_list.head)
        print('\n')
        result = reverse_k_groups(input_linked_list.head, k[i])
        print("\tReversed linked list: ", end=" ")
        LinkedList.print_list_with_forward_arrow(result)
        print("\n")
        print('-'*100)

if __name__ == '__main__':
    main()