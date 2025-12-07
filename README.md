# Class 12 Computer Science - Python Projects

This repository contains a collection of Python programs developed during Class 12. These projects demonstrate understanding of core programming concepts including file handling, data structures, and database connectivity.

## 📂 Project Categories

### 1. Mathematical Operations & Logic
Basic programs implementing mathematical algorithms and logic.

#### `Arthmetic.py`
A menu-driven program to perform basic arithmetic operations (Addition, Subtraction, Multiplication, Division).
**Output:**
```
1. Addition
2. Subraction
3. Multiplication
4. Division
Enter your choice: 1
Enter the First Number: 10
Enter the Second Number: 20
The Addition of two number is: 30
```

#### `FIBONACCI SERIES.py`
Generates the Fibonacci series for a specific number of terms.
**Output:**
```
How many FIBONACCI number you want to display?: 5
0
1
1
2
3
```

#### `Factorial and sum of list.py`
Calculates the factorial of a number and computes the sum of elements in a list.
**Output:**
```
. To FInd Factorial
2. To find sum of LIst elements
Enter your Choice: 1
Enter a number to find Factorial: 5
The Factorial of 5 is: 120
```

#### `MATHEMATICAL FUNCTIONS.py`
Demonstrates the use of the `math` module to compute squares, cubes, square roots, factorials, and logarithms.
**Output:**
```
Enter your choice: 3
Enter a number: 16
The Square Root of 16 is: 4.0
```

#### `RANDOM NUMBER.py`
A simple number guessing game using the `random` module.
**Output:**
```
Guess a number between 1 and 10: 5
You guessed it wrong
Guess a number between 1 and 10: 8
You guessed it right
```

---

### 2. File Handling
Programs to create, read, and manipulate Text, Binary, and CSV files.

#### `TEXT FILE AND DISPLAY.py`
Reads a text file (`textfile.txt`) and analyzes its content to count vowels, consonants, digits, and special characters.
**Output:**
```
Vowels: 12
Consonants: 24
Lower case: 30
Upper case: 5
Digits: 2
Special: 1
```

#### `TEXT FILE.py`
Reads a text file and displays its content with a specific separator (`#`).
**Output:**
```
Hello#World#This#is#Python#
```

#### `CREATE AND SEARCH EMPLOYEE’S RECORD IN CSV FILE..py`
Uses the `csv` module to store and search for employee records.
**Output:**
```
Enter name: John
Enter age: 30
Enter city: New York
Do you want to add more records? (y/n): n
Enter name to search: John
Name: John
Age: 30
City: New York
```

#### `CREATE AND SEARCH RECORDS IN BINARY FILE.py`
Uses the `pickle` module to store and retrieve data in valid binary format.
**Output:**
```
Enter name: Alice
Enter age: 25
Enter city: London
Do you want to add more records? (y/n): n
Enter name to search: Alice
Name: Alice
Age: 25
City: London
```

#### `MODIFY RECORDS IN BINARY FILE.py`
An advanced binary file handler that supports creating, searching, modifying, and deleting records.
**Output:**
```
Enter name to modify: Alice
Enter new age: 26
Enter new city: London
Record updated successfully.
```

---

### 3. Data Structures
Implementation of Stack data structure using Lists and Dictionaries.

#### `IMPLEMENT STACK OPERATIONS(LIST).py`
Implements a Stack (LIFO) for managing Doctor details (ID, Name, Mobile, Specialization). Push operation is restricted to 'ENT' specialists.
**Output:**
```
1. PUSH
2. POP
3. PEEK
4. Disp
Enter your choice: 1
Enter Document ID: 101
Enter The name of the Doctor: Dr. Smith
Enter the mobile Number of the doctore: 9876543210
Enter the specialization: ENT
```

#### `IMPLEMENT STACK OPERATIONS(Dictionary).py`
Demonstrates stack operations where underlying storage is managed/interacted with using Dictionary concepts.
**Output:**
```
Performing Stack Operations using Dictionary

1. PUSH
2. POP
3. PEEK
4. DISPLAY
Enter your choice: 4
Stack is empty
```

---

### 4. Database Management (MySQL)
Scripts to integrate Python with MySQL database for CRUD operations.

#### `INTEGRATE MYSQL WITH PYTHON (CREATING DATABASE AND TABLE).py`
Establishes a connection to MySQL 8.0 server and creates the `employees` database and `employee` table.
**Output:**
```
Database created successfully
Table created successfully
```

#### `INTEGRATE MYSQL WITH PYTHON (INSERTING RECORDS AND DISPLAYING RECORDS).py`
Inserts new employee records into the database and fetches them for display.
**Output:**
```
1. Insert Records
2. Display Records
Enter your choice: 1
Record inserted successfully
```

#### `INTEGRATE MYSQL WITH PYTHON (SEARCHING AND DISPLAYING RECORDS).py`
Searches for specific records in the MySQL database based on queries.
**Output:**
```
Enter name to search: Alex
Name: Alex
Age: 28
Salary: 50000
```

#### `INTEGRATE MYSQL WITH PYTHON (UPDATING RECORDS).py`
Updates existing records (e.g., salary or age) in the database.
**Output:**
```
Enter Employee ID to update: 102
Record updated successfully
```
