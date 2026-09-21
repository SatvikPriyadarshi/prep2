# Topic 2: DBMS (Database Management Systems)

## 📝 Quick Revision Cheat Sheet (Before you start)

- **ACID:** Atomicity, Consistency, Isolation, Durability.
- **Normal Forms:** 1NF (Atomic), 2NF (No Partial Dependency), 3NF (No Transitive Dependency), BCNF (Every determinant is a candidate key).
- **Keys:** Super Key ⊃ Candidate Key ⊃ Primary Key. Foreign Key references Primary Key.
- **SQL Commands:** DDL (Create, Alter, Drop), DML (Select, Insert, Update, Delete), DCL (Grant, Revoke), TCL (Commit, Rollback, Savepoint).
- **Joins:** Inner Join (Intersection), Left Join (All Left + Matching Right), Right Join (All Right + Matching Left), Full Join (Union).

## Part A: Basic Concepts & Architecture (Questions 1-20)


### 1. What does DBMS stand for?
- A) Database Management System
- B) Data Binding Management System
- C) Digital Base Management System
- D) Database Mining System

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** DBMS is software that manages databases, providing an interface for users to store, retrieve, and manipulate data.

</details>

### 2. Which of the following is NOT a disadvantage of a file system compared to a DBMS?
- A) Data redundancy
- B) Data inconsistency
- C) Program-data independence
- D) Difficulty in concurrent access

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Program-data independence is an advantage of DBMS, not a disadvantage of file systems. File systems lack it.

</details>

### 3. The three-level architecture of a DBMS consists of:
- A) Physical, Logical, View
- B) Internal, Conceptual, External
- C) Hardware, Software, User
- D) Local, Global, Universal

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The ANSI/SPARC architecture defines Internal (physical), Conceptual (logical), and External (view) levels.

</details>

### 4. Which level of DBMS architecture describes how data is physically stored?
- A) External level
- B) Conceptual level
- C) Internal level
- D) View level

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** The Internal level (physical level) describes the physical storage structure and access methods.

</details>

### 5. Data independence in DBMS refers to:
- A) Data stored independently of programs
- B) Ability to change schema at one level without affecting the schema at the next higher level
- C) Data stored in multiple files
- D) Independent tables

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Logical and physical data independence allow changes in schema without affecting application programs.

</details>

### 6. Which of the following is a logical data model?
- A) Relational model
- B) Network model
- C) Hierarchical model
- D) All of the above

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** Relational, Network, and Hierarchical are all logical data models.

</details>

### 7. In the relational model, data is stored in:
- A) Trees
- B) Graphs
- C) Tables
- D) Linked lists

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** The relational model stores data in relations (tables) consisting of rows and columns.

</details>

### 8. A row in a relational table is called:
- A) Attribute
- B) Tuple
- C) Domain
- D) Relation

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A row is called a tuple. A column is called an attribute.

</details>

### 9. A column in a relational table is called:
- A) Tuple
- B) Attribute
- C) Record
- D) Instance

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Columns represent attributes (properties) of the entity.

</details>

### 10. The number of tuples in a relation is called:
- A) Degree
- B) Cardinality
- C) Domain
- D) Schema

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Cardinality refers to the number of rows (tuples) in a relation.

</details>

### 11. The number of attributes in a relation is called:
- A) Degree
- B) Cardinality
- C) Domain
- D) Schema

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Degree refers to the number of columns (attributes) in a relation.

</details>

### 12. Which of the following is NOT a component of a DBMS?
- A) Query Processor
- B) Storage Manager
- C) Disk Controller
- D) Transaction Manager

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Disk Controller is hardware. DBMS components include Query Processor, Storage Manager, and Transaction Manager.

</details>

### 13. The person responsible for authorizing access to the database is:
- A) Database Administrator (DBA)
- B) End User
- C) Application Programmer
- D) System Analyst

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** The DBA manages the database, including user access, security, and performance tuning.

</details>

