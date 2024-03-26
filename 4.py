def switch_case(choice):
 if choice==1:
    print("Stack Implementation")
    stack = []
    stack.append(10)
    stack.append(20)
    stack.append(30)
    print("Before Removed Element in Stack:", stack)
    pop_element = stack.pop()
    print("Popped Element:", pop_element)
    print("After Removed Element in Stack:", stack)
 elif choice==2:
    print("Queue Implementation")
    queue = deque()
    queue.append(10)
    queue.append(20)
    queue.append(30)
    print("Before Removed Element in a Queue:", queue)
    dequeue_element = queue.popleft()
    print("Dequeued Element:", dequeue_element)
    print("After Removed Element in a Queue:", queue)
 elif choice==3:
     print("Tuple as a Sequence")
    my_tuple = (1, 2, 'a', 'b', 3.14)
    first_element = my_tuple[0]
    third_element = my_tuple[2]
    subset = my_tuple[1:4]
    new_tuple = my_tuple + ('x', 'y', 'z')
    print("Original Tuple:", my_tuple)
    print("First Element:", first_element)
    print("Subset:", subset)
    print("New Tuple:", new_tuple)
 else:
    print("Invalid choice")
    print("Python Data Structures: Stack, Queue and Tuple Implementation")
    print("1.Using list as Stack")
    print("2.Using list as Queue")
    print("3.Tuple as Sequence")
    choice=int(input("Enter your choice:"))
switch_case(choice)