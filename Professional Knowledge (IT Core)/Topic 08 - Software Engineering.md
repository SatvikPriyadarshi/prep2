# Topic 8: Software Engineering (Previous Year Pattern)

## 📝 Quick Revision Cheat Sheet (Before you start)

- **SDLC Phases:** Planning → Analysis → Design → Implementation → Testing → Deployment → Maintenance.
- **SDLC Models:** Waterfall (linear), Spiral (risk-driven), Agile (iterative), Prototype (user feedback), V-Model (verification/validation).
- **Cohesion:** Degree of relatedness within a module. High cohesion is good.
- **Coupling:** Degree of interdependence between modules. Low coupling is good.
- **Testing Types:** Unit (individual components), Integration (combined modules), System (complete system), Acceptance (user validation).
- **Black Box vs White Box:** Black box tests functionality without knowing internals; White box tests internal logic.

## Part A: SDLC & Process Models (Questions 1-30)


### 1. What is SDLC?
- A) Software Development Life Cycle
- B) System Design Life Cycle
- C) Software Design Logic Cycle
- D) System Development Logic Cycle

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** SDLC (Software Development Life Cycle) is a framework for developing software through a structured process .

</details>

### 2. Which of the following is NOT a phase of SDLC?
- A) Requirement Analysis
- B) Design
- C) Compilation
- D) Testing

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Compilation is part of implementation, not a separate SDLC phase. The phases are Analysis, Design, Implementation, Testing, and Maintenance.

</details>

### 3. In which SDLC phase are user requirements gathered?
- A) Design
- B) Analysis
- C) Implementation
- D) Testing

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The Analysis phase involves gathering and documenting user requirements .

</details>

### 4. Which SDLC model follows a linear sequential flow?
- A) Spiral Model
- B) Waterfall Model
- C) Agile Model
- D) Prototype Model

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The Waterfall model follows a linear, sequential flow where each phase must be completed before the next begins.

</details>

### 5. Which SDLC model is known for its risk management feature?
- A) Waterfall Model
- B) Spiral Model
- C) Prototype Model
- D) V-Model

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The Spiral model is risk-driven and includes risk analysis in each iteration .

</details>

### 6. What is the most important feature of the Spiral model?
- A) Requirement analysis
- B) Risk management
- C) Quality management
- D) Configuration management

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Risk management is the defining feature of the Spiral model .

</details>

### 7. Which SDLC model is best suited when requirements are unclear?
- A) Waterfall Model
- B) Spiral Model
- C) Prototype Model
- D) V-Model

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** The Prototype model is used when requirements are not well understood, allowing users to provide feedback on a working model.

</details>

### 8. Which SDLC model emphasizes iterative development?
- A) Waterfall Model
- B) Agile Model
- C) V-Model
- D) Big Bang Model

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Agile models focus on iterative development with short cycles of planning, development, and testing.

</details>

### 9. What is the main disadvantage of the Waterfall model?
- A) Too much user involvement
- B) Difficult to accommodate changes
- C) Too expensive
- D) Requires too many resources

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The Waterfall model is rigid and does not easily accommodate changes once a phase is completed.

</details>

### 10. What does the V-Model emphasize?
- A) Risk management
- B) Verification and validation
- C) Iterative development
- D) Rapid prototyping

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The V-Model emphasizes verification and validation at each stage of development.

</details>

### 11. What is the primary goal of the Design phase?
- A) Writing code
- B) Creating a blueprint for the system
- C) Testing the system
- D) Gathering requirements

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The Design phase creates the architectural and detailed design of the system.

</details>

### 12. What is the output of the Analysis phase in SDLC?
- A) Program code
- B) Set of user requirements
- C) Test cases
- D) Design diagrams

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The Analysis phase produces a set of user requirements .

</details>

### 13. What is the role of a systems analyst in a software project?
- A) Write program source code
- B) Interact with users to determine their specific needs
- C) Manage the project budget
- D) Test the software

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The systems analyst interacts with users to determine their needs .

</details>

### 14. Which SDLC model is also known as the Linear Sequential Model?
- A) Spiral Model
- B) Waterfall Model
- C) Agile Model
- D) RAD Model

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The Waterfall model is also called the Linear Sequential Model.

</details>

