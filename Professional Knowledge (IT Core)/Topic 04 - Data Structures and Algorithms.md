# Topic 4: Data Structures & Algorithms

## 📝 Quick Revision Cheat Sheet (Before you start)

- **Stack:** LIFO (Last In, First Out). Operations: Push, Pop, Peek. Used in recursion, expression evaluation.
- **Queue:** FIFO (First In, First Out). Operations: Enqueue, Dequeue. Used in scheduling, BFS.
- **Linked List:** Dynamic data structure. Types: Singly, Doubly, Circular.
- **Tree:** Hierarchical structure. Binary Tree: Max 2 children. BST: Left < Root < Right.
- **Graph:** Collection of vertices and edges. Representations: Adjacency Matrix, Adjacency List.
- **Time Complexity:** Big O notation. O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2^n) < O(n!).

## Part A: Arrays & Linked Lists (Questions 1-30)


### 1. What is an array?
- A) A collection of elements of different data types
- B) A collection of elements of the same data type stored in contiguous memory
- C) A dynamic data structure
- D) A linked list

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** An array is a fixed-size collection of elements of the same type stored in contiguous memory locations.

</details>

### 2. What is the time complexity of accessing an element in an array by index?
- A) O(1)
- B) O(n)
- C) O(log n)
- D) O(n²)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Array access by index is constant time because the address is calculated directly.

</details>

### 3. What is the time complexity of inserting an element at the beginning of an array?
- A) O(1)
- B) O(n)
- C) O(log n)
- D) O(n²)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Inserting at the beginning requires shifting all existing elements, which takes O(n) time.

</details>

### 4. What is the time complexity of searching for an element in an unsorted array?
- A) O(1)
- B) O(n)
- C) O(log n)
- D) O(n²)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** In the worst case, you may need to check every element, which is O(n).

</details>

### 5. What is the time complexity of binary search on a sorted array?
- A) O(1)
- B) O(n)
- C) O(log n)
- D) O(n²)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Binary search divides the search space in half each time, resulting in O(log n).

</details>

### 6. What is a linked list?
- A) A collection of elements stored in contiguous memory
- B) A linear data structure where elements are stored in nodes with pointers
- C) A type of array
- D) A tree structure

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A linked list consists of nodes, each containing data and a pointer to the next node.

</details>

### 7. What is the main advantage of a linked list over an array?
- A) Faster access
- B) Dynamic size
- C) Less memory usage
- D) Simpler implementation

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Linked lists can grow and shrink dynamically, while arrays have a fixed size.

</details>

### 8. What is the main disadvantage of a linked list compared to an array?
- A) Dynamic size
- B) No random access
- C) More memory usage for pointers
- D) Both B and C

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** Linked lists do not allow direct random access (must traverse) and require extra memory for pointers.

</details>

### 9. In a singly linked list, each node contains:
- A) Data and a pointer to the previous node
- B) Data and a pointer to the next node
- C) Only data
- D) Only pointers

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A singly linked list node has data and a next pointer.

</details>

### 10. In a doubly linked list, each node contains:
- A) Data and a pointer to the next node
- B) Data and pointers to both previous and next nodes
- C) Only data
- D) Only pointers

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A doubly linked list node has data, a prev pointer, and a next pointer.

</details>

### 11. What is the time complexity of inserting at the beginning of a linked list?
- A) O(1)
- B) O(n)
- C) O(log n)
- D) O(n²)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Inserting at the head only requires updating a few pointers, which is O(1).

</details>

### 12. What is the time complexity of searching for an element in a linked list?
- A) O(1)
- B) O(n)
- C) O(log n)
- D) O(n²)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** You may need to traverse the entire list, which is O(n).

</details>

### 13. What is a circular linked list?
- A) A list where the last node points to the first node
- B) A list with no end
- C) A list with two heads
- D) A list with no pointers

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** In a circular linked list, the last node's next pointer points back to the head.

</details>

### 14. Which data structure is used to implement a stack?
- A) Array
- B) Linked List
- C) Both A and B
- D) Tree

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** A stack can be implemented using either an array or a linked list.

</details>

### 15. Which data structure is used to implement a queue?
- A) Array
- B) Linked List
- C) Both A and B
- D) Tree

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** A queue can be implemented using either an array or a linked list.

</details>

