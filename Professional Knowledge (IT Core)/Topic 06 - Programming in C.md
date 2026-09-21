# Topic 6: Programming in C (Previous Year Pattern)

## 📝 Quick Revision Cheat Sheet (Before you start)

- **Data Types:** int, char, float, double. Format Specifiers: %d, %c, %f, %lf.
- **Operators:** Precedence: () > [] > ++/-- > */% > +/- > Relational > Logical > Assignment.
- **Pointers:** Stores memory address. * dereferences. & gives address.
- **Arrays:** Contiguous memory. Zero-indexed.
- **Functions:** Call by value (copy) vs Call by reference (pointer).

## Part A: C Fundamentals (Questions 1-25)


### 1. Which of the following is NOT a valid C data type?
- A) int
- B) float
- C) string
- D) char

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** C does not have a built-in string data type. Strings are represented as character arrays.

</details>

### 2. What is the correct format specifier for a float in C?
- A) %d
- B) %f
- C) %c
- D) %s

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** %f is used for float, %lf for double, %d for int, %c for char.

</details>

### 3. What is the size of an int in C (typically on a 32-bit system)?
- A) 1 byte
- B) 2 bytes
- C) 4 bytes
- D) 8 bytes

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** On most 32-bit and 64-bit systems, int is 4 bytes.

</details>

### 4. What is the size of a char in C?
- A) 1 byte
- B) 2 bytes
- C) 4 bytes
- D) 8 bytes

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** char is always 1 byte (8 bits) in C.

</details>

### 5. Which keyword is used to define a constant in C?
- A) const
- B) constant
- C) final
- D) static

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** The const keyword makes a variable read-only.

</details>

### 6. Which of the following is a valid variable name in C?
- A) 1stVariable
- B) _variable
- C) variable-1
- D) variable 1

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Variable names can start with underscore or letter, but not digits or special symbols (except underscore).

</details>

### 7. What is the output of printf("%d", 10/3);?
- A) 3.33
- B) 3
- C) 4
- D) 0

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Integer division truncates the decimal part, so 10/3 = 3.

</details>

### 8. What is the output of printf("%d", 10%3);?
- A) 1
- B) 3
- C) 3.33
- D) 0

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** The modulo operator returns the remainder: 10 % 3 = 1.

</details>

### 9. Which operator is used to access the value at a pointer address?
- A) &
- B) *
- C) ->
- D) .

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The dereference operator () accesses the value at a pointer address.*

</details>

### 10. Which operator returns the address of a variable?
- A) *
- B) &
- C) ->
- D) .

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The address-of operator (&) returns the memory address of a variable.

</details>

### 11. What is the correct way to declare a pointer to an integer?
- A) int ptr;
- B) int *ptr;
- C) int ptr;
- D) ptr int;

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** int *ptr; declares a pointer to an integer.

</details>

### 12. What does sizeof() return?
- A) The value of a variable
- B) The size of a variable/type in bytes
- C) The address of a variable
- D) The type of a variable

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** sizeof() returns the size in bytes of the operand.

</details>

### 13. Which header file is required for printf() and scanf()?
- A) stdlib.h
- B) stdio.h
- C) string.h
- D) math.h

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** stdio.h (standard input/output) contains printf and scanf.

</details>

### 14. What is the output of printf("%d", 5 + 3 * 2);?
- A) 16
- B) 11
- C) 13
- D) 10

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Multiplication has higher precedence: 5 + (32) = 5 + 6 = 11.*

</details>

### 15. Which of the following is a valid escape sequence?
- A) \n
- B) \t
- C) \
- D) All of the above

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** \n (newline), \t (tab), \ (backslash) are all valid escape sequences.

</details>

### 16. What is the output of printf("%c", 'A' + 1);?
- A) A
- B) B
- C) 66
- D) 65

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** 'A' has ASCII value 65. 65 + 1 = 66, which is 'B'.

</details>

### 17. Which keyword is used to define a function that doesn't return any value?
- A) int
- B) void
- C) null
- D) empty

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** void indicates no return value.