### 15. What is the main advantage of the Prototype model?
- A) Low cost
- B) High user involvement and feedback
- C) Fast development
- D) No need for testing

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The Prototype model allows users to see and interact with a working model, providing early feedback.

</details>

### 16. What is the primary goal of Software Maintenance?
- A) To develop new software
- B) To modify software after delivery
- C) To test software
- D) To design software

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Software Maintenance involves modifying software after delivery to fix bugs, improve performance, or adapt to changes.

</details>

### 17. What is the main drawback of the Spiral model?
- A) Too much user involvement
- B) Complex and expensive
- C) Too fast
- D) No risk management

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The Spiral model is complex and can be expensive, especially for smaller projects.

</details>

### 18. Which model is best for large, complex projects with high risk?
- A) Waterfall Model
- B) Spiral Model
- C) Prototype Model
- D) Big Bang Model

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The Spiral model is designed for large, complex projects where risk management is critical.

</details>

### 19. What is the primary focus of the Implementation phase?
- A) Gathering requirements
- B) Writing and compiling code
- C) Testing
- D) Maintenance

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The Implementation phase involves writing and compiling the actual code.

</details>

### 20. What is the main purpose of the Testing phase?
- A) To write code
- B) To identify and fix defects
- C) To gather requirements
- D) To design the system

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Testing aims to identify and fix defects before the software is delivered .

</details>

### 21. What is the primary goal of the Deployment phase?
- A) To develop software
- B) To deliver software to users
- C) To test software
- D) To design software

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Deployment involves delivering the software to the production environment.

</details>

### 22. What is the primary goal of the Maintenance phase?
- A) To develop new features
- B) To ensure the software continues to work correctly
- C) To design the system
- D) To gather requirements

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Maintenance ensures the software continues to function correctly after deployment.

</details>

### 23. Which of the following is NOT an SDLC model?
- A) Waterfall
- B) Spiral
- C) Compiler
- D) Agile

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Compiler is a software tool, not an SDLC model.

</details>

### 24. What is the primary benefit of the Agile model?
- A) Flexibility and adaptability
- B) Low cost
- C) No testing required
- D) No documentation

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Agile allows for flexibility and adaptability to changing requirements.

</details>

### 25. What is the primary disadvantage of the Agile model?
- A) Too much documentation
- B) Less predictability and documentation
- C) Too slow
- D) No user involvement

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Agile can lack predictability and comprehensive documentation compared to traditional models.

</details>

### 26. What is a "Make or Buy" decision in SDLC?
- A) Deciding whether to develop software in-house or purchase it
- B) Deciding whether to test or not
- C) Deciding whether to use Agile or Waterfall
- D) Deciding whether to hire more developers

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A Make or Buy decision is made during the Analysis phase to determine whether to build or purchase software .

</details>

### 27. What is the primary output of the Design phase?
- A) User requirements
- B) Design documents and diagrams
- C) Test cases
- D) Code

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The Design phase produces design documents, diagrams, and specifications.

</details>

### 28. What is the primary input to the Testing phase?
- A) User requirements
- B) Design documents and code
- C) Maintenance plan
- D) Deployment plan

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Testing uses design documents and code to create test cases and identify defects.

</details>

### 29. What is the primary output of the Implementation phase?
- A) Design documents
- B) Source code
- C) User requirements
- D) Test plan

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The Implementation phase produces source code.

</details>

### 30. What is the primary goal of Software Engineering?
- A) To develop software that meets user requirements
- B) To make software fast
- C) To reduce costs
- D) To eliminate testing

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Software Engineering aims to develop software that meets user requirements and is reliable, maintainable, and efficient.

</details>

## Part B: Testing & Quality (Questions 31-60)


### 31. What is software testing?
- A) Writing code
- B) Executing software with test data to find defects
- C) Designing software
- D) Gathering requirements

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Software testing involves executing software with test data to examine outputs and operational behavior .

</details>

### 32. What is Unit Testing?
- A) Testing individual components or modules
- B) Testing the entire system
- C) Testing user acceptance
- D) Testing performance

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Unit testing tests individual components or modules in isolation.

</details>

### 33. What is Integration Testing?
- A) Testing individual components
- B) Testing combined modules
- C) Testing user acceptance
- D) Testing performance

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Integration testing tests combined modules to find interface errors .

</details>

### 34. What is the main purpose of Integration Testing?
- A) To find design errors
- B) To find analysis errors
- C) To find interface errors
- D) To find procedure errors

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Integration testing focuses on finding interface errors between modules .

