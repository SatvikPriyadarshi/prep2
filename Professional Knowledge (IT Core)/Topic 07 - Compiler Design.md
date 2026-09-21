# Topic 7: Compiler Design (Previous Year Pattern)

## 📝 Quick Revision Cheat Sheet (Before you start)

- **Phases of Compiler:** Lexical Analysis → Syntax Analysis → Semantic Analysis → Intermediate Code Generation → Code Optimization → Code Generation.
- **Lexical Analysis:** Converts source code into tokens (scanner).
- **Syntax Analysis:** Checks grammatical structure using parse trees (parser).
- **Semantic Analysis:** Checks meaning, type checking, scope resolution.
- **Code Optimization:** Improves intermediate code for efficiency.
- **Linker:** Combines object modules into an executable.
- **Loader:** Loads executable into memory for execution.
- **Cross-Compiler:** Compiler that runs on one platform but generates code for another.

## Part A: Compiler Basics & Phases (Questions 1-30)


### 1. What does a compiler do?
- A) Translates high-level language to machine language
- B) Translates machine language to high-level language
- C) Executes the program
- D) Debugs the program

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A compiler translates source code (high-level) into object code (low-level/machine code) .

</details>

### 2. Which of the following is NOT a phase of a compiler?
- A) Lexical Analysis
- B) Syntax Analysis
- C) Code Execution
- D) Code Generation

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Code execution is done by the CPU, not the compiler. The compiler phases are: Lexical, Syntax, Semantic, Intermediate Code Generation, Optimization, and Code Generation .

</details>

### 3. What is the first phase of a compiler?
- A) Syntax Analysis
- B) Lexical Analysis
- C) Semantic Analysis
- D) Code Generation

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Lexical Analysis (scanning) is the first phase where source code is converted into tokens .

</details>

### 4. Which phase of the compiler converts source code into tokens?
- A) Syntax Analysis
- B) Semantic Analysis
- C) Lexical Analysis
- D) Code Generation

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Lexical Analysis groups characters into tokens .

</details>

### 5. What is a token in compiler design?
- A) A keyword
- B) A sequence of characters treated as a unit
- C) A variable
- D) An operator

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A token is a sequence of characters that can be treated as a unit in the grammar (e.g., keywords, identifiers, operators) .

</details>

### 6. Which phase checks whether the source code follows the syntax rules of the language?
- A) Lexical Analysis
- B) Syntax Analysis
- C) Semantic Analysis
- D) Code Optimization

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Syntax Analysis (parsing) checks the grammatical structure of the code .

</details>

### 7. What is the output of Syntax Analysis?
- A) Tokens
- B) Parse Tree / Syntax Tree
- C) Object Code
- D) Optimized Code

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Syntax Analysis produces a parse tree or syntax tree representing the grammatical structure .

</details>

### 8. Which phase checks for semantic errors like type mismatches?
- A) Lexical Analysis
- B) Syntax Analysis
- C) Semantic Analysis
- D) Code Generation

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Semantic Analysis checks the meaning of the code, including type checking and scope resolution .

</details>

### 9. Which phase generates intermediate code like Three-Address Code?
- A) Semantic Analysis
- B) Intermediate Code Generation
- C) Code Optimization
- D) Syntax Analysis

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Intermediate Code Generation produces a representation between source and machine code .

</details>

### 10. What is the purpose of Code Optimization?
- A) To make the code run faster and use less space
- B) To convert code to machine language
- C) To check syntax
- D) To generate tokens

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Code Optimization improves the intermediate code for better performance .

</details>

### 11. Which phase generates the final machine code?
- A) Code Optimization
- B) Code Generation
- C) Semantic Analysis
- D) Lexical Analysis

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Code Generation produces the target machine code .

</details>

### 12. What is an interpreter?
- A) Translates and executes line by line
- B) Translates the entire program at once
- C) Combines object modules
- D) Loads programs into memory

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** An interpreter translates and executes each line of high-level code individually .