### 14. Which of the following is a physical data model?
- A) ER Model
- B) Relational Model
- C) Object-Oriented Model
- D) None of the above

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** ER, Relational, and Object-Oriented models are logical/conceptual. Physical models describe storage details.

</details>

### 15. The conceptual schema is also known as:
- A) View level
- B) Logical schema
- C) Physical schema
- D) External schema

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The conceptual level is also called the logical schema, describing the structure of the entire database.

</details>

### 16. Which of the following is true about a DBMS?
- A) It reduces data redundancy
- B) It increases data inconsistency
- C) It eliminates the need for backups
- D) It is always faster than file systems

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** DBMS controls redundancy through normalization and centralized management.

</details>

### 17. Metadata in a DBMS refers to:
- A) Actual data
- B) Data about data
- C) Deleted data
- D) Encrypted data

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Metadata describes the structure, constraints, and properties of the data.

</details>

### 18. The data dictionary stores:
- A) User data
- B) Metadata
- C) Indexes
- D) Logs

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The data dictionary (system catalog) stores metadata about tables, columns, constraints, and users.

</details>

### 19. Which of the following is a valid DBMS language?
- A) SQL
- B) QBE
- C) DDL
- D) All of the above

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** SQL (Structured Query Language), QBE (Query By Example), and DDL (Data Definition Language) are all DBMS languages.

</details>

### 20. DDL stands for:
- A) Data Definition Language
- B) Data Deletion Language
- C) Data Duplication Language
- D) Data Distribution Language

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** DDL is used to define the database schema (CREATE, ALTER, DROP).

</details>

## Part B: ER Model & Keys (Questions 21-50)


### 21. In an ER diagram, a rectangle represents:
- A) Attribute
- B) Entity
- C) Relationship
- D) Primary Key

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Rectangles represent entity sets.

</details>

### 22. In an ER diagram, a diamond represents:
- A) Entity
- B) Attribute
- C) Relationship
- D) Weak Entity

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Diamonds represent relationship sets between entities.

</details>

### 23. In an ER diagram, an ellipse represents:
- A) Entity
- B) Attribute
- C) Relationship
- D) Key

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Ellipses represent attributes of an entity or relationship.

</details>

### 24. A double-lined ellipse represents:
- A) Primary Key
- B) Multivalued Attribute
- C) Derived Attribute
- D) Composite Attribute

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Double-lined ellipses represent multivalued attributes (e.g., phone numbers).

</details>

### 25. A dashed ellipse represents:
- A) Primary Key
- B) Multivalued Attribute
- C) Derived Attribute
- D) Composite Attribute

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Dashed ellipses represent derived attributes (e.g., age derived from DOB).

</details>

### 26. A double rectangle represents:
- A) Strong Entity
- B) Weak Entity
- C) Relationship
- D) Attribute

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Weak entities do not have a primary key and depend on a strong entity.

</details>

### 27. A double diamond represents:
- A) Strong Relationship
- B) Weak Relationship
- C) Identifying Relationship
- D) Recursive Relationship

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Identifying relationships connect weak entities to their strong entities.

</details>

### 28. What is a super key?
- A) A key with a single attribute
- B) Any set of attributes that uniquely identifies a tuple
- C) A key with multiple attributes
- D) A foreign key

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A super key is any combination of attributes that can uniquely identify a row.

</details>

### 29. What is a candidate key?
- A) A minimal super key
- B) A foreign key
- C) A primary key
- D) A composite key

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A candidate key is a minimal set of attributes that uniquely identifies a tuple (no redundant attributes).

</details>

### 30. What is a primary key?
- A) A key chosen from candidate keys to uniquely identify tuples
- B) A foreign key
- C) A super key
- D) A composite key

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** The primary key is the candidate key selected by the DBA for unique identification.

</details>

### 31. A foreign key is:
- A) A key that uniquely identifies a row
- B) An attribute that references the primary key of another table
- C) A candidate key
- D) A super key

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A foreign key creates a link between two tables by referencing the primary key of another table.

</details>