</details>

### 35. What is System Testing?
- A) Testing individual components
- B) Testing the complete system
- C) Testing user acceptance
- D) Testing performance

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** System testing tests the complete, integrated system against requirements.

</details>

### 36. What is Acceptance Testing?
- A) Testing individual components
- B) Testing combined modules
- C) Testing by the user to validate the system
- D) Testing performance

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Acceptance testing is performed by the user to validate that the system meets their needs.

</details>

### 37. What is Black Box Testing?
- A) Testing internal logic
- B) Testing functionality without knowing internal structure
- C) Testing performance
- D) Testing security

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Black box testing focuses on inputs and outputs without knowledge of internal code.

</details>

### 38. What is White Box Testing?
- A) Testing functionality without knowing internals
- B) Testing internal logic and structure
- C) Testing performance
- D) Testing security

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** White box testing examines the internal logic and structure of the code.

</details>

### 39. Which testing technique is a fault simulation technique?
- A) Mutation testing
- B) Stress testing
- C) Black box testing
- D) White box testing

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Mutation testing is a fault simulation testing technique .

</details>

### 40. What is Stress Testing?
- A) Testing normal conditions
- B) Testing extreme conditions
- C) Testing user acceptance
- D) Testing functionality

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Stress testing tests the system under extreme conditions to evaluate its robustness.

</details>

### 41. What is Regression Testing?
- A) Testing new features
- B) Re-testing after changes to ensure no new bugs
- C) Testing performance
- D) Testing security

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Regression testing ensures that changes have not introduced new defects.

</details>

### 42. What is the main goal of testing?
- A) To prove software is bug-free
- B) To find defects
- C) To write code
- D) To design software

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Testing aims to find defects, not to prove the absence of bugs.

</details>

### 43. Which of the following is NOT a measure of software quality?
- A) Correctness
- B) Maintainability
- C) Accessibility
- D) Integrity

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Accessibility is a usability feature, not a core software quality measure .

</details>

### 44. What is correctness in software quality?
- A) The extent to which software meets its specifications
- B) The speed of software
- C) The cost of software
- D) The size of software

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Correctness measures how well software meets its specified requirements.

</details>

### 45. What is maintainability?
- A) The ease with which software can be modified
- B) The speed of software
- C) The cost of software
- D) The size of software

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Maintainability is the ease with which software can be understood, modified, and extended.

</details>

### 46. What is reliability?
- A) The ability of software to perform its required functions under stated conditions
- B) The speed of software
- C) The cost of software
- D) The size of software

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Reliability is the probability that software will work without failure for a specified time.

</details>

### 47. What is efficiency in software quality?
- A) The degree to which software uses resources optimally
- B) The speed of software
- C) The cost of software
- D) The size of software

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Efficiency measures how well software uses resources like CPU time and memory.

</details>

### 48. What is usability?
- A) The ease with which users can use the software
- B) The speed of software
- C) The cost of software
- D) The size of software

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Usability measures how easy it is for users to learn and operate the software.

</details>

### 49. What is portability?
- A) The ease with which software can be transferred to different environments
- B) The speed of software
- C) The cost of software
- D) The size of software

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Portability is the ease with which software can be adapted to different platforms.

</details>

### 50. What is the difference between verification and validation?
- A) Verification checks if we built the product right; validation checks if we built the right product
- B) Verification checks if we built the right product; validation checks if we built the product right
- C) Both are the same
- D) Verification is testing; validation is not

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Verification ensures the product meets specifications; validation ensures it meets user needs.

</details>

### 51. What is a test case?
- A) A set of inputs, execution conditions, and expected results
- B) A bug report
- C) A design document
- D) A requirement

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A test case defines inputs, conditions, and expected outputs for testing.

</details>

### 52. What is a test plan?
- A) A document describing the scope, approach, and schedule of testing
- B) A bug report
- C) A design document
- D) A requirement

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A test plan outlines the testing strategy, resources, and schedule.

</details>

### 53. What is a defect?
- A) A flaw in the software that causes incorrect results
- B) A feature
- C) A requirement
- D) A design document

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A defect (bug) is a flaw that causes the software to produce incorrect or unexpected results.

</details>