### 16. What is a sparse matrix?
- A) A matrix with many non-zero elements
- B) A matrix with many zero elements
- C) A matrix with all zeros
- D) A matrix with all ones

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A sparse matrix has a large number of zero elements and can be stored efficiently.

</details>

### 17. What is the time complexity of merging two sorted arrays of size n and m?
- A) O(n+m)
- B) O(n*m)
- C) O(n log n)
- D) O(m log m)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Merging two sorted arrays requires comparing elements once, which is O(n+m).

</details>

### 18. What is the time complexity of reversing an array of size n?
- A) O(1)
- B) O(n)
- C) O(log n)
- D) O(n²)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Reversing an array requires swapping elements, which takes O(n) time.

</details>

### 19. What is the space complexity of an array of size n?
- A) O(1)
- B) O(n)
- C) O(log n)
- D) O(n²)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** An array of size n requires O(n) space.

</details>

### 20. What is the main advantage of using a circular linked list?
- A) Can traverse the list from any node
- B) Faster access
- C) Less memory
- D) Simpler implementation

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** In a circular linked list, you can start from any node and traverse the entire list.

</details>

### 21. Which operation is NOT possible on an array?
- A) Insertion
- B) Deletion
- C) Dynamic resizing
- D) Access by index

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Arrays have a fixed size and cannot be dynamically resized (in most languages).

</details>

### 22. What is the time complexity of deleting the first element from a linked list?
- A) O(1)
- B) O(n)
- C) O(log n)
- D) O(n²)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Deleting the head only requires updating the head pointer, which is O(1).

</details>

### 23. What is a header linked list?
- A) A linked list with a dummy node at the beginning
- B) A linked list with no head
- C) A linked list with two heads
- D) A linked list with no tail

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A header linked list has a dummy header node that simplifies insertion and deletion operations.

</details>

### 24. What is the time complexity of finding the middle element of a linked list?
- A) O(1)
- B) O(n)
- C) O(log n)
- D) O(n²)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** You need to traverse the list to find the middle, which is O(n).

</details>

### 25. Which data structure is best for implementing a recursive algorithm?
- A) Queue
- B) Stack
- C) Array
- D) Graph

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Recursion uses the call stack implicitly, so a stack is the natural choice.

</details>

### 26. What is the time complexity of inserting at the end of a singly linked list (without a tail pointer)?
- A) O(1)
- B) O(n)
- C) O(log n)
- D) O(n²)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Without a tail pointer, you must traverse the entire list to find the end, which is O(n).

</details>

### 27. What is the time complexity of inserting at the end of a singly linked list (with a tail pointer)?
- A) O(1)
- B) O(n)
- C) O(log n)
- D) O(n²)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** With a tail pointer, you can directly access the last node and insert in O(1).

</details>

### 28. What is the space complexity of a doubly linked list with n nodes?
- A) O(1)
- B) O(n)
- C) O(log n)
- D) O(n²)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Each node stores data and two pointers, so the total space is O(n).

</details>

### 29. Which of the following is NOT a type of linked list?
- A) Singly linked list
- B) Doubly linked list
- C) Circular linked list
- D) Binary linked list

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** Binary linked list is not a standard type. The standard types are singly, doubly, and circular.

</details>

### 30. What is the time complexity of concatenating two linked lists?
- A) O(1)
- B) O(n)
- C) O(log n)
- D) O(n²)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** You need to traverse the first list to find its end, which is O(n).

</details>

## Part B: Stacks & Queues (Questions 31-60)


### 31. What is the principle of a stack?
- A) FIFO
- B) LIFO
- C) LILO
- D) Random

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A stack follows Last In, First Out (LIFO).

</details>

### 32. What is the principle of a queue?
- A) FIFO
- B) LIFO
- C) LILO
- D) Random

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A queue follows First In, First Out (FIFO).

</details>

### 33. Which operation adds an element to a stack?
- A) Push
- B) Pop
- C) Enqueue
- D) Dequeue

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Push adds an element to the top of the stack.

</details>

### 34. Which operation removes an element from a stack?
- A) Push
- B) Pop
- C) Enqueue
- D) Dequeue

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Pop removes the top element from the stack.

</details>

### 35. Which operation adds an element to a queue?
- A) Push
- B) Pop
- C) Enqueue
- D) Dequeue

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Enqueue adds an element to the rear of the queue.

</details>

### 36. Which operation removes an element from a queue?
- A) Push
- B) Pop
- C) Enqueue
- D) Dequeue

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** Dequeue removes an element from the front of the queue.