</details>

### 13. What is the main difference between a compiler and an interpreter?
- A) Compiler translates the entire program; interpreter translates line by line
- B) Interpreter translates the entire program; compiler translates line by line
- C) Both are the same
- D) Compiler executes code; interpreter does not

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A compiler processes the entire program at once, while an interpreter processes line by line .

</details>

### 14. What is an assembler?
- A) Translates assembly language to machine language
- B) Translates high-level language to assembly
- C) Executes programs
- D) Debugs programs

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** An assembler translates assembly language (low-level) into machine code .

</details>

### 15. What is a cross-compiler?
- A) A compiler that runs on one platform and generates code for another platform
- B) A compiler that runs on the same platform it generates code for
- C) A compiler that compiles multiple languages
- D) A compiler that is cross-platform

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A cross-compiler runs on a host machine but generates executable code for a different target machine .

</details>

### 16. What is a bootstrap compiler?
- A) A compiler used to compile itself
- B) A compiler for a new language
- C) A compiler with no optimization
- D) A compiler that only works on one platform

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Bootstrapping is the process of using a compiler to compile itself.

</details>

### 17. What is a self-hosting compiler?
- A) A compiler that can compile its own source code
- B) A compiler that runs on the same machine
- C) A compiler with no dependencies
- D) A compiler that is open source

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A self-hosting compiler is written in the language it compiles.

</details>

### 18. What is a JIT compiler?
- A) Just-In-Time compiler that compiles code during execution
- B) A compiler that runs before execution
- C) A compiler for Java only
- D) A compiler with no optimization

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** JIT compiles bytecode to machine code at runtime for better performance .

</details>

### 19. What is the symbol table used for in a compiler?
- A) To store information about identifiers (variables, functions)
- B) To store machine code
- C) To store tokens
- D) To store parse trees

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** The symbol table stores metadata about identifiers like type, scope, and memory location.

</details>

### 20. Which phase is responsible for error handling and reporting?
- A) Lexical Analysis only
- B) All phases
- C) Code Generation only
- D) Semantic Analysis only

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Error handling occurs across all phases of compilation .

</details>

### 21. What is a one-pass compiler?
- A) A compiler that processes the source code in one pass
- B) A compiler that processes the source code in multiple passes
- C) A compiler that runs only once
- D) A compiler with no optimization

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A one-pass compiler reads the source code once and generates code immediately.

</details>

### 22. What is a multi-pass compiler?
- A) A compiler that processes the source code in multiple passes
- B) A compiler that processes the source code once
- C) A compiler that runs multiple times
- D) A compiler with no optimization

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Multi-pass compilers read the source code multiple times for better optimization.

</details>

### 23. What is the front end of a compiler?
- A) Analysis phase (lexical, syntax, semantic)
- B) Synthesis phase (code generation, optimization)
- C) Both A and B
- D) Neither

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** The front end performs analysis (lexical, syntax, semantic) and produces intermediate code.

</details>

### 24. What is the back end of a compiler?
- A) Analysis phase
- B) Synthesis phase (code generation, optimization)
- C) Both A and B
- D) Neither

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The back end performs synthesis (code optimization and generation) from intermediate code.

</details>

### 25. What is a parse tree?
- A) A tree representation of the syntactic structure of source code
- B) A tree of tokens
- C) A tree of machine code
- D) A tree of variables

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A parse tree represents the grammatical structure of source code .

</details>

### 26. What is an abstract syntax tree (AST)?
- A) A simplified parse tree without unnecessary details
- B) A full parse tree
- C) A tree of tokens
- D) A tree of machine code

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** AST is a condensed form of parse tree that omits details like parentheses.

</details>

### 27. What is the difference between a parse tree and an AST?
- A) AST is more abstract and omits syntactic details
- B) Parse tree is more abstract
- C) Both are the same
- D) AST contains more details

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** AST is a simplified representation focusing on semantic structure.

