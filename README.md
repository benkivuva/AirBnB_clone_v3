# AirBnB Clone - The Console

The console is the first segment of the AirBnB project at Holberton School that collectively covers fundamental concepts of higher level programming. The goal of the AirBnB project is to eventually deploy our server as a simple copy of the AirBnB Website (HBnB). A command interpreter is created in this segment to manage objects for the AirBnB (HBnB) website.

## Functionalities of this command interpreter:

- Create a new object (e.g., a new User or a new Place).
- Retrieve an object from a file, a database, etc.
- Perform operations on objects (count, compute stats, etc.).
- Update attributes of an object.
- Destroy an object.

## Table of Contents

- [Environment](#environment)
- [Installation](#installation)
- [File Descriptions](#file-descriptions)
- [Usage](#usage)
- [Examples of Use](#examples-of-use)
- [Bugs](#bugs)
- [Authors](#authors)
- [License](#license)

## Environment

This project is interpreted and tested on Ubuntu 14.04 LTS using Python 3 (version 3.4.3).

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/alexaorrico/AirBnB_clone.git
   ```

2. Access the AirBnb directory:

   ```bash
   cd AirBnB_clone
   ```

3. Run the console interactively:

   ```bash
   ./console
   ```

   And enter your commands.

4. Run the console non-interactively:

   ```bash
   echo "<command>" | ./console.py
   ```

## File Descriptions

### console.py

The console contains the entry point of the command interpreter. List of commands this console currently supports:

- `EOF` - Exits the console.
- `quit` - Exits the console.
- `<emptyline>` - Overwrites the default empty line method and does nothing.
- `create` - Creates a new instance of `BaseModel`, saves it (to the JSON file), and prints the ID.
- `destroy` - Deletes an instance based on the class name and ID (saves the change into the JSON file).
- `show` - Prints the string representation of an instance based on the class name and ID.
- `all` - Prints all string representations of all instances based on or not based on the class name.
- `update` - Updates an instance based on the class name and ID by adding or updating attributes (saves the change into the JSON file).

### models/ Directory

This directory contains classes used for this project:

#### base_model.py

The BaseModel class from which future classes will be derived. It includes methods for initialization, string representation, saving, and conversion to a dictionary.

Classes inherited from Base Model:

- amenity.py
- city.py
- place.py
- review.py
- state.py
- user.py

### models/engine/ Directory

This directory contains the File Storage class that handles JSON serialization and deserialization:

#### file_storage.py

- `all(self)` - Returns the dictionary __objects.
- `new(self, obj)` - Sets in __objects the obj with the key `<obj class name>.id`.
- `save(self)` - Serializes __objects to the JSON file (path: __file_path).
- `reload(self)` - Deserializes the JSON file to __objects.

## Tests Directory

The `/tests` directory contains all unit test cases for this project:

- `/test_models/test_base_model.py` - Contains the TestBaseModel and TestBaseModelDocs classes.
  - TestBaseModelDocs class:
    - PEP8 conformance tests
    - Module and class docstring tests
  - TestBaseModel class:
    - Tests for BaseModel instantiation and attributes

- `/test_models/test_amenity.py` - Contains the TestAmenityDocs class:
  - PEP8 conformance tests
  - Module and class docstring tests

- `/test_models/test_city.py` - Contains the TestCityDocs class:
  - PEP8 conformance tests
  - Module and class docstring tests

- `/test_models/test_file_storage.py` - Contains the TestFileStorageDocs class:
  - PEP8 conformance tests
  - Module and class docstring tests

- `/test_models/test_place.py` - Contains the TestPlaceDocs class:
  - PEP8 conformance tests
  - Module and class docstring tests

- `/test_models/test_review.py` - Contains the TestReviewDocs class:
  - PEP8 conformance tests
  - Module and class docstring tests

- `/test_models/test_state.py` - Contains the TestStateDocs class:
  - PEP8 conformance tests
  - Module and class docstring tests

- `/test_models/test_user.py` - Contains the TestUserDocs class:
  - PEP8 conformance tests
  - Module and class docstring tests

## Examples of Use

```bash
vagrantAirBnB_clone$./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) all MyModel
** class doesn't exist **
(hbnb) create BaseModel
7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) all BaseModel
[[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}]
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}
(hbnb) destroy BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
** no instance found **
(hbnb) quit
```

## Bugs

No known bugs at this time.

## Authors

- Mohammad Hassieb - [Github](https://github.com/hassiebb)
- Ben Kivuva - [Github](https://github.com/benkivuva)

## License

Public Domain. No copyright protection.
