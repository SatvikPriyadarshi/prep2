# Topic 1: Operating Systems

*Process, Threads, Deadlock, Memory Management, File Systems*

## 📝 Quick Revision Cheat Sheet (Before you start)

- **Process States:** New → Ready → Running → Waiting → Terminated.
- **Deadlock Conditions (Coffman Conditions):** Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait.
- **Banker's Algorithm:** Used for Deadlock Avoidance.
- **Paging:** Divides physical memory into fixed-size frames and logical memory into pages. Eliminates External Fragmentation.
- **Segmentation:** Variable-sized logical divisions. Suffers from External Fragmentation.
- **Thrashing:** High page fault rate due to insufficient frames.
- **Belady's Anomaly:** Increasing frames increases page faults (seen in FIFO, not LRU/Optimal).

## Part A: Process & Threads (Questions 1-25)


### 1. What is a process?
- A) A program stored on disk
- B) A program in execution
- C) A set of instructions
- D) A thread

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A process is an active entity, which is a program currently being executed by the CPU. A program on disk is a passive entity.

</details>

### 2. Which of the following is NOT a valid process state?
- A) Ready
- B) Running
- C) Blocked
- D) Compiled

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** The standard process states are New, Ready, Running, Waiting/Blocked, and Terminated. "Compiled" is not a state.

</details>

### 3. The PCB (Process Control Block) does NOT contain:
- A) Program Counter
- B) CPU Registers
- C) Process ID
- D) The source code of the program

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** The PCB stores process metadata (PID, state, PC, registers, memory limits, open files). The source code is stored in the program file, not the PCB.

</details>

### 4. Which scheduling algorithm is non-preemptive?
- A) Round Robin
- B) Shortest Remaining Time First
- C) First Come First Serve
- D) Preemptive Priority

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** FCFS allows a process to run until it voluntarily yields the CPU or terminates; it cannot be interrupted.

</details>

### 5. In a multi-threaded process, threads share:
- A) Stack
- B) Registers
- C) Code, Data, and Files
- D) Program Counter

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Threads share the code section, data section, and OS resources (like open files). Each thread has its own stack, registers, and program counter.

</details>

### 6. What is a context switch?
- A) Switching from user mode to kernel mode
- B) Saving the state of one process and loading the state of another
- C) Changing the priority of a process
- D) Moving a process from RAM to disk

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A context switch is the mechanism used by the OS to save the context (PCB) of a running process and restore the context of the next scheduled process.

</details>

### 7. Which is faster: Process creation or Thread creation?
- A) Process creation
- B) Thread creation
- C) Both are equal
- D) Depends on the OS

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Thread creation is faster because it does not require allocating a new memory space or copying the entire process context.

</details>

### 8. The time taken by the scheduler to decide which process to run next is called:
- A) Throughput
- B) Turnaround time
- C) Dispatch latency
- D) Waiting time

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Dispatch latency is the time taken by the dispatcher to stop one process and start another.

</details>

### 9. Which of the following is a benefit of multithreading?
- A) Increased memory usage
- B) Responsiveness
- C) Slower context switching
- D) Increased security

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Multithreading allows a program to remain responsive (e.g., a word processor can still type while a spell-check runs in the background).

</details>

### 10. Which system call is used to create a new process in UNIX?
- A) exec()
- B) fork()
- C) wait()
- D) exit()

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** fork() creates a new child process that is a duplicate of the parent process.

</details>

### 11. A process that is waiting for an I/O operation to complete is in which state?
- A) Ready
- B) Running
- C) Waiting/Blocked
- D) Terminated

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** When a process requests I/O, it cannot continue execution, so it moves to the Waiting (or Blocked) state.

</details>

### 12. Which scheduling algorithm gives the minimum average waiting time?
- A) FCFS
- B) SJF (Shortest Job First)
- C) Round Robin
- D) Priority

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** SJF is provably optimal for minimizing average waiting time, provided the burst times are known in advance.