### 32. A composite key is:
- A) A key with a single attribute
- B) A primary key with multiple attributes
- C) A foreign key
- D) A super key

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A composite key consists of two or more attributes that together uniquely identify a row.

</details>

### 33. Which of the following is NOT a type of key?
- A) Primary key
- B) Foreign key
- C) Secondary key
- D) Tertiary key

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** Tertiary key is not a standard DBMS key type.

</details>

### 34. A relationship where one entity is associated with at most one entity of another type is:
- A) One-to-One
- B) One-to-Many
- C) Many-to-Many
- D) None

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** In a 1:1 relationship, each entity instance is related to at most one instance of the other entity.

</details>

### 35. A relationship where one entity is associated with multiple entities of another type is:
- A) One-to-One
- B) One-to-Many
- C) Many-to-Many
- D) None

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** In a 1:N relationship, one entity instance can relate to many instances of another entity.

</details>

### 36. A relationship where multiple entities are associated with multiple entities is:
- A) One-to-One
- B) One-to-Many
- C) Many-to-Many
- D) None

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** In an M:N relationship, many instances of one entity relate to many instances of another.

</details>

### 37. In a many-to-many relationship, a new table is created to:
- A) Store the relationship
- B) Store the entities
- C) Store the primary key
- D) Store the foreign key

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** M:N relationships require a junction (associative) table to store the relationship.

</details>

### 38. Generalization in ER modeling is:
- A) Bottom-up approach
- B) Top-down approach
- C) Left-right approach
- D) Random approach

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Generalization combines lower-level entities into a higher-level entity (bottom-up).

</details>

### 39. Specialization in ER modeling is:
- A) Bottom-up approach
- B) Top-down approach
- C) Left-right approach
- D) Random approach

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Specialization divides a higher-level entity into lower-level entities (top-down).

</details>

### 40. Aggregation in ER modeling represents:
- A) A relationship between entities
- B) A relationship between relationships
- C) A weak entity
- D) A derived attribute

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Aggregation treats a relationship as an entity to relate it to another entity.

</details>

### 41. A recursive relationship is:
- A) Between two different entities
- B) Between an entity and itself
- C) Between three entities
- D) Between a relationship and an entity

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A recursive (unary) relationship occurs when an entity is related to itself (e.g., Employee manages Employee).

</details>

### 42. A ternary relationship involves:
- A) Two entities
- B) Three entities
- C) One entity
- D) Four entities

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A ternary relationship involves three entities simultaneously.

</details>

### 43. Which of the following is a valid ER notation for a primary key?
- A) Underlined attribute
- B) Dashed attribute
- C) Double ellipse
- D) Double rectangle

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Primary keys are represented by underlining the attribute name.

</details>

### 44. Which of the following is NOT an ER model concept?
- A) Entity
- B) Attribute
- C) Relationship
- D) Normalization

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** Normalization is a relational database design technique, not an ER modeling concept.

</details>

### 45. In an ER diagram, a double line connecting an entity to a relationship indicates:
- A) Partial participation
- B) Total participation
- C) No participation
- D) Optional participation

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Double lines indicate total participation (existence dependency).

</details>

### 46. A single line connecting an entity to a relationship indicates:
- A) Partial participation
- B) Total participation
- C) No participation
- D) Mandatory participation

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Single lines indicate partial participation (not all entities participate).

</details>

### 47. What is a weak entity?
- A) An entity with a primary key
- B) An entity without a primary key
- C) An entity with a foreign key
- D) An entity with no attributes

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Weak entities do not have a primary key of their own and depend on a strong entity.

</details>

### 48. The discriminator of a weak entity is:
- A) Its primary key
- B) A partial key
- C) A foreign key
- D) A super key

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A discriminator (partial key) distinguishes weak entity instances for the same owner.

</details>

### 49. Which of the following is true about a primary key?
- A) It can contain NULL values
- B) It cannot contain NULL values
- C) It can have duplicate values
- D) It is always a foreign key

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Primary keys must be unique and cannot contain NULL values.

