# Topic 5: Object-Oriented Programming (OOPs) Concepts

## 📝 Quick Revision Cheat Sheet (Before you start)

- **Four Pillars of OOPs:** Encapsulation, Abstraction, Inheritance, Polymorphism.
- **Class vs Object:** Class is a blueprint; Object is an instance.
- **Inheritance Types:** Single, Multiple, Multilevel, Hierarchical, Hybrid.
- **Polymorphism:** Compile-time (Overloading) vs Runtime (Overriding).
- **Access Specifiers:** Private, Protected, Public.
- **Constructor:** Special method to initialize objects. Destructor: Cleans up objects.

## Part A: Basic OOPs Concepts (Questions 1-30)


### 1. What is Object-Oriented Programming (OOP)?
- A) A programming paradigm based on functions
- B) A programming paradigm based on objects and classes
- C) A programming language
- D) A database model

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** OOP organizes software design around data, or objects, rather than functions and logic.

</details>

### 2. What is a class?
- A) An instance of an object
- B) A blueprint or template for creating objects
- C) A function
- D) A variable

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A class defines the properties (attributes) and behaviors (methods) that objects of that type will have.

</details>

### 3. What is an object?
- A) A blueprint for a class
- B) An instance of a class
- C) A function
- D) A data type

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** An object is a specific instance created from a class, with its own state and behavior.

</details>

### 4. What is encapsulation?
- A) Hiding implementation details and exposing only necessary interfaces
- B) Inheriting properties from a parent class
- C) Creating multiple objects
- D) Overloading methods

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Encapsulation bundles data and methods together and restricts direct access to some components.

</details>

### 5. What is abstraction?
- A) Hiding complex implementation details and showing only essential features
- B) Creating objects
- C) Inheriting methods
- D) Overloading operators

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Abstraction focuses on what an object does rather than how it does it.

</details>

### 6. What is inheritance?
- A) Creating multiple objects
- B) Acquiring properties and behaviors from a parent class
- C) Hiding data
- D) Overloading methods

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Inheritance allows a child class to inherit attributes and methods from a parent class.

</details>

### 7. What is polymorphism?
- A) The ability of an object to take many forms
- B) Hiding data
- C) Creating classes
- D) Inheriting from multiple classes

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Polymorphism allows the same method or operator to behave differently based on the context.

</details>

### 8. Which of the following is NOT a pillar of OOPs?
- A) Encapsulation
- B) Inheritance
- C) Compilation
- D) Polymorphism

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Compilation is a process, not an OOP pillar. The four pillars are Encapsulation, Abstraction, Inheritance, and Polymorphism.

</details>

### 9. What is a constructor?
- A) A method that destroys objects
- B) A special method that initializes objects
- C) A method that inherits properties
- D) A method that hides data

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A constructor is automatically called when an object is created to initialize its state.

</details>

### 10. What is a destructor?
- A) A method that initializes objects
- B) A special method that cleans up when an object is destroyed
- C) A method that inherits properties
- D) A method that hides data

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A destructor is called when an object goes out of scope or is explicitly deleted.

</details>

### 11. Can a class have multiple constructors?
- A) Yes, through constructor overloading
- B) No, only one constructor is allowed
- C) Yes, but only in C++
- D) Depends on the language

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Constructor overloading allows multiple constructors with different parameter lists .

</details>

### 12. What is the default constructor?
- A) A constructor with no parameters
- B) A constructor with one parameter
- C) A constructor with multiple parameters
- D) A constructor that is private

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A default constructor takes no arguments and is automatically provided if no constructor is defined.

</details>

### 13. What is a copy constructor?
- A) A constructor that copies an object
- B) A constructor that deletes an object
- C) A constructor with no parameters
- D) A constructor that inherits properties

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A copy constructor creates a new object as a copy of an existing object.

</details>

### 14. What is a parameterized constructor?
- A) A constructor with no parameters
- B) A constructor that accepts arguments
- C) A constructor that copies objects
- D) A constructor that is private

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A parameterized constructor accepts arguments to initialize object attributes .

</details>

### 15. What is a friend function?
- A) A function that can access private members of a class
- B) A function that is a member of a class
- C) A function that inherits from a class
- D) A function that is virtual

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A friend function is not a member but can access private and protected members of a class.

</details>

### 16. What is a virtual function?
- A) A function that can be overridden in a derived class
- B) A function that cannot be overridden
- C) A function that is private
- D) A function that is static

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Virtual functions enable runtime polymorphism by allowing derived classes to override them .

