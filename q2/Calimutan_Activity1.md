# Activity 1: Fundamentals of Object-Oriented Programming - Inheritance

## 1. What is/are the parent class/es of the Programmer class in the video?
In standard object-oriented programming hierarchy examples (such as workplace/employee models), the parent class of the **Programmer** class is **Employee** (which in turn inherits from a broader **Person** or **Staff** base class). The `Programmer` class inherits common attributes such as `name`, `age`, and `salary` from its parent, while introducing specialized attributes and behaviors unique to software developers.

## 2. If you were to add a new role called Intern, where would you place it in the inheritance hierarchy? Why?
An **Intern** class would be placed as a child class of **Employee** (or directly under `Staff`), on the same hierarchical level as `Programmer` or `Manager`. 
* **Why:** An intern shares all the fundamental characteristics of an employee (such as a `name`, `age`, `employee_id`, and contact information), making code reuse through inheritance ideal. However, an intern also has distinct attributes (such as `university`, `internship_duration`, or `mentor`) and specific behaviors that differentiate them from full-time programmers or managers.