</details>

### 37. What is the time complexity of push and pop operations on a stack?
- A) O(1)
- B) O(n)
- C) O(log n)
- D) O(n²)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Push and pop on a stack are constant time operations.

</details>

### 38. What is the time complexity of enqueue and dequeue operations on a queue?
- A) O(1)
- B) O(n)
- C) O(log n)
- D) O(n²)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Enqueue and dequeue on a queue are constant time operations.

</details>

### 39. What is a circular queue?
- A) A queue where the last position is connected to the first
- B) A queue with no end
- C) A queue with two fronts
- D) A queue with no rear

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A circular queue connects the last position back to the first to efficiently use space.

</details>

### 40. What is a priority queue?
- A) A queue where elements are processed based on priority
- B) A queue where elements are processed FIFO
- C) A queue where elements are processed LIFO
- D) A queue with no order

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** In a priority queue, elements with higher priority are dequeued first.

</details>

### 41. Which data structure is used to evaluate postfix expressions?
- A) Queue
- B) Stack
- C) Array
- D) Graph

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Stacks are used to evaluate postfix (Reverse Polish) expressions.

</details>

### 42. Which data structure is used to convert infix to postfix?
- A) Queue
- B) Stack
- C) Array
- D) Graph

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Stacks are used to convert infix expressions to postfix.

</details>

### 43. What is the postfix form of A + B?
- A) AB+
- B) A+B
- C) +AB
- D) AB+

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** In postfix notation, the operator comes after the operands: AB+.

</details>

### 44. What is the prefix form of A + B?
- A) AB+
- B) +AB
- C) A+B
- D) AB+

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** In prefix notation, the operator comes before the operands: +AB.

</details>

### 45. Which data structure is used for BFS (Breadth-First Search)?
- A) Stack
- B) Queue
- C) Array
- D) Tree

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** BFS uses a queue to explore nodes level by level.

</details>

### 46. Which data structure is used for DFS (Depth-First Search)?
- A) Stack
- B) Queue
- C) Array
- D) Tree

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** DFS uses a stack (or recursion) to explore as far as possible along each branch.

</details>

### 47. What is the condition for a queue to be empty?
- A) Front = Rear
- B) Front = Rear + 1
- C) Front = NULL
- D) Rear = NULL

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** In a circular queue, an empty queue has Front = Rear.

</details>

### 48. What is the condition for a queue to be full?
- A) Front = Rear
- B) Front = (Rear + 1) % size
- C) Front = NULL
- D) Rear = NULL

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** In a circular queue, the queue is full when (Rear + 1) % size == Front.

</details>

### 49. What is a deque?
- A) Double-ended queue
- B) Double-ended stack
- C) Double queue
- D) Dual queue

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A deque (double-ended queue) allows insertion and deletion at both ends.

</details>

### 50. What is the time complexity of accessing the top element of a stack?
- A) O(1)
- B) O(n)
- C) O(log n)
- D) O(n²)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Accessing the top element (peek) is O(1).

</details>

### 51. What is the time complexity of searching for an element in a stack?
- A) O(1)
- B) O(n)
- C) O(log n)
- D) O(n²)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** To search for an element, you may need to pop all elements, which is O(n).

</details>

### 52. Which of the following is NOT an application of a stack?
- A) Function calls
- B) Undo operations
- C) Expression evaluation
- D) Job scheduling

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** Job scheduling typically uses queues, not stacks.

</details>

### 53. Which of the following is NOT an application of a queue?
- A) Printer spooling
- B) CPU scheduling
- C) Undo operations
- D) BFS

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Undo operations use stacks, not queues.

</details>

### 54. What is the time complexity of reversing a queue?
- A) O(1)
- B) O(n)
- C) O(log n)
- D) O(n²)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Reversing a queue requires processing all elements, which is O(n).

</details>

### 55. What is a priority queue implemented using?
- A) Array
- B) Linked List
- C) Heap
- D) All of the above

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** A priority queue can be implemented using arrays, linked lists, or heaps (most efficient).

</details>

### 56. What is the time complexity of inserting into a priority queue implemented as a heap?
- A) O(1)
- B) O(n)
- C) O(log n)
- D) O(n²)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Heap insertion takes O(log n) time.

</details>

### 57. What is the time complexity of deleting the minimum element from a min-heap?
- A) O(1)
- B) O(n)
- C) O(log n)
- D) O(n²)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Deleting the root (minimum) from a heap takes O(log n) time.