</details>

### 17. What is a pure virtual function?
- A) A virtual function with no implementation
- B) A virtual function with implementation
- C) A static function
- D) A friend function

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A pure virtual function has no body and makes the class abstract.

</details>

### 18. What is an abstract class?
- A) A class that cannot be instantiated
- B) A class that can be instantiated
- C) A class with no methods
- D) A class with no attributes

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** An abstract class contains at least one pure virtual function and cannot be instantiated directly.

</details>

### 19. What is an interface?
- A) A class with only abstract methods
- B) A class with concrete methods
- C) A class with attributes only
- D) A class with no methods

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** An interface is a contract that defines method signatures without implementation.

</details>

### 20. What is method overloading?
- A) Defining multiple methods with the same name but different parameters
- B) Defining multiple methods with the same name and same parameters
- C) Overriding a method in a subclass
- D) Hiding a method

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Method overloading is compile-time polymorphism with same method name but different signatures.

</details>

### 21. What is method overriding?
- A) Defining a method in a subclass with the same signature as in the parent class
- B) Defining multiple methods with the same name
- C) Hiding a method
- D) Creating a new method

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Method overriding is runtime polymorphism where a subclass provides a specific implementation.

</details>

### 22. Which is resolved at compile time: overloading or overriding?
- A) Overloading
- B) Overriding
- C) Both
- D) Neither

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Method overloading is resolved at compile time (static binding) .

</details>

### 23. Which is resolved at runtime: overloading or overriding?
- A) Overloading
- B) Overriding
- C) Both
- D) Neither

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Method overriding is resolved at runtime (dynamic binding) .

</details>

### 24. What is static binding?
- A) Binding at compile time
- B) Binding at runtime
- C) Binding at link time
- D) Binding at load time

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Static binding (early binding) occurs at compile time for overloading, final methods, and private methods .

</details>

### 25. What is dynamic binding?
- A) Binding at compile time
- B) Binding at runtime
- C) Binding at link time
- D) Binding at load time

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Dynamic binding (late binding) occurs at runtime for overridden methods .

</details>

### 26. What is the this pointer in C++?
- A) A pointer to the current object
- B) A pointer to the parent class
- C) A null pointer
- D) A static pointer

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** The this pointer refers to the current object instance .

</details>

### 27. What is the super keyword in Java?
- A) Refers to the parent class
- B) Refers to the current object
- C) Refers to a static method
- D) Refers to a friend class

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** The super keyword refers to the immediate parent class.

</details>

### 28. What is a nested class?
- A) A class defined inside another class
- B) A class defined outside a class
- C) A class with no methods
- D) A class with no attributes

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A nested class is defined within the scope of another class.

</details>

### 29. What is the difference between a class and a structure in C++?
- A) Class members are private by default; struct members are public
- B) Class members are public by default; struct members are private
- C) They are exactly the same
- D) Structs cannot have methods

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** In C++, class members are private by default, while struct members are public by default.

</details>

### 30. Which OOP concept allows a class to inherit from multiple parent classes?
- A) Single inheritance
- B) Multiple inheritance
- C) Multilevel inheritance
- D) Hierarchical inheritance

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Multiple inheritance allows a class to inherit from more than one parent class (e.g., in C++).

</details>

## Part B: Inheritance & Polymorphism (Questions 31-60)


### 31. What is single inheritance?
- A) A class inheriting from one parent class
- B) A class inheriting from multiple parent classes
- C) A class inheriting from no parent class
- D) A class inheriting from itself

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Single inheritance involves one base class and one derived class.

</details>

### 32. What is multilevel inheritance?
- A) A class inheriting from a class that inherits from another class
- B) A class inheriting from multiple classes
- C) A class inheriting from no class
- D) A class inheriting from itself

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Multilevel inheritance forms a chain: A → B → C.

</details>

### 33. What is hierarchical inheritance?
- A) Multiple classes inherit from a single base class
- B) A single class inherits from multiple classes
- C) A class inherits from itself
- D) A class inherits from no class

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Hierarchical inheritance has one base class and multiple derived classes.

</details>

### 34. What is hybrid inheritance?
- A) Combination of two or more types of inheritance
- B) Single inheritance only
- C) Multiple inheritance only
- D) No inheritance

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Hybrid inheritance combines multiple and multilevel inheritance.

</details>

### 35. What is the diamond problem in inheritance?
- A) Ambiguity when a class inherits from two classes that share a common base
- B) A class inheriting from itself
- C) A class with no methods
- D) A class with no attributes

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** The diamond problem occurs with multiple inheritance when two parent classes inherit from the same grandparent.