</details>

### 28. What is a lexical error?
- A) An error in token formation (e.g., invalid character)
- B) An error in grammar
- C) An error in meaning
- D) An error in code generation

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Lexical errors occur when the scanner encounters invalid characters or malformed tokens.

</details>

### 29. What is a syntax error?
- A) An error in the grammatical structure of code
- B) An error in token formation
- C) An error in meaning
- D) An error in code generation

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Syntax errors occur when the code violates the grammar rules of the language.

</details>

### 30. What is a semantic error?
- A) An error in the meaning of code (e.g., type mismatch)
- B) An error in grammar
- C) An error in token formation
- D) An error in code generation

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Semantic errors occur when the code is syntactically correct but logically incorrect .

</details>

## Part B: Lexical Analysis (Questions 31-50)


### 31. What is the main task of Lexical Analysis?
- A) Tokenization
- B) Parsing
- C) Code generation
- D) Optimization

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Lexical Analysis converts source code into tokens .

</details>

### 32. Which tool is commonly used for Lexical Analysis?
- A) Lex/Flex
- B) Yacc/Bison
- C) GCC
- D) GDB

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Lex (or Flex) is a tool for generating lexical analyzers .

</details>

### 33. What is a lexeme?
- A) The actual sequence of characters matched by a token
- B) A token
- C) A keyword
- D) An operator

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A lexeme is the actual string that matches a token pattern (e.g., "int" is a lexeme for the keyword token).

</details>

### 34. What is a regular expression used for in Lexical Analysis?
- A) To define token patterns
- B) To define grammar rules
- C) To optimize code
- D) To generate machine code

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Regular expressions define the patterns for tokens .

</details>

### 35. What is a finite automaton used for in Lexical Analysis?
- A) To recognize token patterns
- B) To parse grammar
- C) To optimize code
- D) To generate code

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Finite automata (DFA/NFA) are used to recognize regular expressions for tokenization .

</details>

### 36. What is the output of Lexical Analysis?
- A) A stream of tokens
- B) A parse tree
- C) Object code
- D) Optimized code

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Lexical Analysis produces a sequence of tokens .

</details>

### 37. Which of the following is NOT a token type?
- A) Keyword
- B) Identifier
- C) Function
- D) Operator

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Function is not a token type. Token types include keywords, identifiers, literals, operators, and punctuation.

</details>

### 38. What is a keyword in compiler design?
- A) A reserved word with special meaning
- B) A user-defined name
- C) A number
- D) An operator

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Keywords are reserved words like if, else, while, int, etc.

</details>

### 39. What is an identifier?
- A) A user-defined name for variables, functions, etc.
- B) A reserved word
- C) A number
- D) An operator

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Identifiers are names given by the programmer.

</details>

### 40. What is a literal in compiler design?
- A) A constant value (e.g., 5, "hello")
- B) A variable
- C) A function
- D) An operator

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Literals are constant values used in the program.

</details>

### 41. What is the role of the symbol table in Lexical Analysis?
- A) To store identifiers and their attributes
- B) To store tokens
- C) To store machine code
- D) To store parse trees

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** The symbol table stores information about identifiers as they are encountered.

</details>

### 42. What is a buffer used for in Lexical Analysis?
- A) To store input characters for tokenization
- B) To store tokens
- C) To store machine code
- D) To store parse trees

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Buffers are used to read and process input characters efficiently.

</details>

### 43. What is the purpose of a sentinel in Lexical Analysis?
- A) To simplify buffer management
- B) To store tokens
- C) To store machine code
- D) To store parse trees

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A sentinel (a special character) is used to simplify boundary checking in buffers.

</details>

### 44. What is a token stream?
- A) A sequence of tokens produced by Lexical Analysis
- B) A sequence of characters
- C) A sequence of machine instructions
- D) A sequence of parse trees

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** The token stream is the output of the lexical analyzer.