</details>

### 58. What is the postfix form of (A + B) * C?
- A) AB+C*
- B) ABC+*
- C) ABC+
- D) A+BC

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** (A+B) becomes AB+, then * C gives AB+C.*

</details>

### 59. What is the prefix form of (A + B) * C?
- A) +ABC
- B) +ABC
- C) AB+C
- D) A+BC

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** 

</details>

### 60. Which data structure is used to check for balanced parentheses?
- A) Queue
- B) Stack
- C) Array
- D) Graph

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A stack is used to match opening and closing parentheses.

</details>

## Part C: Trees & Graphs (Questions 61-90)


### 61. What is a tree?
- A) A linear data structure
- B) A hierarchical data structure
- C) A graph with cycles
- D) A type of array

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A tree is a hierarchical data structure with a root and child nodes.

</details>

### 62. What is the topmost node of a tree called?
- A) Leaf
- B) Root
- C) Branch
- D) Child

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The root is the topmost node of a tree.

</details>

### 63. What is a node with no children called?
- A) Root
- B) Leaf
- C) Branch
- D) Internal node

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A leaf node has no children.

</details>

### 64. What is the maximum number of children a binary tree node can have?
- A) 1
- B) 2
- C) 3
- D) Unlimited

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A binary tree node can have at most 2 children.

</details>

### 65. What is the maximum number of nodes at level L in a binary tree?
- A) 2^L
- B) 2^(L-1)
- C) L^2
- D) L

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** At level L (root at level 0), the maximum nodes is 2^L.

</details>

### 66. What is the maximum number of nodes in a binary tree of height H?
- A) 2^H
- B) 2^(H+1) - 1
- C) 2^H - 1
- D) H^2

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A binary tree of height H has at most 2^(H+1) - 1 nodes.

</details>

### 67. What is a full binary tree?
- A) Every node has 0 or 2 children
- B) Every node has 2 children
- C) Every node has 1 child
- D) Every node has 0 children

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A full binary tree has nodes with either 0 or 2 children.

</details>

### 68. What is a complete binary tree?
- A) All levels are completely filled except possibly the last, which is filled from left to right
- B) Every node has 2 children
- C) Every node has 1 child
- D) All leaves are at the same level

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A complete binary tree is filled level by level, left to right.

</details>

### 69. What is a perfect binary tree?
- A) All internal nodes have 2 children and all leaves are at the same level
- B) Every node has 1 child
- C) Every node has 0 children
- D) All nodes are at the same level

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A perfect binary tree is both full and complete, with all leaves at the same level.

</details>

### 70. What is the height of a tree with a single node?
- A) 0
- B) 1
- C) 2
- D) -1

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A tree with a single node has height 0 (if root is at level 0).

</details>

### 71. What is a binary search tree (BST)?
- A) A binary tree where left child < root < right child
- B) A binary tree where left child > root > right child
- C) A binary tree with no order
- D) A tree with 3 children

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** In a BST, the left subtree contains smaller values and the right subtree contains larger values.

</details>

### 72. What is the time complexity of searching in a balanced BST?
- A) O(1)
- B) O(n)
- C) O(log n)
- D) O(n²)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** A balanced BST has height O(log n), so search is O(log n).

</details>

### 73. What is the worst-case time complexity of searching in a BST?
- A) O(1)
- B) O(n)
- C) O(log n)
- D) O(n²)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** In a skewed BST (like a linked list), search can take O(n).

</details>

### 74. Which traversal of a BST gives sorted order?
- A) Preorder
- B) Inorder
- C) Postorder
- D) Level order

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Inorder traversal of a BST visits nodes in ascending order.

</details>

### 75. What is the order of nodes in preorder traversal?
- A) Root, Left, Right
- B) Left, Root, Right
- C) Left, Right, Root
- D) Right, Left, Root

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Preorder: Root → Left → Right.

</details>

### 76. What is the order of nodes in postorder traversal?
- A) Root, Left, Right
- B) Left, Root, Right
- C) Left, Right, Root
- D) Right, Left, Root

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Postorder: Left → Right → Root.

</details>

### 77. What is the order of nodes in inorder traversal?
- A) Root, Left, Right
- B) Left, Root, Right
- C) Left, Right, Root
- D) Right, Left, Root

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Inorder: Left → Root → Right.

</details>