### 54. What is a test suite?
- A) A collection of test cases
- B) A collection of bugs
- C) A collection of requirements
- D) A collection of designs

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A test suite is a collection of test cases that are run together.

</details>

### 55. What is the purpose of a test harness?
- A) To automate the execution of tests
- B) To write code
- C) To design software
- D) To gather requirements

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A test harness provides an environment for automated test execution.

</details>

### 56. What is alpha testing?
- A) Testing performed by the development team at the developer's site
- B) Testing performed by users at the developer's site
- C) Testing performed by users at the user's site
- D) Testing performed by the development team at the user's site

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Alpha testing is performed by the development team internally before release.

</details>

### 57. What is beta testing?
- A) Testing performed by users at the user's site
- B) Testing performed by the development team
- C) Testing performed by the development team at the user's site
- D) Testing performed at the developer's site

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Beta testing is performed by real users in their own environment.

</details>

### 58. What is the difference between a fault and a failure?
- A) A fault is a defect in code; a failure is the manifestation of a fault
- B) A failure is a defect in code; a fault is the manifestation
- C) Both are the same
- D) Fault is in hardware; failure is in software

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A fault is the underlying defect; a failure is the observed incorrect behavior.

</details>

### 59. What is a test oracle?
- A) A mechanism to determine whether a test has passed or failed
- B) A test case
- C) A bug
- D) A requirement

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A test oracle determines the expected outcome of a test.

</details>

### 60. What is the purpose of test coverage?
- A) To measure the extent to which the code is tested
- B) To measure the number of bugs
- C) To measure the speed of testing
- D) To measure the cost of testing

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Test coverage measures how much of the code is exercised by the test suite.

</details>

## Part C: Cohesion & Coupling (Questions 61-85)


### 61. What is cohesion?
- A) The degree of relatedness within a module
- B) The degree of interdependence between modules
- C) The speed of a module
- D) The size of a module

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Cohesion measures how closely related the elements within a module are .

</details>

### 62. What is coupling?
- A) The degree of interdependence between modules
- B) The degree of relatedness within a module
- C) The speed of a module
- D) The size of a module

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Coupling measures the degree of interdependence between modules .

</details>

### 63. Which is better: high cohesion or low cohesion?
- A) High cohesion
- B) Low cohesion
- C) Both are equal
- D) Depends on the project

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** High cohesion means a module has a single, well-defined purpose.

</details>

### 64. Which is better: high coupling or low coupling?
- A) High coupling
- B) Low coupling
- C) Both are equal
- D) Depends on the project

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Low coupling means modules are less dependent on each other, making them easier to maintain.

</details>

### 65. What is functional cohesion?
- A) Elements of a module work together to perform a single function
- B) Elements are related by sequence
- C) Elements are related by communication
- D) Elements are related by coincidence

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Functional cohesion is the highest and best form of cohesion, where all elements contribute to a single task.

</details>

### 66. What is logical cohesion?
- A) Elements are related by logical function (e.g., all input operations)
- B) Elements are related by sequence
- C) Elements are related by communication
- D) Elements are related by coincidence

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Logical cohesion groups elements that perform logically similar functions.

</details>

### 67. What is temporal cohesion?
- A) Elements are related by timing (e.g., initialization)
- B) Elements are related by sequence
- C) Elements are related by communication
- D) Elements are related by coincidence

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Temporal cohesion groups elements that are executed at the same time.

</details>

### 68. What is procedural cohesion?
- A) Elements are related by sequence of execution
- B) Elements are related by timing
- C) Elements are related by communication
- D) Elements are related by coincidence

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Procedural cohesion groups elements that must be executed in a specific order.

</details>

### 69. What is communicational cohesion?
- A) Elements are related by communication (e.g., operate on the same data)
- B) Elements are related by sequence
- C) Elements are related by timing
- D) Elements are related by coincidence

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Communicational cohesion groups elements that operate on the same data.

</details>

### 70. What is coincidental cohesion?
- A) Elements are related by coincidence (no meaningful relationship)
- B) Elements are related by sequence
- C) Elements are related by communication
- D) Elements are related by function

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Coincidental cohesion is the worst form, where elements have no meaningful relationship.

</details>

### 71. What is data coupling?
- A) Modules share data through parameters
- B) Modules share global data
- C) Modules share control information
- D) Modules are completely independent

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Data coupling occurs when modules communicate by passing simple data parameters.