</details>

### 13. What is the main disadvantage of FCFS scheduling?
- A) It causes starvation
- B) It has high overhead
- C) The Convoy Effect
- D) It requires preemption

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** The Convoy Effect occurs when a long CPU-bound process blocks many short I/O-bound processes behind it.

</details>

### 14. In Round Robin scheduling, what is "time quantum"?
- A) The total time a process takes to complete
- B) The maximum time a process can run before being preempted
- C) The time taken to switch contexts
- D) The time a process waits in the queue

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The time quantum is a small unit of time (typically 10-100ms) that defines the maximum execution slice for a process.

</details>

### 15. Which of the following is true about User-Level Threads (ULTs)?
- A) The OS kernel is aware of them
- B) Context switching is very fast
- C) A blocking system call blocks the entire process
- D) Both B and C

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** ULTs are managed by a library without kernel support. They switch very fast, but if one thread makes a blocking call, the whole process blocks.

</details>

### 16. Which component of the OS is responsible for selecting the next process to run?
- A) Dispatcher
- B) Scheduler
- C) Interpreter
- D) Compiler

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The CPU Scheduler selects a process from the ready queue, while the Dispatcher actually allocates the CPU to it.

</details>

### 17. What is the "idle" process?
- A) A process waiting for I/O
- B) A process that runs when no other process is ready
- C) A process with low priority
- D) A process in the ready queue

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The idle process (or idle task) runs only when the CPU has no other ready processes to execute.

</details>

### 18. Which of the following is NOT a type of thread?
- A) Kernel-level
- B) User-level
- C) Hybrid
- D) Virtual

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** Threads are generally classified as Kernel-level or User-level (and hybrid models). "Virtual threads" are not a standard OS classification.

</details>

### 19. In the context of process synchronization, a "race condition" occurs when:
- A) Two processes run at the same time
- B) Multiple processes access shared data concurrently and the outcome depends on the order of access
- C) A process runs faster than the CPU
- D) A process never terminates

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A race condition occurs when the final result depends on which process executes last in a critical section.

</details>

### 20. A semaphore is a:
- A) Integer variable
- B) Hardware register
- C) Type of process
- D) Scheduling algorithm

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A semaphore is an integer variable accessed via atomic operations (wait and signal) to manage synchronization.

</details>

### 21. Which of the following is an advantage of multi-threading?
- A) Increased resource sharing
- B) Economical (cheaper than process creation)
- C) Scalability
- D) All of the above

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** Multithreading provides all these benefits: sharing resources, lower creation overhead, and better utilization of multiprocessor systems.

</details>

### 22. The fork() system call returns 0 to:
- A) The parent process
- B) The child process
- C) Both
- D) The kernel

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** fork() returns 0 to the newly created child process and the child's PID to the parent.

</details>

### 23. Which of the following scheduling algorithms is preemptive?
- A) FCFS
- B) SJF (non-preemptive)
- C) Round Robin
- D) None of the above

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Round Robin is inherently preemptive because it forces processes to yield the CPU after the time quantum expires.

</details>

### 24. What is the "critical section" problem?
- A) A section of code that must be executed by only one process at a time
- B) A section of memory that is read-only
- C) A section of the OS that handles interrupts
- D) A section of code that causes a deadlock

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** The critical section is a piece of code where a process accesses shared resources, requiring mutual exclusion to prevent data corruption.

</details>

### 25. Which of the following is NOT a requirement for the critical section solution?
- A) Mutual Exclusion
- B) Progress
- C) Bounded Waiting
- D) Infinite Loop

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** The three requirements are Mutual Exclusion, Progress, and Bounded Waiting. Infinite Loop is a bug, not a requirement.

</details>

## Part B: Deadlocks & Synchronization (Questions 26-45)


### 26. Which of the following is NOT a necessary condition for a deadlock?
- A) Mutual Exclusion
- B) Hold and Wait
- C) Preemption
- D) Circular Wait

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** The conditions are Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait. Preemption prevents deadlocks.