</details>

### 36. How is the diamond problem solved in C++?
- A) Using virtual inheritance
- B) Using multiple inheritance
- C) Using private inheritance
- D) Using protected inheritance

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Virtual inheritance ensures only one copy of the common base class exists.

</details>

### 37. What is the access specifier that allows access only within the class?
- A) Public
- B) Private
- C) Protected
- D) Default

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Private members are accessible only within the class itself.

</details>

### 38. What is the access specifier that allows access within the class and derived classes?
- A) Public
- B) Private
- C) Protected
- D) Default

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Protected members are accessible within the class and its subclasses.

</details>

### 39. What is the access specifier that allows access from anywhere?
- A) Public
- B) Private
- C) Protected
- D) Default

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Public members are accessible from any code.

</details>

### 40. What is the default access specifier for class members in C++?
- A) Public
- B) Private
- C) Protected
- D) Default

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Class members in C++ are private by default.

</details>

### 41. What is the default access specifier for struct members in C++?
- A) Public
- B) Private
- C) Protected
- D) Default

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Struct members in C++ are public by default.

</details>

### 42. Which inheritance type is NOT supported in Java?
- A) Single
- B) Multilevel
- C) Multiple (through classes)
- D) Hierarchical

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Java does not support multiple inheritance through classes (only through interfaces).

</details>

### 43. What is an interface in Java?
- A) A reference type that can contain only constants, method signatures, default methods, static methods, and nested types
- B) A class with private members
- C) A class with attributes only
- D) A class with no methods

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Interfaces define a contract that implementing classes must follow.

</details>

### 44. Can a class implement multiple interfaces in Java?
- A) Yes
- B) No
- C) Only one
- D) Depends on the version

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Java allows a class to implement multiple interfaces.

</details>

### 45. What is an abstract method?
- A) A method without a body
- B) A method with a body
- C) A static method
- D) A final method

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** An abstract method has no implementation and must be overridden.

</details>

### 46. Can an abstract class have concrete methods?
- A) Yes
- B) No
- C) Only in Java
- D) Only in C++

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Abstract classes can have both abstract and concrete methods.

</details>

### 47. What is the difference between an abstract class and an interface?
- A) Abstract class can have concrete methods; interface cannot (before Java 8)
- B) Interface can have concrete methods; abstract class cannot
- C) Both are the same
- D) Abstract class cannot have constructors

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Abstract classes can have concrete methods and fields; interfaces traditionally only had abstract methods.

</details>

### 48. What is the final keyword in Java?
- A) Prevents inheritance or overriding
- B) Allows inheritance
- C) Allows overriding
- D) Makes a method abstract

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** final prevents a class from being subclassed or a method from being overridden.

</details>

### 49. What is the virtual keyword in C++?
- A) Enables runtime polymorphism
- B) Prevents overriding
- C) Makes a method static
- D) Makes a method private

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** virtual allows a method to be overridden in derived classes for runtime polymorphism .

</details>

### 50. What is a virtual destructor?
- A) A destructor declared virtual to ensure proper cleanup of derived objects
- B) A destructor that is private
- C) A destructor that is static
- D) A destructor with no parameters

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Virtual destructors ensure the correct destructor is called when deleting a derived object via a base pointer.

</details>

### 51. What is the output of cout << sizeof(emptyClass); in C++?
- A) 0
- B) 1
- C) 4
- D) 8

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** An empty class in C++ has a size of 1 byte to ensure unique addresses.

</details>

### 52. What is a static member?
- A) A member shared by all objects of a class
- B) A member unique to each object
- C) A private member
- D) A protected member

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Static members belong to the class rather than any specific object.

</details>

### 53. What is a static method?
- A) A method that can be called without creating an object
- B) A method that requires an object
- C) A method that is private
- D) A method that is virtual

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Static methods belong to the class and can be called using the class name.

</details>

### 54. Can a static method access non-static members?
- A) Yes
- B) No
- C) Only in C++
- D) Only in Java

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Static methods cannot access non-static members directly because they don't have a this pointer.

</details>

### 55. What is a constant member function?
- A) A function that cannot modify the object's data members
- B) A function that can modify data members
- C) A static function
- D) A virtual function

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Constant member functions (const in C++) cannot modify the object's state.

</details>

### 56. What is a mutable member?
- A) A member that can be modified even in a constant function
- B) A member that cannot be modified
- C) A static member
- D) A private member

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** The mutable keyword allows a member to be modified in a const function.