</details>

### 18. What is the correct syntax for a for loop?
- A) for(init; condition; increment)
- B) for(init, condition, increment)
- C) for(init condition increment)
- D) for{init; condition; increment}

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** for(initialization; condition; increment/decrement).

</details>

### 19. What is the output of printf("%d", 5 && 0);?
- A) 1
- B) 0
- C) 5
- D) Error

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Logical AND (&&) returns 1 only if both operands are non-zero. Here 5 && 0 = 0.

</details>

### 20. What is the output of printf("%d", 5 || 0);?
- A) 1
- B) 0
- C) 5
- D) Error

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Logical OR (||) returns 1 if at least one operand is non-zero. Here 5 || 0 = 1.

</details>

### 21. Which of the following is a valid comment in C?
- A) // comment
- B) /* comment */
- C) Both A and B
- D) # comment

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** C supports both single-line (//) and multi-line (/ /) comments.

</details>

### 22. What is the output of printf("%d", 10 > 5);?
- A) 10
- B) 5
- C) 1
- D) 0

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Relational operators return 1 (true) or 0 (false). 10 > 5 is true, so 1.

</details>

### 23. Which function is used to read a string in C?
- A) scanf()
- B) gets() (deprecated) or fgets()
- C) printf()
- D) puts()

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** gets() (deprecated) and fgets() are used to read strings.

</details>

### 24. What is the output of printf("%d", sizeof(char));?
- A) 0
- B) 1
- C) 2
- D) 4

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** char is always 1 byte.

</details>

### 25. Which of the following is NOT a valid loop in C?
- A) for
- B) while
- C) do-while
- D) repeat-until

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** repeat-until is not a C loop construct. C has for, while, and do-while.

</details>

## Part B: Pointers & Arrays (Questions 26-50)


### 26. What is the output of int arr[] = {1,2,3}; printf("%d", *arr);?
- A) 1
- B) 2
- C) 3
- D) Address of arr

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** *arr is equivalent to arr[0], which is 1.

</details>

### 27. What is the output of int arr[] = {1,2,3}; printf("%d", *(arr+1));?
- A) 1
- B) 2
- C) 3
- D) Address of arr

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** *(arr+1) is equivalent to arr[1], which is 2.

</details>

### 28. In C, the name of an array is essentially:
- A) A variable
- B) A pointer to the first element
- C) A constant value
- D) A function

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The array name decays into a pointer to the first element.

</details>

### 29. What is the output of int a = 5; int *p = &a; printf("%d", *p);?
- A) Address of a
- B) 5
- C) 0
- D) Error

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** *p dereferences the pointer, giving the value of a (5).

</details>

### 30. What is the output of int a = 5; int *p = &a; *p = 10; printf("%d", a);?
- A) 5
- B) 10
- C) 0
- D) Error

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Changing *p changes the value of a to 10.

</details>

### 31. What is a NULL pointer?
- A) A pointer that points to nothing
- B) A pointer that points to address 0
- C) Both A and B
- D) A pointer with garbage value

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** A NULL pointer points to nothing (address 0) and is used to indicate no valid address.

</details>

### 32. What is the output of printf("%d", sizeof(int*));?
- A) 2
- B) 4
- C) 8
- D) Depends on the system architecture

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** Pointer size depends on the architecture (4 bytes on 32-bit, 8 bytes on 64-bit).

</details>

### 33. Which of the following declares an array of 10 integers?
- A) int arr[10];
- B) int arr;
- C) int arr(10);
- D) array int[10];

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** int arr[10]; declares an array of 10 integers.

</details>

### 34. What is the index of the first element in a C array?
- A) 1
- B) 0
- C) -1
- D) Depends on the declaration

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** C arrays are zero-indexed, so the first element is at index 0.

</details>

### 35. What is the output of int arr[3] = {1,2,3}; printf("%d", arr[3]);?
- A) 3
- B) Garbage value
- C) 0
- D) Error

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Accessing out-of-bounds memory gives a garbage value (undefined behavior).

</details>