</details>

### 27. Banker's Algorithm is used for:
- A) Deadlock Prevention
- B) Deadlock Avoidance
- C) Deadlock Detection
- D) Deadlock Recovery

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Banker's Algorithm is a deadlock avoidance algorithm that checks for safe states before allocating resources.

</details>

### 28. A situation where a process is repeatedly denied access to a resource is called:
- A) Deadlock
- B) Starvation
- C) Race condition
- D) Thrashing

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Starvation (or indefinite blocking) occurs when a process waits indefinitely because the scheduler keeps favoring other processes.

</details>

### 29. Which of the following is true about a deadlock?
- A) Processes are not blocked
- B) Processes are blocked waiting for each other
- C) It can be resolved by increasing CPU speed
- D) It only occurs in single-processor systems

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** In a deadlock, a set of processes are permanently blocked because each holds a resource and waits for another held by a different process in the set.

</details>

### 30. What is a "safe state" in deadlock avoidance?
- A) A state where no deadlock can occur
- B) A state where there is at least one sequence of process executions that avoids deadlock
- C) A state where all resources are allocated
- D) A state where the CPU is idle

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A safe state guarantees that there exists a safe sequence where all processes can complete without deadlocking.

</details>

### 31. Which of the following is a deadlock prevention technique?
- A) Resource ordering
- B) Banker's Algorithm
- C) Wait-for graph
- D) Timeouts

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Resource ordering prevents Circular Wait by forcing processes to request resources in a strictly increasing order.

</details>

### 32. A binary semaphore can take values:
- A) 0 and 1
- B) -1 and 0
- C) Any integer
- D) Only 1

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A binary semaphore (mutex) only takes values 0 (locked) or 1 (unlocked).

</details>

### 33. The wait() operation on a semaphore S is also known as:
- A) V operation
- B) P operation
- C) Signal operation
- D) Up operation

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Wait is called P (Proberen/Dutch for "to test"). Signal is called V (Verhogen/Dutch for "to increment").

</details>

### 34. Which of the following is NOT a method for deadlock recovery?
- A) Process termination
- B) Resource preemption
- C) Rollback
- D) Increasing memory

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** Recovery methods include aborting processes, preempting resources, and checkpoint/rollback. Increasing memory doesn't resolve a logical deadlock.

</details>

### 35. In a resource allocation graph, a cycle indicates:
- A) A deadlock is guaranteed
- B) A deadlock may exist
- C) No deadlock
- D) A safe state

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** If every resource has a single instance, a cycle means deadlock. If there are multiple instances, a cycle means a deadlock may exist.

</details>

### 36. What is the main purpose of a "Monitor" in synchronization?
- A) To increase CPU speed
- B) To provide high-level synchronization and mutual exclusion
- C) To detect deadlocks
- D) To schedule processes

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A monitor is a high-level abstraction that automatically handles mutual exclusion, making synchronization easier for programmers.

</details>

### 37. Which of the following is a classic synchronization problem?
- A) Producer-Consumer
- B) Readers-Writers
- C) Dining Philosophers
- D) All of the above

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** These are the three classic synchronization problems used to test synchronization algorithms.

</details>

### 38. In the Dining Philosophers problem, what does a philosopher represent?
- A) A resource
- B) A process
- C) A semaphore
- D) A CPU

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The philosophers represent processes, and the forks represent shared resources.

</details>

### 39. What is the main issue in the Readers-Writers problem?
- A) Readers starve
- B) Writers starve
- C) Both may starve if not handled properly
- D) Deadlock is impossible

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** If readers are always given priority, writers starve; if writers are always prioritized, readers starve. A balanced solution is needed.

</details>

### 40. Which system call is used to lock a file in UNIX?
- A) lockf()
- B) flock()
- C) Both A and B
- D) lock()

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** UNIX provides flock() and lockf() (and fcntl()) for file locking.