</details>

### 72. What is stamp coupling?
- A) Modules share a composite data structure (e.g., a record)
- B) Modules share simple data
- C) Modules share global data
- D) Modules share control information

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Stamp coupling occurs when modules share a composite data structure.

</details>

### 73. What is control coupling?
- A) One module controls the execution of another by passing control flags
- B) Modules share simple data
- C) Modules share global data
- D) Modules are completely independent

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Control coupling occurs when one module passes a control flag to another.

</details>

### 74. What is common coupling?
- A) Modules share global data
- B) Modules share simple data
- C) Modules share control information
- D) Modules are completely independent

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Common coupling occurs when modules share global data.

</details>

### 75. What is content coupling?
- A) One module directly accesses the internal data of another
- B) Modules share simple data
- C) Modules share global data
- D) Modules are completely independent

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Content coupling is the worst form, where one module directly modifies or relies on the internal workings of another.

</details>

### 76. Which coupling is best?
- A) Data coupling
- B) Content coupling
- C) Common coupling
- D) Control coupling

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Data coupling is the best (lowest) form of coupling.

</details>

### 77. Which cohesion is best?
- A) Functional cohesion
- B) Coincidental cohesion
- C) Logical cohesion
- D) Temporal cohesion

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Functional cohesion is the best (highest) form of cohesion.

</details>

### 78. Which coupling is worst?
- A) Content coupling
- B) Data coupling
- C) Stamp coupling
- D) Control coupling

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Content coupling is the worst (highest) form of coupling.

</details>

### 79. Which cohesion is worst?
- A) Coincidental cohesion
- B) Functional cohesion
- C) Sequential cohesion
- D) Communicational cohesion

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Coincidental cohesion is the worst (lowest) form of cohesion.

</details>

### 80. What is the relationship between cohesion and coupling?
- A) High cohesion and low coupling are desirable
- B) Low cohesion and high coupling are desirable
- C) High cohesion and high coupling are desirable
- D) Low cohesion and low coupling are desirable

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Good software design aims for high cohesion within modules and low coupling between modules.

</details>

### 81. What is a module?
- A) A self-contained unit of software
- B) A function
- C) A class
- D) A file

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A module is a self-contained component that performs a specific function.

</details>

### 82. What is modularity?
- A) The degree to which software is composed of discrete modules
- B) The speed of software
- C) The size of software
- D) The cost of software

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Modularity is the degree to which a system's components can be separated and recombined.

</details>

### 83. What is information hiding?
- A) Hiding implementation details from other modules
- B) Sharing all information
- C) Hiding all data
- D) Sharing all code

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Information hiding (encapsulation) hides internal details, reducing coupling.

</details>

### 84. What is the primary benefit of high cohesion?
- A) Modules are easier to understand and maintain
- B) Modules are faster
- C) Modules are smaller
- D) Modules are cheaper

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** High cohesion makes modules more understandable and maintainable.

</details>

### 85. What is the primary benefit of low coupling?
- A) Modules are easier to modify and reuse
- B) Modules are faster
- C) Modules are smaller
- D) Modules are cheaper

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Low coupling reduces the impact of changes, making modules easier to modify and reuse.

</details>

## Part D: Software Metrics & Estimation (Questions 86-110)


### 86. What is LOC?
- A) Lines of Code
- B) Length of Code
- C) Logic of Code
- D) Level of Code

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** LOC (Lines of Code) is a simple metric for measuring software size.

</details>

### 87. What is a COCOMO model?
- A) Constructive Cost Estimation Model
- B) Common Cost Estimation Model
- C) Complete Cost Estimation Model
- D) Comprehensive Cost Estimation Model

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** COCOMO (Constructive Cost Estimation Model) is used for software cost estimation .

</details>

### 88. What is function point analysis?
- A) A method to measure software size based on functionality
- B) A method to measure lines of code
- C) A method to measure bugs
- D) A method to measure speed

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Function point analysis measures software size based on the functionality it provides.

</details>

### 89. What is a software metric?
- A) A measure of some property of software
- B) A bug
- C) A requirement
- D) A design document

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Software metrics are quantitative measures of software properties.

</details>

### 90. What is cyclomatic complexity?
- A) A measure of the number of linearly independent paths through a program
- B) A measure of lines of code
- C) A measure of bugs
- D) A measure of speed

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Cyclomatic complexity measures the number of independent paths through code.