### 36. What is a pointer to a pointer?
- A) A pointer that points to another pointer
- B) A pointer that points to itself
- C) A null pointer
- D) A void pointer

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** int **pp; is a pointer to a pointer to an int.

</details>

### 37. What is the output of char str[] = "Hello"; printf("%c", str[1]);?
- A) H
- B) e
- C) l
- D) o

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** str[0] = 'H', str[1] = 'e', so output is 'e'.

</details>

### 38. What is the output of char str[] = "Hello"; printf("%s", str);?
- A) H
- B) Hello
- C) ello
- D) Error

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** %s prints the entire string "Hello".

</details>

### 39. What is the output of printf("%d", strlen("Hello"));?
- A) 4
- B) 5
- C) 6
- D) 7

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** strlen() returns the number of characters excluding the null terminator: 5.

</details>

### 40. What is the output of printf("%d", sizeof("Hello"));?
- A) 4
- B) 5
- C) 6
- D) 7

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** sizeof() includes the null terminator: 5 + 1 = 6.

</details>

### 41. Which function is used to copy a string in C?
- A) strcpy()
- B) strcat()
- C) strcmp()
- D) strlen()

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** strcpy(dest, src) copies src to dest.

</details>

### 42. Which function is used to concatenate strings?
- A) strcpy()
- B) strcat()
- C) strcmp()
- D) strlen()

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** strcat(dest, src) appends src to dest.

</details>

### 43. Which function is used to compare strings?
- A) strcpy()
- B) strcat()
- C) strcmp()
- D) strlen()

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** strcmp() compares two strings and returns 0 if equal.

</details>

### 44. What is the output of printf("%d", strcmp("abc", "abc"));?
- A) 0
- B) 1
- C) -1
- D) Error

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** strcmp returns 0 when strings are equal.

</details>

### 45. What is the output of int arr[5]; printf("%d", arr[0]);?
- A) 0
- B) Garbage value
- C) 5
- D) Error

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Uninitialized array elements contain garbage values.

</details>

### 46. Which of the following is a valid way to initialize an array?
- A) int arr[] = {1,2,3};
- B) int arr[3] = {1,2,3};
- C) int arr[3] = {1,2};
- D) All of the above

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** All are valid. C initializes remaining elements to 0.

</details>

### 47. What is the output of int arr[3] = {1,2}; printf("%d", arr[2]);?
- A) 2
- B) 0
- C) Garbage
- D) Error

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Remaining elements are initialized to 0.

</details>

### 48. What is a void pointer?
- A) A pointer that can point to any data type
- B) A pointer that points to nothing
- C) A null pointer
- D) A pointer to void function

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** void * is a generic pointer that can hold the address of any data type.

</details>

### 49. What is the output of int a = 10; int *p = &a; printf("%d", *p + 5);?
- A) 10
- B) 15
- C) 5
- D) Error

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** *p is 10, so 10 + 5 = 15.

</details>

### 50. What is the output of int arr[] = {1,2,3,4,5}; printf("%d", *(arr+3));?
- A) 3
- B) 4
- C) 5
- D) Error

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** *(arr+3) is arr[3], which is 4 (0-indexed: 1,2,3,4,5).

</details>

## Part C: Functions & Recursion (Questions 51-75)


### 51. What is a function in C?
- A) A block of code that performs a specific task
- B) A variable
- C) A data type
- D) An operator

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A function is a reusable block of code designed to perform a specific task.

</details>

### 52. What is the correct way to declare a function?
- A) return_type function_name(parameters);
- B) function_name(return_type parameters);
- C) return_type function_name;
- D) function function_name(parameters);

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** return_type function_name(parameter_list).

</details>

### 53. What is a function prototype?
- A) A declaration of a function before its use
- B) A definition of a function
- C) A call to a function
- D) A return statement

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A function prototype tells the compiler about the function's return type and parameters before it is defined.

</details>

### 54. What is recursion?
- A) A function calling itself
- B) A function calling another function
- C) A loop
- D) A variable

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Recursion is a technique where a function calls itself to solve a smaller subproblem.