### 78. What is an AVL tree?
- A) A self-balancing binary search tree
- B) A complete binary tree
- C) A full binary tree
- D) A type of heap

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** An AVL tree is a self-balancing BST where the height difference between left and right subtrees is at most 1.

</details>

### 79. What is a heap?
- A) A complete binary tree with heap property
- B) A BST
- C) A full binary tree
- D) A type of graph

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A heap is a complete binary tree where each parent is either greater (max-heap) or smaller (min-heap) than its children.

</details>

### 80. What is a graph?
- A) A collection of vertices and edges
- B) A collection of nodes
- C) A linear data structure
- D) A type of tree

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A graph consists of vertices (nodes) and edges (connections).

</details>

### 81. What is a directed graph?
- A) A graph with directed edges
- B) A graph with undirected edges
- C) A graph with no edges
- D) A graph with cycles

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** In a directed graph (digraph), edges have a direction.

</details>

### 82. What is an undirected graph?
- A) A graph with undirected edges
- B) A graph with directed edges
- C) A graph with no edges
- D) A graph with cycles

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** In an undirected graph, edges have no direction.

</details>

### 83. What is the maximum number of edges in an undirected graph with n vertices?
- A) n
- B) n(n-1)/2
- C) n(n-1)
- D) n²

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The maximum edges in an undirected graph is n(n-1)/2.

</details>

### 84. What is the maximum number of edges in a directed graph with n vertices?
- A) n
- B) n(n-1)/2
- C) n(n-1)
- D) n²

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** The maximum edges in a directed graph is n(n-1).

</details>

### 85. What is an adjacency matrix?
- A) A 2D array representing graph edges
- B) A 1D array representing vertices
- C) A linked list of edges
- D) A type of tree

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** An adjacency matrix is a 2D array where entry [i][j] indicates an edge between vertices i and j.

</details>

### 86. What is an adjacency list?
- A) An array of linked lists representing graph edges
- B) A 2D array
- C) A type of tree
- D) A matrix

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** An adjacency list stores neighbors for each vertex as a linked list.

</details>

### 87. Which graph representation is more space-efficient for sparse graphs?
- A) Adjacency Matrix
- B) Adjacency List
- C) Both are equal
- D) Neither

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Adjacency lists use O(V+E) space, while matrices use O(V²), making lists better for sparse graphs.

</details>

### 88. What is a spanning tree?
- A) A subgraph that is a tree connecting all vertices
- B) A graph with cycles
- C) A disconnected graph
- D) A type of binary tree

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A spanning tree connects all vertices with the minimum number of edges (no cycles).

</details>

### 89. What is the time complexity of BFS?
- A) O(V)
- B) O(E)
- C) O(V+E)
- D) O(V*E)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** BFS visits all vertices and edges, so it is O(V+E).

</details>

### 90. What is the time complexity of DFS?
- A) O(V)
- B) O(E)
- C) O(V+E)
- D) O(V*E)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** DFS visits all vertices and edges, so it is O(V+E).

</details>

## Part D: Algorithms & Complexity (Questions 91-115)


### 91. What is the time complexity of bubble sort in the worst case?
- A) O(n)
- B) O(n log n)
- C) O(n²)
- D) O(log n)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Bubble sort has O(n²) worst-case time complexity.

</details>

### 92. What is the time complexity of insertion sort in the best case?
- A) O(n)
- B) O(n log n)
- C) O(n²)
- D) O(log n)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Insertion sort is O(n) when the array is already sorted.

</details>

### 93. What is the time complexity of selection sort?
- A) O(n)
- B) O(n log n)
- C) O(n²)
- D) O(log n)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Selection sort always takes O(n²) time regardless of input.

</details>

### 94. What is the time complexity of merge sort?
- A) O(n)
- B) O(n log n)
- C) O(n²)
- D) O(log n)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Merge sort divides and merges, resulting in O(n log n) time.

</details>

### 95. What is the time complexity of quick sort in the worst case?
- A) O(n)
- B) O(n log n)
- C) O(n²)
- D) O(log n)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Quick sort's worst case is O(n²) when the pivot is always the smallest or largest element.

</details>

### 96. What is the time complexity of quick sort in the average case?
- A) O(n)
- B) O(n log n)
- C) O(n²)
- D) O(log n)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Quick sort's average case is O(n log n).

</details>