</details>

### 41. Which of the following is a preemptive deadlock prevention method?
- A) Hold and Wait
- B) No Preemption
- C) Circular Wait
- D) Mutual Exclusion

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** By allowing preemption of resources, you break the "No Preemption" condition, preventing deadlock.

</details>

### 42. A "spinlock" is:
- A) A blocking lock
- B) A busy-waiting lock
- C) A type of semaphore
- D) A deadlock

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A spinlock causes a thread to loop (spin) continuously while waiting for a lock to become available.

</details>

### 43. Which of the following is NOT a valid state in a resource allocation graph?
- A) Request edge
- B) Assignment edge
- C) Claim edge
- D) Release edge

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** The graph uses Request edges (P→R), Assignment edges (R→P), and Claim edges (dashed P→R).

</details>

### 44. What is the "Bounded Waiting" requirement?
- A) A process can wait indefinitely
- B) There is a bound on the number of times other processes can enter their critical section after a process has requested entry
- C) The critical section has a time limit
- D) The CPU can only wait for a fixed time

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Bounded waiting ensures that no process waits forever to enter its critical section.

</details>

### 45. Which of the following is true about a "deadlock" vs "starvation"?
- A) Deadlock is permanent, starvation may be temporary
- B) Starvation is permanent, deadlock may be temporary
- C) Both are permanent
- D) Both are temporary

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Deadlocked processes will never proceed. Starved processes might eventually proceed if scheduling changes.

</details>

## Part C: Memory Management (Questions 46-75)


### 46. What is the main purpose of memory management?
- A) To increase RAM size
- B) To allocate and deallocate memory efficiently
- C) To compile programs
- D) To schedule processes

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Memory management handles the allocation, tracking, and recycling of physical and virtual memory.

</details>

### 47. Which of the following is NOT a memory allocation technique?
- A) Contiguous allocation
- B) Paging
- C) Segmentation
- D) Compilation

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** Compilation is a translation process, not a memory allocation technique.

</details>

### 48. In paging, the physical memory is divided into:
- A) Pages
- B) Frames
- C) Segments
- D) Blocks

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Logical memory is divided into pages; physical memory is divided into frames of the same size.

</details>

### 49. What is the size of a page in paging?
- A) Always 4KB
- B) Always 1MB
- C) Power of 2
- D) Fixed by the OS and CPU architecture

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** Page size is determined by the hardware architecture (e.g., 4KB, 8KB) and is a power of 2.

</details>

### 50. Which of the following eliminates external fragmentation?
- A) Segmentation
- B) Paging
- C) Contiguous allocation
- D) Dynamic partitioning

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Paging eliminates external fragmentation because memory is allocated in fixed-size frames. It may cause internal fragmentation.

</details>

### 51. Which of the following suffers from external fragmentation?
- A) Paging
- B) Segmentation
- C) Both A and B
- D) Neither

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Segmentation uses variable-sized blocks, leading to external fragmentation (free memory scattered in small holes).

</details>

### 52. What is a TLB (Translation Lookaside Buffer)?
- A) A cache for page table entries
- B) A type of RAM
- C) A disk buffer
- D) A scheduling queue

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** TLB is a high-speed hardware cache that stores recent virtual-to-physical address translations.

</details>

### 53. What is the main purpose of virtual memory?
- A) To increase physical RAM
- B) To allow execution of processes larger than physical memory
- C) To speed up the CPU
- D) To reduce disk usage

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Virtual memory allows a process to be executed even if it is larger than the available physical memory by using disk as an extension.

</details>

### 54. Which page replacement algorithm suffers from Belady's Anomaly?
- A) LRU
- B) Optimal
- C) FIFO
- D) LFU

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** FIFO can sometimes have more page faults when more frames are allocated. LRU and Optimal do not suffer from this.

</details>