</details>

### 45. What is a lookahead in Lexical Analysis?
- A) Reading ahead to decide the next token
- B) Reading behind
- C) Skipping tokens
- D) Generating tokens

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Lookahead is used to determine token boundaries when patterns overlap.

</details>

### 46. What is a reserved word?
- A) A keyword
- B) An identifier
- C) A literal
- D) An operator

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Reserved words (keywords) have special meaning and cannot be used as identifiers.

</details>

### 47. Which of the following is NOT a task of Lexical Analysis?
- A) Removing comments
- B) Removing white spaces
- C) Generating tokens
- D) Building parse trees

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** Building parse trees is the task of Syntax Analysis .

</details>

### 48. What is the time complexity of Lexical Analysis?
- A) O(n) where n is the length of source code
- B) O(n²)
- C) O(log n)
- D) O(1)

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Lexical Analysis scans the source code once, making it O(n).

</details>

### 49. What is a token pattern?
- A) A regular expression that describes a token
- B) A token
- C) A keyword
- D) An operator

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Token patterns are defined using regular expressions.

</details>

### 50. What is a DFA?
- A) Deterministic Finite Automaton
- B) Direct Finite Automaton
- C) Dynamic Finite Automaton
- D) Dual Finite Automaton

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** DFA (Deterministic Finite Automaton) is used for lexical analysis.

</details>

## Part C: Syntax Analysis & Parsing (Questions 51-75)


### 51. What is Syntax Analysis also known as?
- A) Parsing
- B) Scanning
- C) Tokenizing
- D) Optimizing

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Syntax Analysis is also called parsing .

</details>

### 52. Which tool is commonly used for Syntax Analysis?
- A) Yacc/Bison
- B) Lex/Flex
- C) GCC
- D) GDB

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Yacc (or Bison) is a parser generator .

</details>

### 53. What is a context-free grammar (CFG)?
- A) A grammar used to define the syntax of programming languages
- B) A grammar for lexical analysis
- C) A grammar for code optimization
- D) A grammar for code generation

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** CFG defines the syntax rules of a programming language .

</details>

### 54. What is a parse tree?
- A) A tree representation of the syntactic structure
- B) A tree of tokens
- C) A tree of machine code
- D) A tree of variables

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Parse trees represent the grammatical structure of source code .

</details>

### 55. What is a top-down parser?
- A) A parser that starts from the root and works down to leaves
- B) A parser that starts from leaves and works up to root
- C) A parser that parses from left to right
- D) A parser that parses from right to left

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Top-down parsers build the parse tree from root to leaves.

</details>

### 56. What is a bottom-up parser?
- A) A parser that starts from leaves and works up to root
- B) A parser that starts from root and works down
- C) A parser that parses from left to right
- D) A parser that parses from right to left

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Bottom-up parsers build the parse tree from leaves to root.

</details>

### 57. Which of the following is a top-down parser?
- A) Recursive Descent
- B) LR Parser
- C) LALR Parser
- D) SLR Parser

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Recursive Descent is a top-down parser.

</details>

### 58. Which of the following is a bottom-up parser?
- A) Recursive Descent
- B) LL Parser
- C) LR Parser
- D) Predictive Parser

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** LR (Left-to-Right, Rightmost derivation) is a bottom-up parser.

</details>

### 59. What is an LL parser?
- A) Left-to-right, Leftmost derivation (top-down)
- B) Left-to-right, Rightmost derivation
- C) Right-to-left, Leftmost derivation
- D) Right-to-left, Rightmost derivation

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** LL parsers read input left-to-right and produce a leftmost derivation.

</details>

### 60. What is an LR parser?
- A) Left-to-right, Rightmost derivation (bottom-up)
- B) Left-to-right, Leftmost derivation
- C) Right-to-left, Leftmost derivation
- D) Right-to-left, Rightmost derivation

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** LR parsers read input left-to-right and produce a rightmost derivation in reverse.

