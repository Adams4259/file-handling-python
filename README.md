# File Handling in Python

This project demonstrates various file handling operations in Python, including reading, writing, appending, and managing different file formats (TXT, CSV, JSON).

## Features
- Open and read text files
- Write and append data to files
- Handle CSV files using `csv` module
- Manage JSON files using `json` module
- Error handling for file operations

## Requirements
Ensure you have Python installed (version 3.6+ recommended).

## Installation
Clone the repository and navigate to the project directory:

```sh
git clone https://github.com/Adams4259/file-handling-python.git
cd file-handling-python
```

## Usage
Run the provided scripts to test different file operations:

```sh
python file_read.py  # Reads a file
python file_write.py # Writes to a file
python file_csv.py   # Handles CSV files
python file_json.py  # Handles JSON files
```

## Example Code
### Reading a File
```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

### Writing to a File
```python
with open("example.txt", "w") as file:
    file.write("Hello, File Handling in Python!")
```

### Handling CSV Files
```python
import csv

with open("data.csv", mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

### Handling JSON Files
```python
import json

data = {"name": "John", "age": 30}

with open("data.json", "w") as file:
    json.dump(data, file)
```

## Contributing
Feel free to fork this repository, submit issues, or suggest improvements.

## License
This project is open-source and available under the MIT License.

