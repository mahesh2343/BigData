#!/usr/bin/env python
# coding: utf-8

# Q1. What is the purpose of Python's OOP?
# 
# Ans. The purpose of Python's Object-Oriented Programming (OOP) is to provide a flexible and modular approach for modeling real-world entities and their interactions. OOP allows developers to create classes that encapsulate data and behavior, promoting code reusability and maintainability. Through abstraction, OOP simplifies complex systems by focusing on essential features, while encapsulation ensures data security and prevents unauthorized access. Additionally, inheritance and polymorphism facilitate code reuse and flexibility, enabling developers to build efficient and intuitive solutions.

# Q2. Where does an inheritance search look for an attribute?
# 
# Ans. In Python, during an inheritance search for an attribute, the search starts from the instance's class and then moves up the class hierarchy. It looks in the immediate superclass, followed by its superclass, until it reaches the top-most superclass (typically the object class). If the attribute is not found, Python raises an AttributeError.

# Q3. How do you distinguish between a class object and an instance object?
# 
# Ans. A class object in Python represents the class itself and serves as a blueprint for creating instances. It is created when the class keyword is encountered during class definition. An instance object, on the other hand, is a unique object that is created based on the class blueprint and holds its own set of attributes. Instances are created by using the class as a constructor to create individual objects.

# Q4. What makes the first argument in a class’s method function special?
# 
# Ans. The first argument in a class's method function is conventionally named `self` and represents the instance of the class on which the method is called. It allows the method to access and manipulate the instance's attributes and methods. `self` is automatically passed when the method is called, enabling interactions with the specific instance.

# Q5. What is the purpose of the init method?
# 
# Ans. The __init__ method in a Python class is a constructor automatically called when a new instance is created. Its purpose is to initialize the instance's attributes and set its initial state. It allows you to provide default values and customize the object's behavior during object creation.

# Q6. What is the process for creating a class instance?
# 
# Ans. Define the class using the class keyword, specifying its attributes and methods.
# Inside the class, define the __init__ method, which initializes the instance's attributes with provided values.
# Call the class as a constructor, passing the necessary arguments to the __init__ method.
# This call creates a new instance based on the class blueprint with the given attribute values.
# Access the instance's attributes and methods using dot notation for further interactions with the object.

# Q7. What is the process for creating a class?
# 
# Ans. Use the class keyword followed by the class name and a colon.
# Inside the class, define attributes and methods that represent the class's properties and behaviors.
# Optionally, define the __init__ method to initialize the instance's attributes during object creation.
# Instantiate the class by calling the class name as a constructor, which creates instances based on the class blueprint.

# Q8. How would you define the superclasses of a class?
# 
# Ans. To define the superclasses of a class in Python, you specify them inside the parentheses after the class name when defining the class.

# Q9. What is the relationship between classes and modules?
# 
# Ans. A module is a file containing Python code that can include class definitions, functions, and variables.
# Classes are defined within modules to organize and encapsulate related data and behavior.
# Multiple classes can be defined within the same module, making it a convenient way to group related classes together.
# Modules act as containers for classes, providing a namespace to avoid naming conflicts between classes from different modules.
# You can import classes from modules to use them in other parts of the program, promoting code reusability and organization.

# Q10. How do you make instances and classes?
# 
# Ans. Creating a Class: Use the class keyword followed by the class name and a colon to define a class. Inside the class, define attributes and methods that represent the properties and behaviors of the objects you want to create.
# 
# Creating an Instance: To create an instance of the class, call the class name as if it were a function, passing any required arguments to the __init__ method (the constructor). This call will create a new object (instance) based on the class blueprint.
# 
# Eg. # Creating a Class
# class Car:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
# 
#  car_instance = Car("Toyota", "Camry")
# 

# Q11. Where and how should be class attributes created?
# 
# Ans. Class attributes should be created within the class definition and outside of any method. They are defined directly in the class body, typically before any methods.

# Q12. Where and how are instance attributes created?
# 
# Ans. Instance attributes are created inside the __init__ method of a class. The __init__ method is a special method that serves as the constructor for the class, and it is automatically called when a new instance of the class is created.

# Q13. What does the term "self" in a Python class mean?
# 
# Ans. In Python, the term "self" refers to the instance of the class that a method is associated with. It is a conventional name for the first parameter of instance methods within a class.

# Q14. How does a Python class handle operator overloading?
# 
# Ans. In Python, class instances can handle operator overloading by defining special methods for specific operators. These special methods have names surrounded by double underscores, such as __add__ for the + operator or __eq__ for the == operator. When an operator is used on instances of a class, Python looks for the corresponding special method in the class definition to perform the desired operation. By defining these special methods, you can customize how instances of the class respond to specific operators, allowing for more intuitive and meaningful interactions between objects. Operator overloading enables the creation of more expressive and readable code, as it allows you to use familiar operators with user-defined objects, mimicking the behavior of built-in data types.

# Q15. When do you consider allowing operator overloading of your classes?
# 
# Ans. You should consider allowing operator overloading of your classes when you want to provide a more natural and intuitive way to perform operations on instances of your class. By overloading operators, you can make your objects behave like built-in data types and allow them to interact seamlessly with Python's built-in operators. This can enhance code readability and expressiveness, as users of your class can use familiar syntax to perform operations. Operator overloading is particularly useful when your class represents a mathematical or abstract entity, as it allows you to define meaningful operations like addition, subtraction, comparison, and more. However, use operator overloading judiciously, ensuring that it adheres to the principles of clarity and consistency, and only when it makes sense in the context of your class's behavior and intended use cases.