</details>

### 55. What is the base condition in recursion?
- A) The condition that stops recursion
- B) The condition that starts recursion
- C) The condition that continues recursion
- D) The condition that returns a value

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** The base case stops the recursion to prevent infinite calls.

</details>

### 56. What is the output of a recursive function without a base case?
- A) 0
- B) 1
- C) Infinite recursion (stack overflow)
- D) Compilation error

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Without a base case, recursion continues until stack overflow.

</details>

### 57. What is the output of int fact(int n) { if(n<=1) return 1; return n * fact(n-1); } fact(4);?
- A) 4
- B) 12
- C) 24
- D) 1

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** 4! = 4 * 3 * 2 * 1 = 24.

</details>

### 58. What is the output of int fib(int n) { if(n<=1) return n; return fib(n-1) + fib(n-2); } fib(5);?
- A) 3
- B) 5
- C) 8
- D) 13

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Fibonacci sequence: 0,1,1,2,3,5,8... fib(5) = 5.

</details>

### 59. What is call by value?
- A) Passing a copy of the value to the function
- B) Passing the address of the value
- C) Passing the reference
- D) Passing a pointer

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Call by value passes a copy, so changes inside the function do not affect the original.

</details>

### 60. What is call by reference?
- A) Passing the address of the variable
- B) Passing a copy of the variable
- C) Passing a constant
- D) Passing a pointer to a function

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Call by reference passes the address, allowing the function to modify the original variable.

</details>

### 61. What is the output of void swap(int *a, int *b) { int t = *a; *a = *b; *b = t; } int x=1, y=2; swap(&x, &y); printf("%d %d", x, y);?
- A) 1 2
- B) 2 1
- C) 1 1
- D) 2 2

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Call by reference swaps the values: x=2, y=1.

</details>

### 62. What is the output of void swap(int a, int b) { int t = a; a = b; b = t; } int x=1, y=2; swap(x, y); printf("%d %d", x, y);?
- A) 1 2
- B) 2 1
- C) 1 1
- D) 2 2

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Call by value does not change the original values: x=1, y=2.

</details>

### 63. What is the return type of a function that doesn't return anything?
- A) int
- B) void
- C) null
- D) empty

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** void indicates no return value.

</details>

### 64. What is a function with no parameters called?
- A) Void function
- B) Parameterless function
- C) Null function
- D) Empty function

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A function with no parameters is called a parameterless function.

</details>

### 65. What is the output of printf("%d", add(2,3)); if int add(int a, int b) { return a+b; }?
- A) 2
- B) 3
- C) 5
- D) Error

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** 2 + 3 = 5.

</details>

### 66. What is the main function in C?
- A) The entry point of the program
- B) A helper function
- C) A library function
- D) A user-defined function

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** main() is where program execution begins.

</details>

### 67. What is the output of printf("%d", main());?
- A) 0
- B) 1
- C) Compilation error
- D) Runtime error

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** main() returns 0 by default in C99, though calling main recursively is not recommended.

</details>

### 68. What is a static function?
- A) A function that can only be called within the file it is defined
- B) A function that can be called anywhere
- C) A function that returns a static value
- D) A function that is private

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Static functions have file scope and cannot be accessed from other files.

</details>

### 69. What is an inline function?
- A) A function that is expanded at the call site
- B) A function that is defined inside another function
- C) A function that is static
- D) A function that is recursive

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Inline functions are expanded at compile time to reduce function call overhead.

</details>

### 70. What is the output of int f() { static int x = 0; x++; return x; } f(); f(); printf("%d", f());?
- A) 1
- B) 2
- C) 3
- D) 0

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Static variables retain their value between function calls. x becomes 3 after three calls.

</details>

### 71. What is the output of int f() { int x = 0; x++; return x; } f(); f(); printf("%d", f());?
- A) 1
- B) 2
- C) 3
- D) 0

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Local variables are reinitialized on each call, so x is always 1.

</details>