### 97. Which sorting algorithm is stable?
- A) Quick sort
- B) Heap sort
- C) Merge sort
- D) Selection sort

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Merge sort is stable (maintains relative order of equal elements).

</details>

### 98. Which sorting algorithm is in-place?
- A) Merge sort
- B) Quick sort
- C) Counting sort
- D) Radix sort

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Quick sort is in-place (uses O(log n) auxiliary space for recursion).

</details>

### 99. What is the time complexity of heap sort?
- A) O(n)
- B) O(n log n)
- C) O(n²)
- D) O(log n)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Heap sort takes O(n log n) time in all cases.

</details>

### 100. What is the time complexity of binary search?
- A) O(n)
- B) O(log n)
- C) O(n log n)
- D) O(1)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Binary search halves the search space each time, resulting in O(log n).

</details>

### 101. What is the time complexity of linear search?
- A) O(n)
- B) O(log n)
- C) O(n log n)
- D) O(1)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Linear search checks each element, resulting in O(n).

</details>

### 102. What is Big O notation used for?
- A) To describe the upper bound of an algorithm's time complexity
- B) To describe the lower bound
- C) To describe the exact time
- D) To describe space only

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Big O describes the worst-case (upper bound) time or space complexity.

</details>

### 103. What is the space complexity of merge sort?
- A) O(1)
- B) O(n)
- C) O(log n)
- D) O(n²)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Merge sort requires O(n) auxiliary space for merging.

</details>

### 104. What is the space complexity of quick sort?
- A) O(1)
- B) O(n)
- C) O(log n)
- D) O(n²)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Quick sort uses O(log n) space for the recursion stack.

</details>

### 105. Which algorithm is used to find the shortest path in a weighted graph?
- A) BFS
- B) DFS
- C) Dijkstra's algorithm
- D) Kruskal's algorithm

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Dijkstra's algorithm finds the shortest path from a source to all other vertices.

</details>

### 106. Which algorithm is used to find the minimum spanning tree?
- A) Dijkstra's
- B) Kruskal's
- C) Bellman-Ford
- D) Floyd-Warshall

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Kruskal's (and Prim's) algorithm finds the minimum spanning tree.

</details>

### 107. What is the time complexity of Dijkstra's algorithm using a priority queue?
- A) O(V)
- B) O(V²)
- C) O((V+E) log V)
- D) O(V*E)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** With a binary heap, Dijkstra's algorithm runs in O((V+E) log V).

</details>

### 108. What is dynamic programming?
- A) An algorithmic technique that solves problems by breaking them into overlapping subproblems
- B) A type of sorting
- C) A type of searching
- D) A data structure

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Dynamic programming stores solutions to subproblems to avoid recomputation.

</details>

### 109. Which problem is solved using dynamic programming?
- A) Fibonacci series
- B) Knapsack problem
- C) Longest Common Subsequence
- D) All of the above

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** All these problems can be solved using dynamic programming.

</details>

### 110. What is greedy algorithm?
- A) An algorithm that makes locally optimal choices at each step
- B) An algorithm that tries all possibilities
- C) An algorithm that uses recursion
- D) An algorithm that uses dynamic programming

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Greedy algorithms make the best choice at each step, hoping for a global optimum.

</details>

### 111. Which of the following is a greedy algorithm?
- A) Dijkstra's algorithm
- B) Kruskal's algorithm
- C) Prim's algorithm
- D) All of the above

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** All these algorithms use greedy strategies.

</details>

### 112. What is the time complexity of the Fibonacci sequence using recursion?
- A) O(n)
- B) O(2^n)
- C) O(n log n)
- D) O(n²)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Naive recursive Fibonacci has exponential time complexity O(2^n).

</details>

### 113. What is the time complexity of the Fibonacci sequence using dynamic programming?
- A) O(n)
- B) O(2^n)
- C) O(n log n)
- D) O(n²)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Dynamic programming reduces Fibonacci to O(n) time.

</details>

### 114. What is the time complexity of the 0/1 Knapsack problem using dynamic programming?
- A) O(n)
- B) O(nW)
- C) O(2^n)
- D) O(n²)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The DP solution for 0/1 Knapsack is O(nW), where n is items and W is capacity.

</details>

### 115. Which of the following is NOT a stable sorting algorithm?
- A) Bubble sort
- B) Insertion sort
- C) Merge sort
- D) Quick sort

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** Quick sort is not stable. Bubble, Insertion, and Merge sorts are stable.

</details>