# Q16. What is the most popular form of operator overloading?
# 
# Ans. The most popular form of operator overloading is the addition operator `+`.

# Q17. What are the two most important concepts to grasp in order to comprehend Python OOP code?
# 
# Ans. 1. Classes and Objects 
#      2. Inheritance and polymorphism

# Q18. Describe three applications for exception processing.
# 
# Ans. Three applications for exception processing are:
# 
# 1. *Error Handling:* Exception processing is primarily used for error handling in Python programs. When unexpected or exceptional situations occur during program execution, such as file not found, division by zero, or network errors, exceptions are raised. Properly handling these exceptions using try-except blocks allows the program to gracefully handle errors and prevent abrupt termination.
# 
# 2. *Input Validation:* Exception processing can be utilized for input validation to ensure that user-provided data meets certain criteria. By catching specific exceptions, like ValueError or TypeError, developers can prompt users to re-enter valid input instead of letting the program crash due to invalid data.
# 
# 3. *Resource Cleanup:* In scenarios where resources need to be managed explicitly, such as file handling or database connections, exception processing can help ensure proper cleanup even in the event of errors. Using try-finally or with statements, resources can be released or closed safely regardless of whether an exception is raised during their usage.

# Q19. What happens if you don't do something extra to treat an exception?
# 
# Ans. If an exception is not handled, it will propagate up the call stack until it reaches the top level of the program or encounters a suitable try-except block. If uncaught, the program will terminate with an error message indicating the exception type and traceback. Proper exception handling is essential to prevent program crashes and ensure robustness.

# Q20. What are your options for recovering from an exception in your script?
# 
# Ans. There are 5 ways as follows, 
# 
# Try-Except Block
# Try-Except-Else Block
# Try-Except-Finally Block
# Custom Exception Classes
# Logging and Error Reporting

# Q21. Describe two methods for triggering exceptions in your script.
# 
# Ans. Using the raise statement and Built-in Exception Types

# Q23. What is the purpose of the try statement?
# 
# Ans. The purpose of the try statement is to handle exceptions and prevent program crashes by enclosing potentially error-prone code in a protected block.

# Q24. What are the two most popular try statement variations?
# 
# Ans. Two Most Popular Try Statement Variations:
# 1. try-except
# 2. try-finally

# Q25. What is the purpose of the raise statement?
# 
# Ans. To manually raise exception. 

# Q26. What does the assert statement do, and what other statement is it like?
# 
# Ans. The assert statement in Python checks a condition to ensure that it evaluates to True. If the condition is True, the program continues executing as usual. However, if the condition is False, the assert statement raises an AssertionError, halting the program.
# 
# The assert statement is similar to the if statement, as both involve condition checking. However, assert is primarily used for debugging and testing purposes to catch logical errors, while the if statement is used for controlling the flow of the program based on conditions during regular execution.

# Q27. What is the purpose of the with/as argument, and what other statement is it like?
# 
# Ans. The purpose of the `with/as` statement is to simplify resource management by automatically releasing resources after their usage. It ensures proper cleanup, even in the presence of exceptions. It is similar to the `try/finally` statement but offers a more concise and readable syntax for resource management.

# Q28. What are *args, **kwargs?
# 
# Ans. *args: It allows a function to accept a variable number of positional arguments. When you use *args as a parameter in a function definition, it collects any additional positional arguments passed to the function into a tuple. This allows you to work with an arbitrary number of arguments inside the function.
# 
# **kwargs: It allows a function to accept a variable number of keyword arguments. When you use **kwargs as a parameter in a function definition, it collects any additional keyword arguments passed to the function into a dictionary. This enables you to handle named arguments with arbitrary names and values inside the function.

# Q29. How can I pass optional or keyword parameters from one function to another?
# 
# Ans. We can pass optional or keyword parameters from one function to another by using args and kwargs in the function call. This allows you to forward all variable-length arguments, both positional and keyword, to another function without explicitly specifying them in the function call.

# Q31. Explain Inheritance in Python with an example?
# 
# Ans. Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (subclass) to inherit attributes and methods from another class (superclass). The subclass can then extend or modify the behavior of the superclass while reusing its existing functionality. Inheritance promotes code reusability and helps create a hierarchical structure of classes.
# 
# Eg. class Animal:
#     def __init__(self, species):
#         self.species = species
# 
#     def make_sound(self):
#         pass
# 
# class Dog(Animal):
#     def __init__(self, breed):
#         super().__init__("Dog")
#         self.breed = breed
# 
#     def make_sound(self):
#         return "Woof!"

# Q32. Suppose class C inherits from classes A and B as class C(A,B).Classes A and B both have their own versions of method func(). If we call func() from an object of class C, which version gets invoked?
# 
# Ans. the version from class B would be invoked.

# Q33. Which methods/functions do we use to determine the type of instance and inheritance?
# 
# Ans. Methods/Functions for Determining Type of Instance and Inheritance:
# 
# type() function
# isinstance() function

# Q34.Explain the use of the 'nonlocal' keyword in Python.
# 
# Ans. The 'nonlocal' keyword in Python is used to access and modify variables from an enclosing scope within a nested function, allowing it to avoid creating a new local variable with the same name.

# Q35. What is the global keyword?
# 
# Ans. The 'global' keyword in Python is used to declare that a variable inside a function should refer to the global variable with the same name. It allows you to modify or access global variables from within a function's local scope. Without the 'global' keyword, reassigning a variable inside a function creates a new local variable instead of modifying the global variable.