</details>

### 50. Which of the following is true about a foreign key?
- A) It must be unique
- B) It can contain NULL values
- C) It cannot reference a primary key
- D) It must be a composite key

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Foreign keys can contain NULL values (unless specified otherwise) and can have duplicates.

</details>

## Part C: Normalization (Questions 51-80)


### 51. What is normalization?
- A) A process to increase data redundancy
- B) A process to organize data to minimize redundancy and dependency
- C) A process to delete data
- D) A process to encrypt data

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Normalization organizes columns and tables to reduce data redundancy and improve data integrity.

</details>

### 52. Which normal form deals with atomic values?
- A) 1NF
- B) 2NF
- C) 3NF
- D) BCNF

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** First Normal Form (1NF) requires all attributes to have atomic (indivisible) values.

</details>

### 53. Which normal form deals with partial dependency?
- A) 1NF
- B) 2NF
- C) 3NF
- D) BCNF

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Second Normal Form (2NF) eliminates partial dependencies on the primary key.

</details>

### 54. Which normal form deals with transitive dependency?
- A) 1NF
- B) 2NF
- C) 3NF
- D) BCNF

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Third Normal Form (3NF) eliminates transitive dependencies (non-prime attributes depending on other non-prime attributes).

</details>

### 55. A relation is in 1NF if:
- A) It has no partial dependencies
- B) All attributes are atomic
- C) It has no transitive dependencies
- D) It is in BCNF

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** 1NF requires atomic values in all attributes.

</details>

### 56. A relation is in 2NF if:
- A) It is in 1NF and has no partial dependencies
- B) It is in 1NF and has no transitive dependencies
- C) It is in 3NF
- D) It has no multivalued dependencies

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** 2NF requires 1NF and no partial dependency (non-prime attribute depending on part of a composite key).

</details>

### 57. A relation is in 3NF if:
- A) It is in 2NF and has no transitive dependencies
- B) It is in 1NF
- C) It is in BCNF
- D) It has no partial dependencies

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** 3NF requires 2NF and no transitive dependency.

</details>

### 58. BCNF stands for:
- A) Boyce-Codd Normal Form
- B) Binary Coded Normal Form
- C) Basic Codd Normal Form
- D) Boolean Codd Normal Form

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** BCNF is named after Raymond Boyce and Edgar F. Codd.

</details>

### 59. A relation is in BCNF if:
- A) It is in 3NF
- B) For every functional dependency X→Y, X is a super key
- C) It has no transitive dependencies
- D) It has no partial dependencies

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** BCNF is a stronger version of 3NF where every determinant must be a candidate key.

</details>

### 60. Which normal form is stricter: 3NF or BCNF?
- A) 3NF
- B) BCNF
- C) Both are equal
- D) Depends on the data

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** BCNF is stricter than 3NF. Every BCNF relation is in 3NF, but not vice versa.

</details>

### 61. Which of the following is a type of functional dependency?
- A) Full dependency
- B) Partial dependency
- C) Transitive dependency
- D) All of the above

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** Full, Partial, and Transitive are all types of functional dependencies.

</details>

### 62. A partial dependency occurs when:
- A) A non-prime attribute depends on part of a composite primary key
- B) A non-prime attribute depends on another non-prime attribute
- C) A prime attribute depends on a non-prime attribute
- D) A non-prime attribute depends on the full primary key

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Partial dependency is when a non-prime attribute depends on only a part of a composite primary key.

</details>

### 63. A transitive dependency occurs when:
- A) A → B and B → C, therefore A → C
- B) A → B and A → C
- C) A → B and C → B
- D) A → B and B → A

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Transitive dependency is an indirect dependency (A determines B, B determines C, so A determines C).

</details>

### 64. Which of the following is a multivalued dependency?
- A) X → Y
- B) X →→ Y
- C) X → Y → Z
- D) X ↔ Y

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** The double arrow (→→) represents a multivalued dependency, addressed in 4NF.