### 55. Which page replacement algorithm is theoretically optimal?
- A) FIFO
- B) LRU
- C) Optimal (OPT)
- D) Random

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** The Optimal algorithm replaces the page that will not be used for the longest time. It is impossible to implement in practice as it requires future knowledge.

</details>

### 56. What is "thrashing"?
- A) High CPU utilization
- B) High page fault rate causing low CPU utilization
- C) A type of deadlock
- D) A disk failure

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Thrashing occurs when the system spends more time paging (swapping pages in and out) than executing processes.

</details>

### 57. What is the "working set" model used for?
- A) Deadlock detection
- B) Thrashing prevention
- C) CPU scheduling
- D) File management

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The working set model tracks the set of pages a process needs in its current locality to prevent thrashing.

</details>

### 58. In a paging system, the page table maps:
- A) Logical to physical addresses
- B) Physical to logical addresses
- C) Disk to memory addresses
- D) Cache to RAM addresses

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** The page table translates the page number (logical) to the frame number (physical).

</details>

### 59. What is "internal fragmentation"?
- A) Wasted space within an allocated partition
- B) Wasted space between partitions
- C) Wasted disk space
- D) Wasted CPU cycles

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Internal fragmentation occurs when memory is allocated in fixed-size blocks, and the process doesn't use the entire block.

</details>

### 60. Which of the following is a valid page replacement algorithm?
- A) First-In-First-Out (FIFO)
- B) Least Recently Used (LRU)
- C) Optimal (OPT)
- D) All of the above

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** All three are standard page replacement algorithms.

</details>

### 61. In LRU, the page that is replaced is:
- A) The one that has been in memory the longest
- B) The one that has not been used for the longest time
- C) The one that will be used last
- D) The one with the lowest priority

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** LRU replaces the page that has not been referenced for the longest period.

</details>

### 62. What is the main advantage of virtual memory?
- A) It allows more processes to run concurrently
- B) It makes the computer faster
- C) It reduces the need for RAM
- D) It eliminates fragmentation

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** By allowing processes to be partially loaded, more processes can fit in memory, increasing multiprogramming.

</details>

### 63. What is a "page fault"?
- A) An error in the page table
- B) A reference to a page not currently in main memory
- C) A hardware failure
- D) A syntax error

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A page fault occurs when a process tries to access a page that is not currently loaded in physical RAM.

</details>

### 64. Which of the following is NOT a page replacement algorithm?
- A) FIFO
- B) LIFO
- C) LRU
- D) Optimal

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** LIFO (Last-In-First-Out) is not a standard page replacement algorithm.

</details>

### 65. The malloc() function in C allocates memory from:
- A) Stack
- B) Heap
- C) Data segment
- D) Code segment

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** malloc() dynamically allocates memory from the heap.

</details>

### 66. The free() function in C:
- A) Deallocates memory
- B) Allocates memory
- C) Clears memory
- D) Compiles memory

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** free() releases dynamically allocated memory back to the heap.

</details>

### 67. Which of the following is a contiguous memory allocation method?
- A) Paging
- B) Segmentation
- C) Fixed Partitioning
- D) Virtual Memory

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Fixed partitioning divides memory into contiguous, fixed-size partitions.

</details>

### 68. What is the main disadvantage of fixed partitioning?
- A) External fragmentation
- B) Internal fragmentation
- C) Complex implementation
- D) Slow access

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Fixed partitions are contiguous, but a process smaller than the partition leaves wasted space (internal fragmentation).

</details>

### 69. Which of the following is true about segmentation?
- A) It uses fixed-size blocks
- B) It uses variable-size blocks
- C) It eliminates fragmentation
- D) It is faster than paging

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Segmentation divides memory into logical, variable-sized segments based on the program's structure.

</details>

### 70. What is the "dirty bit" in page replacement?
- A) A bit indicating the page has been modified
- B) A bit indicating the page is clean
- C) A bit indicating the page is in cache
- D) A bit indicating the page is invalid

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** The dirty bit (modify bit) indicates that a page has been modified and must be written back to disk before being replaced.