</details>

### 61. What is a shift-reduce parser?
- A) A bottom-up parser using shift and reduce operations
- B) A top-down parser
- C) A lexical analyzer
- D) A code generator

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Shift-reduce parsers are a type of bottom-up parser.

</details>

### 62. What is a predictive parser?
- A) A top-down parser that predicts which production to use
- B) A bottom-up parser
- C) A lexical analyzer
- D) A code generator

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Predictive parsers are recursive descent parsers without backtracking.

</details>

### 63. What is backtracking in parsing?
- A) Trying different productions when one fails
- B) Skipping tokens
- C) Generating tokens
- D) Optimizing code

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Backtracking involves undoing a parsing decision and trying an alternative.

</details>

### 64. What is a FIRST set in parsing?
- A) The set of terminals that can begin a string derived from a non-terminal
- B) The set of terminals that can follow a non-terminal
- C) The set of non-terminals
- D) The set of tokens

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** FIRST set contains terminals that can start a derivation from a non-terminal.

</details>

### 65. What is a FOLLOW set in parsing?
- A) The set of terminals that can appear immediately after a non-terminal
- B) The set of terminals that can begin a string
- C) The set of non-terminals
- D) The set of tokens

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** FOLLOW set contains terminals that can follow a non-terminal in a derivation.

</details>

### 66. What is an ambiguous grammar?
- A) A grammar that can have multiple parse trees for the same string
- B) A grammar with no parse trees
- C) A grammar with only one parse tree
- D) A grammar with no terminals

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Ambiguous grammars allow multiple parse trees for a single string.

</details>

### 67. What is a left-recursive grammar?
- A) A grammar where a non-terminal can derive itself as the leftmost symbol
- B) A grammar where a non-terminal can derive itself as the rightmost symbol
- C) A grammar with no recursion
- D) A grammar with only right recursion

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Left recursion occurs when a non-terminal derives itself as the leftmost symbol.

</details>

### 68. What is left factoring?
- A) A transformation to eliminate common prefixes in grammar
- B) A transformation to eliminate left recursion
- C) A transformation to add recursion
- D) A transformation to remove ambiguity

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Left factoring is used to make grammars suitable for predictive parsing.

</details>

### 69. What is a parse stack used for?
- A) To store grammar symbols during parsing
- B) To store tokens
- C) To store machine code
- D) To store variables

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Parsers use a stack to store grammar symbols during parsing.

</details>

### 70. What is the output of Syntax Analysis?
- A) Parse tree
- B) Tokens
- C) Machine code
- D) Optimized code

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Syntax Analysis produces a parse tree .

</details>

### 71. What is a syntax error?
- A) An error in the grammatical structure of code
- B) An error in token formation
- C) An error in meaning
- D) An error in code generation

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Syntax errors violate grammar rules .

</details>

### 72. What is an LR(0) item?
- A) A production with a dot indicating the current position
- B) A token
- C) A parse tree
- D) A variable

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** LR(0) items are productions with a dot showing the parsing position.

</details>

### 73. What is SLR parsing?
- A) Simple LR parsing
- B) Strong LR parsing
- C) Standard LR parsing
- D) Sequential LR parsing

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** SLR (Simple LR) is a simplified version of LR parsing.

</details>

### 74. What is LALR parsing?
- A) Look-Ahead LR parsing
- B) Left-Ahead LR parsing
- C) Linear-Ahead LR parsing
- D) Logical-Ahead LR parsing

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** LALR (Look-Ahead LR) is a powerful parsing technique used by Yacc.

</details>

### 75. What is the main advantage of LR parsing?
- A) It can handle a larger class of grammars
- B) It is faster than LL parsing
- C) It requires less memory
- D) It is simpler to implement

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** LR parsers can handle a wider range of grammars than LL parsers.

