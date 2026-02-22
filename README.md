# CSV to JSON Converter

A lightweight Python CLI utility that converts CSV files into structured JSON format.

## Overview

This project demonstrates:
- File handling in Python
- Working with built-in `csv` and `json` modules
- Command-line arguments (`sys.argv`)
- Basic data transformation

## Features

- Converts any CSV file into JSON
- Preserves column headers as JSON keys
- Pretty-prints JSON output
- Simple command-line usage


## Project Structure

```
csv_to_json_converter/
│
├── csv_to_json.py
├── sample.csv
├── output.json
└── README.md
```

## How to Run

1. Navigate to the project folder:

```bash
cd csv_to_json_converter
```

2. Run the script:

```bash
python3 csv_to_json.py input.csv output.json
```

Example:

```bash
python3 csv_to_json.py sample.csv output.json
```

## Example Input (sample.csv)

```csv
name,age,city
Maria,23,Madrid
Alex,30,London
John,28,New York
```

## Example Output (output.json)

```json
[
    {
        "name": "Maria",
        "age": "23",
        "city": "Madrid"
    },
    {
        "name": "Alex",
        "age": "30",
        "city": "London"
    },
    {
        "name": "John",
        "age": "28",
        "city": "New York"
    }
]
```

## Tech Stack

- Python 3.9.6
- Built-in libraries:
  - `csv`
  - `json`
  - `sys`

## Why This Project?

This project was created as part of hands-on practice with:

- Python scripting
- Data transformation
- CLI tool development
- Git & GitHub workflow

## Future Improvements

- Add error handling (missing file, wrong format)
- Support custom delimiters
- Add logging
- Package as installable CLI tool

## The Author

Mariia Ilnitska

Junior Python Automation / Tech Assistant

## ✉️ Contacts

Gmail: maria.ladesigner@gmail.com

LinkedIn: www.linkedin.com/in/maria-ilnitska

Telegram: @mariailnitska
