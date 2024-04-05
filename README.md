//# AirBnB Imitation - The Command Interface
The console stands as the foremost segment of the AirBnB endeavor at Holberton School, purposed to collectively cover the foundational concepts of advanced programming. The objective of the AirBnB endeavor is to ultimately deploy our server as a modest replica of the AirBnB Website (HBnB). This segment encompasses a command interpreter tailored to manage objects for the AirBnB (HBnB) website.

#### Functions of this command interpreter:
* Establish a new object (e.g., a new User or a new Place)
* Retrieve an object from a file, a database, etc...
* Perform operations on objects (count, compute stats, etc...)
* Modify attributes of an object
* Eradicate an object

## Table of Contents
* [Environment](#environment)
* [Installation](#installation)
* [File Descriptions](#file-descriptions)
* [Usage](#usage)
* [Examples of Usage](#examples-of-usage)
* [Issues](#issues)
* [Authors](#authors)
* [License](#license)

## Environment
This endeavor is interpreted and tested on Ubuntu 14.04 LTS utilizing Python 3 (version 3.4.3).

## Installation
* Replicate this repository: `git clone "https://github.com/alexaorrico/AirBnB_clone.git"`
* Access the AirBnB directory: `cd AirBnB_clone`
* Launch hbnb (interactively): `./console` and input command
* Execute hbnb (non-interactively): `echo "<command>" | ./console.py`

## File Descriptions
[console.py](console.py) - The console serves as the entry point of the command interpreter. 
List of commands supported by this console presently:
* `EOF` - ceases console operation 
* `quit` - ceases console operation
* `<emptyline>` - supersedes default emptyline method and takes no action
* `create` - Creates a new instance of `BaseModel`, saves it (to the JSON file), and prints the id
* `destroy` - Deletes an instance based on the class name and id (saves the change into the JSON file). 
* `show` - Prints the string representation of an instance based on the class name and id.
* `all` - Prints all string representations of all instances based or not on the class name. 
* `update` - Updates an instance based on the class name and id by adding or updating attributes (saves the change into the JSON file). 

#### `models/` directory encompasses classes employed for this project:
[base_model.py](/models/base_model.py) - The BaseModel class from which future classes will derive
* `def __init__(self, *args, **kwargs)` - Initialization of the base model
* `def __str__(self)` - String representation of the BaseModel class
* `def save(self)` - Updates the attribute `updated_at` with the current datetime
* `def to_dict(self)` - Returns a dictionary containing all keys/values of the instance

Classes inherited from Base Model:
* [amenity.py](/models/amenity.py)
* [city.py](/models/city.py)
* [place.py](/models/place.py)
* [review.py](/models/review.py)
* [state.py](/models/state.py)
* [user.py](/models/user.py)

#### `/models/engine` directory houses the File Storage class that manages JSON serialization and deserialization :
[file_storage.py](/models/engine/file_storage.py) - Serializes instances to a JSON file & deserializes back to instances
* `def all(self)` - Returns the dictionary __objects
* `def new(self, obj)` - Sets in __objects the obj with key <obj class name>.id
* `def save(self)` - Serializes __objects to the JSON file (path: __file_path)
* ` def reload(self)` -  Deserializes the JSON file to __objects

#### `/tests` directory holds all unit test cases for this project:
[/test_models/test_base_model.py](/tests/test_models/test_base_model.py) - Contains the TestBaseModel and TestBaseModelDocs classes
TestBaseModelDocs class:
* `def setUpClass(cls)`- Preparation for the doc tests
* `def test_pep8_conformance_base_model(self)` - Confirms models/base_model.py conforms to PEP8
* `def test_pep8_conformance_test_base_model(self)` - Confirms tests/test_models/test_base_model.py conforms to PEP8
* `def test_bm_module_docstring(self)` - Checks for the base_model.py module docstring
* `def test_bm_class_docstring(self)` - Verifies the BaseModel class docstring
* `def test_bm_func_docstrings(self)` - Ensures presence of docstrings in BaseModel methods

TestBaseModel class:
* `def test_is_base_model(self)` - Confirms instantiation of a BaseModel works
* `def test_created_at_instantiation(self)` - Checks if created_at is a public instance attribute of type datetime
* `def test_updated_at_instantiation(self)` - Checks if updated_at is a public instance attribute of type datetime
* `def test_diff_datetime_objs(self)` - Verifies that two BaseModel instances have different datetime objects

[/test_models/test_amenity.py](/tests/test_models/test_amenity.py) - Contains the TestAmenityDocs class:
* `def setUpClass(cls)` - Preparation for the doc tests
* `def test_pep8_conformance_amenity(self)` - Confirms models/amenity.py conforms to PEP8
* `def test_pep8_conformance_test_amenity(self)` - Confirms tests/test_models/test_amenity.py conforms to PEP8
* `def test_amenity_module_docstring(self)` - Checks for the amenity.py module docstring
* `def test_amenity_class_docstring(self)` - Verifies the Amenity class docstring

[/test_models/test_city.py](/tests/test_models/test_city.py) - Contains the TestCityDocs class:
* `def setUpClass(cls)` - Preparation for the doc tests
* `def test_pep8_conformance_city(self)` - Confirms models/city.py conforms to PEP8
* `def test_pep8_conformance_test_city(self)` - Confirms tests/test_models/test_city.py conforms to PEP8
* `def test_city_module_docstring(self)` - Checks for the city.py module docstring
* `def test_city_class_docstring(self)` - Verifies the City class docstring

[/test_models/test_file_storage.py](/tests/test_models/test_file_storage.py) - Contains the TestFileStorageDocs class:
* `def setUpClass(cls)` - Preparation for the doc tests
* `def test_pep8_conformance_file_storage(self)` - Confirms models/file_storage.py conforms to PEP8
* `def test_pep8_conformance_test_file_storage(self)` - Confirms tests/test_models/test_file_storage.py conforms to PEP8
* `def test_file_storage_module_docstring(self)` - Checks for the file_storage.py module docstring
* `def test_file_storage_class_docstring(self)` - Verifies the FileStorage class docstring