</details>

### 57. What is a shallow copy?
- A) Copying only the reference/pointer to the data
- B) Copying the actual data
- C) Copying methods only
- D) Copying attributes only

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A shallow copy copies the object's references, not the underlying data.

</details>

### 58. What is a deep copy?
- A) Copying the actual data, not just references
- B) Copying only references
- C) Copying methods only
- D) Copying attributes only

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A deep copy duplicates the underlying data so the original and copy are independent.

</details>

### 59. Which is more efficient: shallow copy or deep copy?
- A) Shallow copy
- B) Deep copy
- C) Both are equal
- D) Depends on the data

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Shallow copy is faster and uses less memory because it only copies references.

</details>

### 60. What is the rule of three in C++?
- A) If a class needs a custom destructor, copy constructor, or copy assignment operator, it likely needs all three
- B) Three constructors are required
- C) Three methods are required
- D) Three attributes are required

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** The Rule of Three states that if a class requires any of these three, it likely requires all three.

</details>

## Part C: Exception Handling & Advanced OOPs (Questions 61-90)


### 61. What is an exception?
- A) An error that occurs during program execution
- B) A syntax error
- C) A compilation error
- D) A warning

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Exceptions are runtime errors that disrupt the normal flow of execution.

</details>

### 62. What is exception handling?
- A) The process of responding to exceptions
- B) The process of creating exceptions
- C) The process of ignoring exceptions
- D) The process of compiling exceptions

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Exception handling allows programs to gracefully recover from errors .

</details>

### 63. Which of the following is NOT an exception handling keyword in Java?
- A) try
- B) catch
- C) finally
- D) except

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** Java uses try, catch, finally, throw, and throws. except is used in Python.

</details>

### 64. What is the try block?
- A) Contains code that might throw an exception
- B) Contains exception handling code
- C) Contains code that always executes
- D) Contains code that never executes

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** The try block encloses code that might generate an exception.

</details>

### 65. What is the catch block?
- A) Contains code to handle the exception
- B) Contains code that might throw an exception
- C) Contains code that always executes
- D) Contains code that never executes

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** The catch block handles exceptions thrown in the try block.

</details>

### 66. What is the finally block?
- A) Contains code that always executes regardless of exceptions
- B) Contains code that might throw an exception
- C) Contains code that never executes
- D) Contains exception handling code

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** The finally block executes regardless of whether an exception occurs.

</details>

### 67. Which exception is thrown when a class is not found at runtime in Java?
- A) NullPointerException
- B) ClassNotFoundException
- C) IOException
- D) ArithmeticException

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** ClassNotFoundException is thrown when the JVM tries to load a class that does not exist .

</details>

### 68. Which exception is thrown when dividing by zero in Java?
- A) NullPointerException
- B) ArithmeticException
- C) IOException
- D) ClassNotFoundException

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** ArithmeticException is thrown for arithmetic errors like division by zero.

</details>

### 69. Which exception is thrown when accessing a null object in Java?
- A) NullPointerException
- B) ArithmeticException
- C) IOException
- D) ClassNotFoundException

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** NullPointerException occurs when trying to use a null reference.

</details>

### 70. What is the throw keyword used for?
- A) To explicitly throw an exception
- B) To catch an exception
- C) To declare an exception
- D) To ignore an exception

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** throw is used to explicitly throw an exception from a method or block.

</details>

### 71. What is the throws keyword used for?
- A) To declare that a method might throw an exception
- B) To catch an exception
- C) To throw an exception
- D) To ignore an exception

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** throws declares which exceptions a method might throw, allowing the caller to handle them.

</details>

### 72. What is a checked exception?
- A) An exception that must be declared or handled at compile time
- B) An exception that is not checked at compile time
- C) An exception that cannot be caught
- D) An exception that is always ignored

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Checked exceptions (like IOException) must be declared or caught.

</details>

### 73. What is an unchecked exception?
- A) An exception that does not need to be declared or caught
- B) An exception that must be declared
- C) An exception that cannot be caught
- D) An exception that is always checked

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Unchecked exceptions (like RuntimeException) are not checked at compile time.

</details>

### 74. What is an error in Java?
- A) A serious problem that cannot be handled by the program
- B) An exception that can be handled
- C) A warning
- D) A compilation issue

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Errors (like OutOfMemoryError) are serious issues that the application usually cannot recover from.

</details>