</details>

### 65. Which normal form deals with multivalued dependencies?
- A) 3NF
- B) BCNF
- C) 4NF
- D) 5NF

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Fourth Normal Form (4NF) eliminates multivalued dependencies.

</details>

### 66. Which normal form deals with join dependencies?
- A) 4NF
- B) 5NF
- C) BCNF
- D) 3NF

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Fifth Normal Form (5NF) or Project-Join Normal Form (PJNF) deals with join dependencies.

</details>

### 67. Denormalization is:
- A) The process of adding redundancy to improve performance
- B) The process of removing redundancy
- C) The process of creating indexes
- D) The process of deleting tables

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Denormalization intentionally introduces redundancy to speed up read queries.

</details>

### 68. Which of the following is a benefit of normalization?
- A) Reduced data redundancy
- B) Improved data integrity
- C) Easier maintenance
- D) All of the above

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** Normalization provides all these benefits.

</details>

### 69. Which of the following is a drawback of normalization?
- A) Increased redundancy
- B) More complex queries (more joins)
- C) Data inconsistency
- D) Larger storage

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Normalization often requires more joins to retrieve data, which can slow down queries.

</details>

### 70. A relation with a composite primary key is in 1NF but not 2NF if:
- A) It has partial dependencies
- B) It has transitive dependencies
- C) It has multivalued dependencies
- D) It has no dependencies

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Partial dependencies violate 2NF.

</details>

### 71. If a relation is in 3NF, it must also be in:
- A) 1NF and 2NF
- B) BCNF
- C) 4NF
- D) 5NF

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** 3NF requires 2NF, which requires 1NF.

</details>

### 72. Which of the following is NOT a normal form?
- A) 1NF
- B) 2NF
- C) 3NF
- D) 6NF

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** While 6NF exists in theory, the standard normal forms are 1NF through 5NF (and BCNF).

</details>

### 73. The process of converting a relation to a higher normal form is called:
- A) Normalization
- B) Denormalization
- C) Decomposition
- D) Aggregation

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** Decomposition is the process of breaking a relation into smaller relations to achieve higher normal forms.

</details>

### 74. Lossless decomposition ensures:
- A) No data is lost during decomposition
- B) Data is duplicated
- C) Data is deleted
- D) Data is encrypted

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A lossless decomposition allows the original relation to be reconstructed without any loss of information.

</details>

### 75. Dependency preservation ensures:
- A) All functional dependencies are preserved after decomposition
- B) Data is lost
- C) Redundancy is increased
- D) Indexes are created

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Dependency preservation means all original FDs can be enforced without joining the decomposed relations.

</details>

### 76. Which normal form is also known as Project-Join Normal Form?
- A) 3NF
- B) BCNF
- C) 4NF
- D) 5NF

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** 5NF is also called Project-Join Normal Form (PJNF).

</details>

### 77. A table with no repeating groups and a primary key is in:
- A) 1NF
- B) 2NF
- C) 3NF
- D) BCNF

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** 1NF requires atomic values and a primary key.

</details>

### 78. If a table is in 2NF, it is automatically in:
- A) 1NF
- B) 3NF
- C) BCNF
- D) 4NF

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** 2NF is a higher form of 1NF, so it must satisfy 1NF.

</details>

### 79. Which of the following is an example of a transitive dependency?
- A) StudentID → StudentName
- B) StudentID → CourseID and CourseID → CourseName
- C) StudentID → CourseID
- D) CourseID → StudentID

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** StudentID determines CourseID, and CourseID determines CourseName. Therefore, StudentID determines CourseName transitively.

</details>

### 80. Which normal form eliminates all redundancy based on functional dependencies?
- A) 1NF
- B) 2NF
- C) 3NF
- D) BCNF

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** BCNF eliminates all redundancy that can be discovered based on functional dependencies.

</details>

## Part D: SQL & Transactions (Questions 81-115)


