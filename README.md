# Main Topic: AirBnB clone - The console

The goal of the project is to deploy on your server a simple copy of the AirBnB website.
At the end of the project we will have a complete web application composed by:

•	A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)

•	A website (the front-end) that shows the final product to everybody: static and dynamic

•	A database or files that store data (data = objects)

•	An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## Subtopic 1: First step: Write a command interpreter to manage your AirBnB objects.

This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…
Each task is linked and will help you to:

•	put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances

•	create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file

•	create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel

•	create the first abstracted storage engine of the project: File storage.

•	create all unittests to validate all our classes and storage engine

## Subtopic 2: What’s a command interpreter?

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

•	Create a new object (ex: a new User or a new Place)

•	Retrieve an object from a file, a database etc…

•	Do operations on objects (count, compute stats, etc…)

•	Update attributes of an object

•	Destroy an object

## Subtopic 3: Execution

Your shell should work like this in interactive mode:

$ ./console.py

(hbnb) help

Documented commands (type help <topic>):
========================================

EOF  help  quit

(hbnb)
 
(hbnb)

(hbnb) quit

$

But also in non-interactive mode:

$ echo "help" | ./console.py

(hbnb)

Documented commands (type help <topic>):
========================================

EOF  help  quit

(hbnb)

$

$ cat test_help

help

$

$ cat test_help | ./console.py

(hbnb)


Documented commands (type help <topic>):
========================================

EOF  help  quit

(hbnb)

$

## Subtopic 4: Testing

Unittests for the AirBnB clone  project are defined in the tests folder.
All your tests should be executed by using this command:

$ python3 -m unittest discover tests

You can also test file by file by using this command:

$ python3 -m unittest tests/test_models/test_base_model.py

All tests should also pass in non-interactive mode:

$ echo "python3 -m unittest discover tests" | bash

