from linked_list import LinkedList, reverse_linked_list, print_list_with_forward_arrow

# time O(n), space O(1)
def palindrome_original(head):
    slow, fast = head, head 
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    fast = reverse_linked_list(slow)
    slow = head
    while slow and fast:
        if slow.data != fast.data:
            return False
        slow = slow.next
        fast = fast.next 
    return True

def palindome(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    revert_data = reverse_linked_list
    check = compare_two_halves(head, revert_data)
    reverse_linked_list(revert_data)
    
    if check:
        return True
    return False

def compare_two_halves(first, second):
    while first and second:
        if first.data != second.data:
            return False
        else:
            first = first.next
            second = second.next  
    return True

def main():
    input = (
                [2, 4, 6, 4, 2],
                [0, 3, 5, 5, 0],
                [9, 7, 4, 4, 7, 9],
                [5, 4, 7, 9, 4, 5],
                [5, 9, 8, 3, 8, 9, 5],
            )
    j = 1

    for i in range(len(input)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input[i])
        print(j, ".\tLinked List:", end=" ", sep="")
        print_list_with_forward_arrow(input_linked_list.head)
        head = input_linked_list.head
        print("\n\tIs it a palindrome?", "Yes" if palindome(head) else "No")
        j += 1
        print("-"*100, "\n")


if __name__ == "__main__":
    main()