### 81. SQL stands for:
- A) Structured Query Language
- B) Simple Query Language
- C) Standard Query Language
- D) Sequential Query Language

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** SQL is the standard language for relational database management systems.

</details>

### 82. Which SQL command is used to create a table?
- A) CREATE
- B) INSERT
- C) UPDATE
- D) SELECT

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** CREATE is a DDL command used to create database objects like tables.

</details>

### 83. Which SQL command is used to add data to a table?
- A) CREATE
- B) INSERT
- C) UPDATE
- D) SELECT

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** INSERT is a DML command used to add new rows to a table.

</details>

### 84. Which SQL command is used to retrieve data?
- A) CREATE
- B) INSERT
- C) SELECT
- D) DELETE

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** SELECT is used to query and retrieve data from tables.

</details>

### 85. Which SQL command is used to modify existing data?
- A) CREATE
- B) INSERT
- C) UPDATE
- D) DELETE

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** UPDATE is used to modify existing rows in a table.

</details>

### 86. Which SQL command is used to remove rows from a table?
- A) CREATE
- B) INSERT
- C) UPDATE
- D) DELETE

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** DELETE is used to remove rows from a table.

</details>

### 87. Which SQL command is used to remove a table completely?
- A) DELETE
- B) DROP
- C) TRUNCATE
- D) REMOVE

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** DROP removes the table structure and data completely.

</details>

### 88. Which SQL command removes all rows but keeps the table structure?
- A) DELETE
- B) DROP
- C) TRUNCATE
- D) REMOVE

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** TRUNCATE removes all rows but retains the table structure for future use.

</details>

### 89. Which SQL clause is used to filter rows?
- A) WHERE
- B) GROUP BY
- C) ORDER BY
- D) HAVING

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** WHERE filters rows before grouping.

</details>

### 90. Which SQL clause is used to filter groups?
- A) WHERE
- B) GROUP BY
- C) HAVING
- D) ORDER BY

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** HAVING filters groups after GROUP BY.

</details>

### 91. Which SQL clause is used to sort results?
- A) WHERE
- B) GROUP BY
- C) ORDER BY
- D) HAVING

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** ORDER BY sorts the result set in ascending or descending order.

</details>

### 92. Which SQL JOIN returns only matching rows from both tables?
- A) INNER JOIN
- B) LEFT JOIN
- C) RIGHT JOIN
- D) FULL JOIN

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** INNER JOIN returns rows with matching values in both tables.

</details>

### 93. Which SQL JOIN returns all rows from the left table and matching rows from the right?
- A) INNER JOIN
- B) LEFT JOIN
- C) RIGHT JOIN
- D) FULL JOIN

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** LEFT JOIN (LEFT OUTER JOIN) returns all left table rows, with NULLs for non-matching right rows.

</details>

### 94. Which SQL JOIN returns all rows from both tables?
- A) INNER JOIN
- B) LEFT JOIN
- C) RIGHT JOIN
- D) FULL JOIN

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** FULL JOIN returns all rows when there is a match in either table.

</details>

### 95. Which SQL function returns the number of rows?
- A) SUM()
- B) COUNT()
- C) AVG()
- D) MAX()

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** COUNT() returns the number of rows matching the query criteria.

</details>

### 96. Which SQL function returns the average value?
- A) SUM()
- B) COUNT()
- C) AVG()
- D) MAX()

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** C  
> **Explanation:** AVG() calculates the average of a numeric column.

</details>

### 97. Which SQL keyword is used to remove duplicate rows?
- A) UNIQUE
- B) DISTINCT
- C) DIFFERENT
- D) SINGLE

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** DISTINCT eliminates duplicate rows from the result set.

</details>

### 98. What is a transaction in DBMS?
- A) A single SQL query
- B) A logical unit of work
- C) A table
- D) A database

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A transaction is a sequence of operations performed as a single logical unit of work.

</details>

### 99. Which of the following is NOT an ACID property?
- A) Atomicity
- B) Consistency
- C) Isolation
- D) Distribution

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** ACID stands for Atomicity, Consistency, Isolation, and Durability.

