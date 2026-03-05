budget tracker

-FILE STRUCTURE IS BELOW:

budget-tracker/
│
├── models/
│   ├── __init__.py
│   ├── transaction.py       # Task 1
│
├── services/
│   ├── __init__.py
│   ├── budget_manager.py    # Task 2
│   ├── storage_handler.py   # Task 3
│
├── data.json                # auto-generated when app runs
├── main.py                  # Task 4
└── README.md

Question, why this file structure? why these names like __init__.py?

The structure separates code by what it does, not just dumping everything in one file. 
This is called Separation of Concerns and it's one of the most fundamental principles in professional codebases.
budget-tracker/

├── models/          ← "what things ARE" (data shapes)
	-i assume models will store the classes/data.
	-this doesn't do any logic, it simply defines structure
├── services/        ← "what things DO" (business logic)
	-interacting with the data
	-logic classes, ie deals with logic
├── main.py          ← "where it starts" (entry point)
	-just asking user for input, how to use app etc

This structure is a simplified version of a pattern you'll see everywhere in 
professional development called **Layered Architecture**:
```
UI Layer        → main.py          (talks to user)
Service Layer   → services/        (does the work)
Data Layer      → models/          (defines the data)
Storage Layer   → storage_handler  (reads/writes data)