### 75. What is a custom exception?
- A) A user-defined exception class
- B) A built-in exception
- C) An unchecked exception
- D) A checked exception

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Custom exceptions are created by extending Exception or RuntimeException.

</details>

### 76. What is the assert keyword used for?
- A) Debugging by verifying assumptions
- B) Exception handling
- C) Error handling
- D) Compilation

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** assert checks conditions during development and throws AssertionError if false.

</details>

### 77. What is a garbage collector?
- A) A mechanism that automatically frees unused memory
- B) A mechanism that allocates memory
- C) A mechanism that compiles code
- D) A mechanism that handles exceptions

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Garbage collection reclaims memory occupied by objects that are no longer referenced.

</details>

### 78. Which language has automatic garbage collection?
- A) Java
- B) C++
- C) C
- D) Assembly

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Java has automatic garbage collection. C++ requires manual memory management.

</details>

### 79. What is memory leak?
- A) Memory that is allocated but never freed
- B) Memory that is freed multiple times
- C) Memory that is not allocated
- D) Memory that is corrupted

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A memory leak occurs when allocated memory is no longer needed but is not released.

</details>

### 80. What is a dangling pointer?
- A) A pointer to memory that has been freed
- B) A pointer to valid memory
- C) A null pointer
- D) A void pointer

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A dangling pointer points to memory that has been deallocated.

</details>

### 81. What is a smart pointer in C++?
- A) A pointer wrapper that manages memory automatically
- B) A raw pointer
- C) A null pointer
- D) A void pointer

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Smart pointers (unique_ptr, shared_ptr) automatically manage memory deallocation.

</details>

### 82. What is a template in C++?
- A) A feature that allows generic programming
- B) A feature for inheritance
- C) A feature for polymorphism
- D) A feature for encapsulation

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Templates allow functions and classes to operate with generic types.

</details>

### 83. What is a generic in Java?
- A) A feature that allows type-safe generic programming
- B) A feature for inheritance
- C) A feature for polymorphism
- D) A feature for encapsulation

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Generics enable types (classes and interfaces) to be parameters when defining classes, interfaces, and methods.

</details>

### 84. What is the difference between == and equals() in Java?
- A) == compares references; equals() compares values
- B) == compares values; equals() compares references
- C) Both compare references
- D) Both compare values

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** == checks reference equality; equals() checks value equality (when overridden).

</details>

### 85. What is the hashCode() method used for?
- A) To generate a hash value for an object
- B) To compare objects
- C) To clone objects
- D) To destroy objects

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** hashCode() returns a hash code value used in hash-based collections.

</details>

### 86. What is the contract between equals() and hashCode()?
- A) If two objects are equal, they must have the same hash code
- B) If two objects have the same hash code, they must be equal
- C) Both A and B
- D) Neither

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Equal objects must have equal hash codes, but equal hash codes do not guarantee equality.

</details>

### 87. What is a singleton class?
- A) A class that allows only one instance
- B) A class that allows multiple instances
- C) A class with no instances
- D) A class with static methods only

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A singleton pattern ensures a class has only one instance and provides a global point of access.

</details>

### 88. What is a factory pattern?
- A) A creational pattern that creates objects without specifying the exact class
- B) A structural pattern
- C) A behavioral pattern
- D) A concurrency pattern

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** The factory pattern provides an interface for creating objects, letting subclasses decide which class to instantiate.

</details>

### 89. What is the observer pattern?
- A) A behavioral pattern where an object notifies dependents of state changes
- B) A creational pattern
- C) A structural pattern
- D) A concurrency pattern

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** The observer pattern defines a one-to-many dependency so that when one object changes state, all dependents are notified.

</details>

### 90. What is the MVC pattern?
- A) Model-View-Controller, a design pattern for user interfaces
- B) Model-View-Compiler
- C) Method-View-Controller
- D) Model-Value-Controller

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** MVC separates application logic into Model (data), View (UI), and Controller (logic).

</details>

## Part D: OOPs in Banking/IT Context (Questions 91-110)


### 91. In the context of banking software, what is the benefit of encapsulation?
- A) It protects sensitive data like account balances from unauthorized access
- B) It makes the code run faster
- C) It reduces memory usage
- D) It simplifies database queries

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Encapsulation hides internal data and only exposes necessary methods, enhancing security.

</details>

### 92. How is inheritance used in banking applications?
- A) Different account types (Savings, Current) inherit from a base Account class
- B) It is not used
- C) Only for UI design
- D) Only for database connections

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Inheritance allows common account properties and methods to be defined once in a base class.