</details>

### 100. Atomicity in ACID means:
- A) All operations in a transaction are completed or none
- B) Data is consistent
- C) Transactions are isolated
- D) Data is durable

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Atomicity ensures that a transaction is treated as a single indivisible unit.

</details>

### 101. Consistency in ACID means:
- A) Database remains in a consistent state before and after a transaction
- B) Transactions are isolated
- C) Data is durable
- D) Operations are atomic

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Consistency ensures that the database transitions from one valid state to another.

</details>

### 102. Isolation in ACID means:
- A) Transactions do not interfere with each other
- B) Data is atomic
- C) Data is consistent
- D) Data is durable

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Isolation ensures that concurrent transactions do not affect each other's execution.

</details>

### 103. Durability in ACID means:
- A) Changes made by a committed transaction persist even after a system failure
- B) Transactions are isolated
- C) Operations are atomic
- D) Data is consistent

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** Durability guarantees that committed data is permanently stored.

</details>

### 104. Which SQL command is used to commit a transaction?
- A) COMMIT
- B) ROLLBACK
- C) SAVEPOINT
- D) END

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** COMMIT permanently saves the transaction changes to the database.

</details>

### 105. Which SQL command is used to undo a transaction?
- A) COMMIT
- B) ROLLBACK
- C) SAVEPOINT
- D) UNDO

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** ROLLBACK undoes all changes made in the current transaction.

</details>

### 106. What is a deadlock in DBMS?
- A) Two transactions waiting for each other's locks
- B) A transaction waiting for I/O
- C) A table locked forever
- D) A query taking too long

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A deadlock occurs when two or more transactions are waiting indefinitely for locks held by each other.

</details>

### 107. Which concurrency control technique uses timestamps?
- A) Lock-based
- B) Timestamp-based
- C) Validation-based
- D) All of the above

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Timestamp-based concurrency control assigns timestamps to transactions to order their execution.

</details>

### 108. What is a "dirty read"?
- A) Reading uncommitted data from another transaction
- B) Reading committed data
- C) Reading deleted data
- D) Reading encrypted data

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A dirty read occurs when a transaction reads data modified by another transaction that has not yet committed.

</details>

### 109. What is a "phantom read"?
- A) Reading uncommitted data
- B) A new row appearing in a re-executed query
- C) Reading deleted data
- D) Reading encrypted data

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A phantom read occurs when a transaction re-executes a query and finds new rows inserted by another committed transaction.

</details>

### 110. Which isolation level prevents dirty reads?
- A) Read Uncommitted
- B) Read Committed
- C) Repeatable Read
- D) Serializable

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** Read Committed prevents dirty reads but allows non-repeatable reads.

</details>

### 111. Which isolation level is the strictest?
- A) Read Uncommitted
- B) Read Committed
- C) Repeatable Read
- D) Serializable

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** D  
> **Explanation:** Serializable is the highest isolation level, ensuring complete isolation between transactions.

</details>

### 112. What is a view in SQL?
- A) A physical table
- B) A virtual table based on a SELECT query
- C) An index
- D) A stored procedure

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** B  
> **Explanation:** A view is a virtual table derived from a SELECT statement. It does not store data physically.

</details>

### 113. What is an index in SQL?
- A) A data structure to speed up data retrieval
- B) A table
- C) A view
- D) A trigger

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** An index improves the speed of data retrieval operations on a table.

</details>

### 114. What is a trigger in SQL?
- A) A stored procedure that automatically executes on an event
- B) A type of index
- C) A view
- D) A table

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A trigger is a set of SQL statements that automatically execute in response to certain events (INSERT, UPDATE, DELETE).

</details>

### 115. What is a stored procedure?
- A) A precompiled collection of SQL statements
- B) A type of index
- C) A view
- D) A table

<details>
<summary><b>View Answer & Explanation</b></summary>

> **Answer:** A  
> **Explanation:** A stored procedure is a prepared SQL code that can be saved and reused.

</details>