</details>

### 71. Which page replacement algorithm is most commonly used in practice?
- A) FIFO
- B) LRU
- C) Optimal
- D) Random

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** LRU (and its approximations like Clock) is widely used because it provides good performance without requiring future knowledge.

</details>

### 72. What is "demand paging"?
- A) Loading all pages at once
- B) Loading pages only when they are needed
- C) Loading pages randomly
- D) Loading pages from cache

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Demand paging loads a page into memory only when it is referenced, reducing I/O and memory usage.

</details>

### 73. What is a "frame" in paging?
- A) A logical page
- B) A physical memory block
- C) A disk sector
- D) A CPU register

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A frame is a fixed-size block of physical memory that holds a page.

</details>

### 74. Which of the following is NOT a benefit of virtual memory?
- A) Increased multiprogramming
- B) Larger address space
- C) Faster CPU speed
- D) Efficient memory protection

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Virtual memory does not make the CPU physically faster; it improves memory utilization and process size limits.

</details>

### 75. The page table is stored in:
- A) CPU registers
- B) Main memory
- C) Cache
- D) Disk

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The page table is typically stored in main memory, with the TLB caching recently used entries.

</details>

## Part D: File Systems (Questions 76-105)


### 76. What is a file system?
- A) A program for editing files
- B) A method for storing and organizing files on storage devices
- C) A type of RAM
- D) A network protocol

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A file system manages how data is stored, retrieved, and organized on a storage medium.

</details>

### 77. Which of the following is NOT a file attribute?
- A) Name
- B) Size
- C) Type
- D) Compiler

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** File attributes include name, size, type, location, protection, and timestamps. "Compiler" is a program, not an attribute.

</details>

### 78. What is a directory?
- A) A file that contains other files
- B) A special file that stores metadata about files
- C) A type of disk
- D) A CPU register

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A directory is a special file that maps file names to their metadata (inodes).

</details>

### 79. Which of the following is a file allocation method?
- A) Contiguous
- B) Linked
- C) Indexed
- D) All of the above

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** The three main file allocation methods are Contiguous, Linked, and Indexed.

</details>

### 80. Which file allocation method suffers from external fragmentation?
- A) Contiguous
- B) Linked
- C) Indexed
- D) None

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Contiguous allocation requires files to occupy consecutive blocks, leading to external fragmentation.

</details>

### 81. Which file allocation method allows files to be stored anywhere on disk?
- A) Contiguous
- B) Linked
- C) Indexed
- D) Both B and C

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** Linked and Indexed allocation allow non-contiguous storage, eliminating external fragmentation.

</details>

### 82. What is an inode in UNIX?
- A) A file name
- B) A data structure storing file metadata
- C) A directory
- D) A disk block

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** An inode (index node) stores all metadata about a file except its name and actual data.

</details>

### 83. Which of the following is NOT stored in an inode?
- A) File size
- B) File name
- C) File permissions
- D) Disk block pointers

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The file name is stored in the directory entry, not the inode. The inode stores the metadata.

</details>

### 84. What is a "mount" operation in file systems?
- A) Deleting a file system
- B) Attaching a file system to a directory
- C) Formatting a disk
- D) Copying files

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Mounting attaches a file system to a specific directory (mount point) in the existing directory tree.

</details>

### 85. Which of the following is a journaling file system?
- A) FAT32
- B) NTFS
- C) ext3/ext4
- D) Both B and C

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** NTFS and ext3/ext4 are journaling file systems. FAT32 is not.

</details>

### 86. What is the main advantage of a journaling file system?
- A) Faster file access
- B) Quick recovery after a crash
- C) Larger file sizes
- D) Better compression

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Journaling records changes before committing them, allowing fast recovery and preventing corruption after a crash.

</details>

### 87. Which of the following is a valid file operation?
- A) Create
- B) Read
- C) Write
- D) All of the above

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** Basic file operations include create, open, read, write, seek, delete, and close.