</details>

## Part D: Linker, Loader & Code Optimization (Questions 76-110)


### 76. What is a linker?
- A) A program that combines object modules into an executable
- B) A program that loads executables into memory
- C) A program that compiles source code
- D) A program that debugs code

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A linker combines multiple object files into a single executable .

</details>

### 77. What is a loader?
- A) A program that loads an executable into memory
- B) A program that combines object modules
- C) A program that compiles source code
- D) A program that debugs code

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A loader loads the executable into main memory for execution .

</details>

### 78. What is the difference between a linker and a loader?
- A) Linker combines object modules; loader loads into memory
- B) Loader combines object modules; linker loads into memory
- C) Both are the same
- D) Linker executes code; loader compiles code

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Linker combines; loader loads. They are distinct programs .

</details>

### 79. What is a linking loader?
- A) A program that both links and loads
- B) A program that only links
- C) A program that only loads
- D) A program that compiles

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A linking loader performs both linking and loading in one step .

</details>

### 80. What is static linking?
- A) Linking done at compile time
- B) Linking done at runtime
- C) Linking done dynamically
- D) Linking done by the OS

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Static linking combines libraries into the executable at compile time.

</details>

### 81. What is dynamic linking?
- A) Linking done at runtime
- B) Linking done at compile time
- C) Linking done statically
- D) Linking done by the compiler

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Dynamic linking loads libraries at runtime, reducing executable size.

</details>

### 82. What is a DLL?
- A) Dynamic Link Library
- B) Direct Link Library
- C) Dynamic Load Library
- D) Direct Load Library

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** DLL (Dynamic Link Library) is a file containing code and data for dynamic linking.

</details>

### 83. What is relocation?
- A) Adjusting addresses in object code when loading
- B) Combining object modules
- C) Compiling source code
- D) Debugging code

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Relocation adjusts addresses in object code to reflect the actual memory location.

</details>

### 84. What is an absolute loader?
- A) A loader that loads code at absolute addresses
- B) A loader that relocates code
- C) A linker
- D) A compiler

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** An absolute loader loads code at fixed, predetermined addresses .

</details>

### 85. What is a relocating loader?
- A) A loader that adjusts addresses during loading
- B) A loader that loads at fixed addresses
- C) A linker
- D) A compiler

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A relocating loader adjusts addresses as it loads the program.

</details>

### 86. What is code optimization?
- A) Improving code efficiency (speed or size)
- B) Converting code to machine language
- C) Checking syntax
- D) Generating tokens

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Code optimization improves intermediate code for better performance .

</details>

### 87. What is dead code elimination?
- A) Removing code that is never executed
- B) Removing comments
- C) Removing white spaces
- D) Removing functions

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Dead code elimination removes unreachable or unused code.

</details>

### 88. What is loop optimization?
- A) Optimizing code inside loops
- B) Removing loops
- C) Adding loops
- D) Converting loops to recursion

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Loop optimization improves the efficiency of code within loops.

</details>

### 89. What is common subexpression elimination?
- A) Removing repeated calculations
- B) Removing repeated code
- C) Removing variables
- D) Removing functions

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Common subexpression elimination avoids recalculating the same expression.

</details>

### 90. What is strength reduction?
- A) Replacing expensive operations with cheaper ones
- B) Increasing code strength
- C) Removing operations
- D) Adding operations

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Strength reduction replaces expensive operations (e.g., multiplication) with cheaper ones (e.g., addition).

</details>

### 91. What is peephole optimization?
- A) Optimizing a small window of code
- B) Optimizing the entire program
- C) Optimizing loops
- D) Optimizing functions

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Peephole optimization examines a small set of instructions for optimization.

</details>

### 92. What is constant folding?
- A) Evaluating constant expressions at compile time
- B) Removing constants
- C) Adding constants
- D) Changing constants

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Constant folding evaluates constant expressions during compilation.

