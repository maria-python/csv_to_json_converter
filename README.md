# CSV to MySQL Loader

Backend automation tool that securely loads structured CSV data into a MySQL database with validation, transaction handling, and execution logging.

Designed to simulate real-world data ingestion workflows performed by technical support and backend teams.


## Business Problem

In many IT teams, structured data (reports, exports, logs, external datasets) is delivered in CSV format and must be manually imported into relational databases.

Manual import processes:
- Increase the risk of human error  
- Lack validation and consistency  
- Are inefficient for recurring workflows  
- Provide limited visibility into failures  

Teams need a reliable and repeatable data ingestion process.


## Solution

The **CSV to MySQL Loader** automates structured data ingestion into a MySQL database using Python.

The system:

- Reads structured CSV input files  
- Validates and prepares records  
- Establishes a secure database connection  
- Automatically creates a target table (if missing)  
- Inserts records using parameterized SQL queries  
- Handles transactions with proper commit/rollback logic  
- Logs execution status for monitoring and debugging  

This ensures safe, repeatable, and production-style data loading.


## Key Features

- Secure MySQL integration using `mysql-connector-python`  
- Parameterized queries (SQL injection prevention)  
- Transaction control (commit / rollback)  
- Automatic table creation  
- Structured error handling  
- Clean modular code separation  
- Backend workflow simulation  
- Logging of execution results  


## Tech Architecture

The project follows a modular structure separating:

- Database configuration  
- Connection management  
- Data processing logic  
- Execution control  

This mirrors real backend support environments where maintainability and clarity are essential.


## Tech Stack

- Python 3.9.6  
- MySQL  
- mysql-connector-python  
- CSV module
  

## Project Structure

```
csv_to_mysql_loader/
│
├── main.py              # Entry point
├── db_config.py         # Database configuration
├── sample.csv           # Example input dataset
├── requirements.txt
└── README.md
```


## Installation

1. Clone the repository:

```
git clone https://github.com/maria-python/csv_to_mysql_loader.git
cd csv_to_mysql_loader
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Configure database credentials inside `db_config.py`  
4. Ensure the target MySQL database exists  


## Usage

Run the script:

```
python main.py
```

### Workflow:

1. Place structured CSV file in the project directory  
2. Run the loader script  
3. The system:
   - Connects to MySQL  
   - Creates the target table (if needed)  
   - Inserts validated records  
   - Commits the transaction  
   - Logs the execution result  


## Results 

- Eliminates manual database imports  
- Reduces data entry errors  
- Demonstrates backend automation workflow  
- Simulates real IT technical assistant responsibilities  
- Improves data ingestion reliability  


## Future Improvements

- CLI arguments for dynamic file selection  
- Batch insert optimization for large datasets  
- Logging module integration  
- Docker containerization  
- Scheduled automation via cron  
- Integration with cloud databases  


## Author