</details>

### 88. The open() system call returns:
- A) A file descriptor
- B) The file name
- C) The file size
- D) The file content

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** open() returns a file descriptor (an integer) used for subsequent operations.

</details>

### 89. Which file system is used by default on most Linux distributions?
- A) NTFS
- B) FAT32
- C) ext4
- D) HFS+

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** ext4 is the most common default file system for Linux.

</details>

### 90. Which file system is used by Windows?
- A) NTFS
- B) ext4
- C) HFS+
- D) ZFS

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** NTFS (New Technology File System) is the primary file system for modern Windows.

</details>

### 91. What is a "block" in file systems?
- A) A logical unit of data storage
- B) A physical disk sector
- C) A file
- D) A directory

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A block is the smallest logical unit of data storage in a file system, typically 4KB.

</details>

### 92. What is a "boot block"?
- A) A block containing user data
- B) A block containing the OS bootstrap code
- C) A block for temporary files
- D) A block for system logs

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The boot block contains the initial code to load the operating system.

</details>

### 93. Which of the following is a directory structure?
- A) Single-level
- B) Two-level
- C) Tree-structured
- D) All of the above

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** Directory structures can be single-level, two-level, tree-structured, acyclic graph, or general graph.

</details>

### 94. In a tree-structured directory, a file can have:
- A) Multiple parents
- B) One parent
- C) No parent
- D) Infinite parents

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** In a tree structure, each file has exactly one parent directory.

</details>

### 95. What is an "absolute path"?
- A) A path from the current directory
- B) A path from the root directory
- C) A path from the user's home
- D) A path from the disk

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** An absolute path starts from the root directory (e.g., /home/user/file.txt).

</details>

### 96. What is a "relative path"?
- A) A path from the root
- B) A path from the current working directory
- C) A path from the disk
- D) A path from the CPU

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A relative path is interpreted relative to the current working directory.

</details>

### 97. Which of the following is NOT a file system?
- A) NTFS
- B) ext4
- C) HTTP
- D) FAT32

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** HTTP is a network protocol, not a file system.

</details>

### 98. What is "disk fragmentation"?
- A) Files stored in non-contiguous blocks
- B) Files stored in contiguous blocks
- C) Empty disk space
- D) Disk failure

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Fragmentation occurs when files are scattered across non-contiguous blocks, slowing access.

</details>

### 99. Which utility is used to defragment a disk?
- A) Disk Defragmenter
- B) Disk Cleanup
- C) Check Disk
- D) Format

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Disk Defragmenter rearranges fragmented files into contiguous blocks.

</details>

### 100. What is a "swap space"?
- A) A space for temporary files
- B) A disk area used as virtual memory
- C) A cache for CPU
- D) A network buffer

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Swap space is disk space used to hold pages that are swapped out of physical memory.

</details>

### 101. Which of the following is true about FAT32?
- A) It supports files larger than 4GB
- B) It supports files up to 4GB
- C) It is a journaling file system
- D) It is used only in Linux

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** FAT32 has a maximum file size limit of 4GB.

</details>

### 102. Which file system supports encryption and compression natively?
- A) FAT32
- B) NTFS
- C) ext2
- D) ISO 9660

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** NTFS supports native encryption (EFS) and compression.

</details>

### 103. What is the purpose of the chmod command in UNIX?
- A) Change file ownership
- B) Change file permissions
- C) Change file name
- D) Change file location

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** chmod (change mode) modifies file read, write, and execute permissions.

</details>

### 104. What is the purpose of the chown command?
- A) Change file permissions
- B) Change file owner
- C) Change file name
- D) Change file content

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** chown changes the owner and/or group of a file.

</details>

### 105. Which of the following is a valid file extension for a text file?
- A) .txt
- B) .docx
- C) .exe
- D) .jpg

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** .txt is the standard extension for plain text files.

</details>