### 72. What is the purpose of return in a function?
- A) To return a value and exit the function
- B) To start the function
- C) To pause the function
- D) To loop the function

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** return exits the function and optionally returns a value.

</details>

### 73. What is the output of printf("%d", strlen(""));?
- A) 0
- B) 1
- C) -1
- D) Error

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** An empty string has 0 characters.

</details>

### 74. What is the output of printf("%d", sizeof(int));?
- A) 1
- B) 2
- C) 4
- D) 8

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** On most systems, int is 4 bytes.

</details>

### 75. What is the output of printf("%d", 10 == 10);?
- A) 1
- B) 0
- C) 10
- D) Error

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** The equality operator returns 1 (true).

</details>

## Part D: Control Structures & Preprocessor (Questions 76-110)


### 76. Which loop is guaranteed to execute at least once?
- A) for
- B) while
- C) do-while
- D) None

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** The do-while loop checks the condition after executing the body.

</details>

### 77. What is the output of int i=0; while(i<3) { printf("%d", i); i++; }?
- A) 0 1 2
- B) 1 2 3
- C) 0 1 2 3
- D) 1 2

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** i starts at 0 and increments until 3 (0,1,2).

</details>

### 78. What is the output of int i=0; do { printf("%d", i); i++; } while(i<3);?
- A) 0 1 2
- B) 1 2 3
- C) 0 1 2 3
- D) 1 2

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Same output as while loop in this case (0,1,2).

</details>

### 79. What is the output of for(int i=0; i<5; i++) { if(i==3) break; printf("%d", i); }?
- A) 0 1 2
- B) 0 1 2 3
- C) 0 1 2 3 4
- D) 3 4

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** break exits the loop when i==3, so 0,1,2 are printed.

</details>

### 80. What is the output of for(int i=0; i<5; i++) { if(i==3) continue; printf("%d", i); }?
- A) 0 1 2 3 4
- B) 0 1 2 4
- C) 0 1 2 3
- D) 3

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** continue skips i==3, so 0,1,2,4 are printed.

</details>

### 81. What is the output of int i=0; for(; i<3; ) { printf("%d", i); i++; }?
- A) 0 1 2
- B) 1 2 3
- C) 0 1 2 3
- D) Error

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** The init and increment parts are optional; i is initialized outside and incremented inside.

</details>

### 82. What is the output of switch(2) { case 1: printf("One"); case 2: printf("Two"); case 3: printf("Three"); }?
- A) One
- B) Two
- C) TwoThree
- D) Three

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Without break, execution falls through to subsequent cases.

</details>

### 83. What is the output of switch(2) { case 1: printf("One"); break; case 2: printf("Two"); break; case 3: printf("Three"); break; }?
- A) One
- B) Two
- C) TwoThree
- D) Three

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** break stops fall-through, so only "Two" is printed.

</details>

### 84. Which directive is used to include a header file?
- A) #include
- B) #define
- C) #ifdef
- D) #ifndef

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** #include includes header files.

</details>

### 85. Which directive is used to define a macro?
- A) #include
- B) #define
- C) #ifdef
- D) #ifndef

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** #define creates macros.

</details>

### 86. What is the output of #define SQ(x) x*x; printf("%d", SQ(3+1));?
- A) 16
- B) 7
- C) 4
- D) 10

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Macro expansion: 3+13+1 = 3+3+1 = 7 (not 16).*

</details>

### 87. What is the output of #define SQ(x) (x)*(x); printf("%d", SQ(3+1));?
- A) 16
- B) 7
- C) 4
- D) 10

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** With parentheses: (3+1)(3+1) = 44 = 16.

</details>

### 88. Which preprocessor directive is used for conditional compilation?
- A) #ifdef
- B) #ifndef
- C) #if
- D) All of the above

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** #ifdef, #ifndef, and #if are all used for conditional compilation.

</details>

### 89. What is the output of #include <stdio.h> int main() { printf("Hello"); return 0; }?
- A) Hello
- B) hello
- C) HELLO
- D) Error

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Prints "Hello".

</details>