</details>

### 93. What is constant propagation?
- A) Replacing variables with known constant values
- B) Removing constants
- C) Adding constants
- D) Changing constants

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Constant propagation substitutes variables with their known constant values.

</details>

### 94. What is copy propagation?
- A) Replacing one variable with another
- B) Removing variables
- C) Adding variables
- D) Changing variables

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Copy propagation replaces uses of one variable with another when they are equal.

</details>

### 95. What is a basic block?
- A) A sequence of consecutive statements with one entry and one exit
- B) A single statement
- C) A function
- D) A loop

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Basic blocks are maximal sequences of consecutive statements with no branches in or out .

</details>

### 96. What is a control flow graph (CFG)?
- A) A graph representing the flow of control in a program
- B) A graph of tokens
- C) A graph of variables
- D) A graph of functions

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** CFG represents how control flows between basic blocks .

</details>

### 97. What is three-address code?
- A) An intermediate representation with at most three operands per instruction
- B) Machine code
- C) Assembly code
- D) High-level code

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Three-address code is a common intermediate representation .

</details>

### 98. What is a quadruple in intermediate code?
- A) A representation with four fields: operator, arg1, arg2, result
- B) A representation with three fields
- C) A representation with two fields
- D) A representation with one field

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Quadruples are a common form of three-address code.

</details>

### 99. What is a triple in intermediate code?
- A) A representation with three fields: operator, arg1, arg2
- B) A representation with four fields
- C) A representation with two fields
- D) A representation with one field

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Triples use references to other triples for results.

</details>

### 100. What is an indirect triple?
- A) A triple with pointers to other triples
- B) A triple with no pointers
- C) A quadruple
- D) A double

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Indirect triples use pointers to allow easy reordering.

</details>

### 101. What is the main purpose of a symbol table?
- A) To store information about identifiers
- B) To store machine code
- C) To store parse trees
- D) To store tokens

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** The symbol table stores metadata about identifiers (type, scope, etc.).

</details>

### 102. What is the scope of a variable?
- A) The region of code where the variable is accessible
- B) The value of the variable
- C) The type of the variable
- D) The name of the variable

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Scope defines where a variable can be accessed.

</details>

### 103. What is a hash table used for in a compiler?
- A) To implement the symbol table efficiently
- B) To store tokens
- C) To store parse trees
- D) To store machine code

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Hash tables provide fast lookup for symbol table entries.

</details>

### 104. What is a compiler directive?
- A) A command to the compiler (e.g., #include, #define)
- B) A keyword
- C) An operator
- D) A variable

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Compiler directives provide instructions to the compiler.

</details>

### 105. What is a preprocessor?
- A) A program that processes source code before compilation
- B) A program that compiles code
- C) A program that links code
- D) A program that loads code

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** The preprocessor handles directives like #include and #define.

</details>

### 106. What is macro expansion?
- A) Replacing macro names with their definitions
- B) Removing macros
- C) Adding macros
- D) Changing macros

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Macro expansion substitutes macro calls with their defined code.

</details>

### 107. What is conditional compilation?
- A) Compiling parts of code based on conditions
- B) Compiling all code
- C) Compiling no code
- D) Compiling only functions

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Conditional compilation uses directives like #ifdef to include/exclude code.

</details>

### 108. What is the output of a compiler?
- A) Object code
- B) Source code
- C) Assembly code only
- D) High-level code

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A compiler produces object code (machine code) .

</details>

### 109. What is a disassembler?
- A) A program that converts machine code to assembly
- B) A program that converts assembly to machine code
- C) A program that compiles code
- D) A program that links code

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A disassembler reverses the assembly process.

</details>

### 110. What is a decompiler?
- A) A program that converts machine code to high-level code
- B) A program that converts high-level to machine code
- C) A program that compiles code
- D) A program that links code

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A decompiler attempts to reconstruct high-level source from machine code.

</details>
