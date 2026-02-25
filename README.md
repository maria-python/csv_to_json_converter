# CSV to JSON Converter

Lightweight Python CLI automation tool that converts structured CSV files into formatted JSON output.

Designed to simulate real-world data transformation tasks commonly performed in backend support, API preparation, and data processing workflows.


## Business Problem

In many development and support environments, data is frequently exchanged in CSV format, while modern systems, APIs, and web applications require JSON.

Manual data conversion:
- Is repetitive and time-consuming  
- Introduces formatting inconsistencies  
- Slows down integration workflows  
- Reduces efficiency in backend support operations  

Teams need a simple, reliable data transformation utility that standardizes this process.


## Solution

The CSV to JSON Converter automates structured file transformation using Python.

The system:

- Reads structured CSV files  
- Extracts column headers  
- Converts rows into JSON objects  
- Preserves data integrity  
- Generates formatted (pretty-printed) JSON output  
- Supports command-line arguments for flexible usage  

This ensures consistent and repeatable data conversion suitable for development and integration tasks.


## Key Features

- Converts any CSV file into structured JSON  
- Preserves column headers as JSON keys  
- Pretty-printed JSON output for readability  
- Command-line interface (CLI) support  
- Clean and minimal Python implementation  
- Lightweight and dependency-free (built-in libraries only)  


## Tech Architecture

The project demonstrates:

- File handling in Python  
- Data parsing using the `csv` module  
- JSON serialization using the `json` module  
- Command-line argument handling with `sys.argv`  
- Structured scripting workflow  

The design reflects small internal automation tools used in technical support environments.


## Tech Stack

- Python 3.9.6  
- Built-in libraries:
  - `csv`
  - `json`
  - `sys`


## Project Structure

```
csv_to_json_converter/
│
├── csv_to_json.py       # CLI conversion script
├── sample.csv           # Example input file
├── output.json          # Generated output file
└── README.md
```


## Installation

No external dependencies required.

Clone the repository:

```
git clone https://github.com/yourusername/csv_to_json_converter.git
cd csv_to_json_converter
```


## Usage

Run the script with input and output file arguments:

```
python3 csv_to_json.py input.csv output.json
```


## Workflow

1. Provide a structured CSV file  
2. Run the script via CLI  
3. The system:
   - Reads the CSV file  
   - Maps headers to JSON keys  
   - Converts rows into JSON objects  
   - Saves formatted output to the specified file  


## Results 

- Eliminates manual CSV → JSON formatting  
- Standardizes data transformation workflow  
- Demonstrates CLI tool development skills  
- Simulates real backend support automation tasks  
- Improves integration readiness for APIs and web services  


## Future Improvements

- Enhanced error handling (missing file, invalid format)  
- Support for custom delimiters  
- Type conversion (int, float detection)  
- Logging module integration  
- Packaging as installable CLI tool (`pip`)  
- Unit testing implementation  


## Author

Mariia Ilnitska  

Junior Python Automation / Technical Assistant  

## Contacts

Gmail: maria.ilnitska11@gmail.com  

LinkedIn: www.linkedin.com/in/maria-ilnitska  

Telegram: @mariailnitska