</details>

### 93. How is polymorphism used in banking software?
- A) Different account types can implement their own interest calculation method
- B) It is not used
- C) Only for UI design
- D) Only for database connections

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Polymorphism allows a base class reference to call derived class methods, enabling flexible behavior.

</details>

### 94. Which OOP concept is used to hide the complexity of database operations in banking software?
- A) Abstraction
- B) Inheritance
- C) Encapsulation
- D) Polymorphism

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Abstraction hides complex database implementation behind simple methods like getBalance().

</details>

### 95. In Java, which memory area is used for storing class metadata at runtime (Java 8+)?
- A) Stack
- B) Heap
- C) Metaspace
- D) PermGen

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Java 8 replaced PermGen with Metaspace for storing class metadata .

</details>

### 96. What is the main advantage of using OOP in large banking systems?
- A) Code reusability and maintainability
- B) Faster execution
- C) Less memory usage
- D) Simpler syntax

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** OOP promotes modular, reusable, and maintainable code, which is essential for large systems.

</details>

### 97. In a banking application, what does the Account class likely encapsulate?
- A) Account number, balance, and methods to deposit/withdraw
- B) Only account number
- C) Only balance
- D) Only methods

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Encapsulation bundles related data (account number, balance) and methods together.

</details>

### 98. What is the purpose of a constructor in a Customer class?
- A) To initialize customer details like name, ID, and address
- B) To delete customer records
- C) To update customer balance
- D) To calculate interest

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Constructors initialize object state when a new customer object is created.

</details>

### 99. Which design pattern is commonly used for database connections in banking software?
- A) Singleton
- B) Observer
- C) Factory
- D) Strategy

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A singleton pattern ensures only one database connection pool instance exists.

</details>

### 100. What is the purpose of an interface in a payment system?
- A) To define a contract for payment methods (credit card, UPI, net banking)
- B) To store payment data
- C) To calculate taxes
- D) To generate reports

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** An interface defines methods that all payment types must implement.

</details>

### 101. What is the role of exception handling in ATM software?
- A) To gracefully handle errors like insufficient funds or network failure
- B) To hide errors
- C) To ignore errors
- D) To log errors only

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Exception handling allows the ATM to respond appropriately to errors without crashing.

</details>

### 102. What is the difference between ArrayList and LinkedList in Java (OOP context)?
- A) ArrayList uses dynamic arrays; LinkedList uses doubly linked lists
- B) Both use arrays
- C) Both use linked lists
- D) Both are the same

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** ArrayList provides fast random access; LinkedList provides fast insertion/deletion.

</details>

### 103. Which collection class is synchronized in Java?
- A) Vector
- B) ArrayList
- C) HashMap
- D) HashSet

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Vector is synchronized (thread-safe), while ArrayList is not.

</details>

### 104. What is the purpose of the transient keyword in Java?
- A) To prevent a field from being serialized
- B) To make a field static
- C) To make a field final
- D) To make a field volatile

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Transient fields are not included when the object is serialized.

</details>

### 105. What is serialization in Java?
- A) Converting an object into a byte stream
- B) Converting bytes into an object
- C) Converting an object into a string
- D) Converting a string into an object

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Serialization allows objects to be saved to a file or sent over a network.

</details>

### 106. What is the purpose of the volatile keyword in Java?
- A) To ensure visibility of changes across threads
- B) To make a field static
- C) To make a field final
- D) To make a field transient

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Volatile variables are read from main memory, ensuring thread visibility.

</details>

### 107. What is a thread in OOP?
- A) A lightweight process
- B) A class
- C) An object
- D) A method

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A thread is the smallest unit of execution within a process.

</details>

### 108. What is synchronization in Java?
- A) Controlling access to shared resources by multiple threads
- B) Creating multiple threads
- C) Destroying threads
- D) Pausing threads

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Synchronization prevents thread interference and memory consistency errors.

</details>

### 109. Which OOP concept is used to implement the Model-View-Controller (MVC) pattern?
- A) Encapsulation, Inheritance, and Polymorphism
- B) Only Inheritance
- C) Only Encapsulation
- D) Only Polymorphism

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** MVC uses encapsulation (model data), inheritance (view hierarchies), and polymorphism (controller behavior).

</details>

### 110. What is the main benefit of using design patterns in banking software?
- A) Proven solutions to common design problems
- B) Faster code execution
- C) Less memory usage
- D) Simpler syntax

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Design patterns provide reusable solutions to recurring design problems, improving code quality.

</details>