</details>

### 91. What is Halstead's complexity?
- A) A measure based on operators and operands
- B) A measure of lines of code
- C) A measure of bugs
- D) A measure of speed

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Halstead's complexity measures software based on the number of operators and operands.

</details>

### 92. What is a software project plan?
- A) A document describing the project scope, schedule, and resources
- B) A bug report
- C) A design document
- D) A test plan

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A software project plan outlines how the project will be executed.

</details>

### 93. What is risk management?
- A) Identifying and mitigating risks
- B) Writing code
- C) Designing software
- D) Testing software

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Risk management involves identifying, analyzing, and mitigating project risks .

</details>

### 94. What is risk monitoring?
- A) Regular monitoring of identified risks and new risks
- B) Ignoring risks
- C) Eliminating risks
- D) Creating risks

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Risk monitoring involves regularly checking identified risks and identifying new ones .

</details>

### 95. What is a risk?
- A) A potential problem that could affect the project
- B) A bug
- C) A requirement
- D) A design document

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A risk is a potential future problem that could negatively impact the project.

</details>

### 96. What is a Gantt chart?
- A) A bar chart showing project schedule
- B) A pie chart
- C) A line graph
- D) A scatter plot

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A Gantt chart visually represents the project schedule.

</details>

### 97. What is a PERT chart?
- A) A network diagram showing task dependencies
- B) A bar chart
- C) A pie chart
- D) A line graph

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A PERT (Program Evaluation and Review Technique) chart shows task dependencies and the critical path.

</details>

### 98. What is the critical path?
- A) The longest path through a project network
- B) The shortest path
- C) The most expensive path
- D) The least risky path

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** The critical path is the longest sequence of dependent tasks that determines the project duration.

</details>

### 99. What is software configuration management?
- A) Managing changes to software artifacts
- B) Writing code
- C) Designing software
- D) Testing software

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Software configuration management tracks and controls changes to software artifacts.

</details>

### 100. What is version control?
- A) Managing different versions of software artifacts
- B) Writing code
- C) Designing software
- D) Testing software

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Version control tracks changes to files over time, allowing rollback and collaboration.

</details>

### 101. What is a baseline?
- A) A fixed reference point for software configuration
- B) A bug
- C) A requirement
- D) A design document

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A baseline is a formally reviewed and approved configuration item that serves as a reference.

</details>

### 102. What is software reengineering?
- A) Restructuring existing software to improve it
- B) Writing new software
- C) Testing software
- D) Designing software

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Software reengineering involves examining and altering software to reconstitute it in a new form.

</details>

### 103. What is reverse engineering?
- A) Analyzing software to understand its design and implementation
- B) Writing new software
- C) Testing software
- D) Designing software

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Reverse engineering analyzes existing software to recover design information.

</details>

### 104. What is a legacy system?
- A) An old system that is still in use
- B) A new system
- C) A bug
- D) A requirement

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A legacy system is an old system that remains critical to the organization.

</details>

### 105. What is software portability?
- A) The ease with which software can be moved to a different environment
- B) The speed of software
- C) The cost of software
- D) The size of software

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Portability is the ease with which software can be adapted to different platforms.

</details>

### 106. What is software interoperability?
- A) The ability of software to exchange and use information with other software
- B) The speed of software
- C) The cost of software
- D) The size of software

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Interoperability is the ability of systems to exchange and use information.

</details>

### 107. What is a software requirement specification (SRS)?
- A) A document describing what the software should do
- B) A bug report
- C) A design document
- D) A test plan

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** SRS documents the functional and non-functional requirements of the software.

</details>

### 108. What is a functional requirement?
- A) A requirement that describes what the system should do
- B) A requirement that describes how the system should perform
- C) A bug
- D) A design document

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Functional requirements describe the behavior and functions of the system.

</details>

### 109. What is a non-functional requirement?
- A) A requirement that describes how the system should perform (e.g., performance, security)
- B) A requirement that describes what the system should do
- C) A bug
- D) A design document

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Non-functional requirements describe quality attributes like performance, security, and usability.

</details>

### 110. What is requirement elicitation?
- A) The process of gathering requirements from stakeholders
- B) Writing code
- C) Designing software
- D) Testing software

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Requirement elicitation involves gathering requirements from users and stakeholders.

</details>
