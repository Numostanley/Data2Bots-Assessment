The objective of this project is to :

Write a generic program that:
- Read the JSON files present in this location (./data/)
- Sniff the schema of the JSON files, and
- Dumps the output in (./schema/)

The project can be executed by running the following command from the root directory;
```
python -m main
```
Also, the unittests of this project can be executed by running the following command from the root directory;
```
python -m unittest tests
```
It is noteworthy to state that a FileNotFoundError will be raised if an invalid file path or file is inputted.
This exception was not handled intentionally for testing purpose.

# Note: The python version needed to successfully execute this code is python3 and above.