### 90. What is the output of printf("%d", 5/2);?
- A) 2.5
- B) 2
- C) 3
- D) 0

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Integer division: 5/2 = 2 (truncated).

</details>

### 91. What is the output of printf("%f", 5.0/2);?
- A) 2.5
- B) 2
- C) 3
- D) 0

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Float division: 5.0/2 = 2.5.

</details>

### 92. Which operator is used for bitwise AND?
- A) &&
- B) &
- C) |
- D) ||

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** & is bitwise AND. && is logical AND.

</details>

### 93. Which operator is used for bitwise OR?
- A) ||
- B) |
- C) &
- D) &&

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** | is bitwise OR. || is logical OR.

</details>

### 94. What is the output of printf("%d", 5 & 3);?
- A) 1
- B) 7
- C) 8
- D) 2

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** 5 (101) & 3 (011) = 001 = 1.

</details>

### 95. What is the output of printf("%d", 5 | 3);?
- A) 1
- B) 7
- C) 8
- D) 2

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** 5 (101) | 3 (011) = 111 = 7.

</details>

### 96. What is the output of printf("%d", 5 ^ 3);?
- A) 1
- B) 7
- C) 6
- D) 2

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** 5 (101) ^ 3 (011) = 110 = 6.

</details>

### 97. What is the output of printf("%d", ~5);?
- A) -6
- B) 6
- C) -5
- D) 5

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Bitwise NOT of 5 is -6 (two's complement).

</details>

### 98. What is the output of printf("%d", 5 << 1);?
- A) 10
- B) 5
- C) 2
- D) 20

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Left shift by 1 multiplies by 2: 5 * 2 = 10.

</details>

### 99. What is the output of printf("%d", 5 >> 1);?
- A) 10
- B) 5
- C) 2
- D) 20

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Right shift by 1 divides by 2: 5 / 2 = 2.

</details>

### 100. What is the output of printf("%d", 5, 6);?
- A) 5
- B) 6
- C) 5 6
- D) Error

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** printf ignores extra arguments if there are no format specifiers.

</details>

### 101. What is the output of printf("%d %d", 5);?
- A) 5 5
- B) 5 Garbage
- C) 5 0
- D) Error

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The second %d has no corresponding argument, resulting in a garbage value.

</details>

### 102. What is the output of int x = 10; printf("%d", x++);?
- A) 10
- B) 11
- C) 9
- D) Error

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Post-increment returns the original value (10), then increments x to 11.

</details>

### 103. What is the output of int x = 10; printf("%d", ++x);?
- A) 10
- B) 11
- C) 9
- D) Error

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Pre-increment increments x to 11, then returns 11.

</details>

### 104. What is the output of int x = 10; printf("%d", x--);?
- A) 10
- B) 9
- C) 11
- D) Error

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Post-decrement returns 10, then decrements x to 9.

</details>

### 105. What is the output of int x = 10; printf("%d", --x);?
- A) 10
- B) 9
- C) 11
- D) Error

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Pre-decrement decrements x to 9, then returns 9.

</details>

### 106. What is the output of printf("%d", 5 > 3 ? 10 : 20);?
- A) 5
- B) 3
- C) 10
- D) 20

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Ternary operator: 5 > 3 is true, so returns 10.

</details>

### 107. What is the output of printf("%d", 5 < 3 ? 10 : 20);?
- A) 5
- B) 3
- C) 10
- D) 20

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** 5 < 3 is false, so returns 20.

</details>

### 108. What is the output of printf("%s", "Hello" "World");?
- A) Hello
- B) World
- C) HelloWorld
- D) Error

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Adjacent string literals are concatenated: "Hello" "World" = "HelloWorld".

</details>

### 109. What is the output of printf("%d", sizeof(5.5));?
- A) 4
- B) 8
- C) 2
- D) Error

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** 5.5 is a double literal, which is 8 bytes.

</details>

### 110. What is the output of printf("%d", sizeof(5.5f));?
- A) 4
- B) 8
- C) 2
- D) Error

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** 5.5f is a float literal, which is 4 bytes.

</details>
