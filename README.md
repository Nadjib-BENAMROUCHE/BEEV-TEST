# Data Engineering Use Case Solution

This repository contains the solution for the Data Engineering Use Case provided by Beev. The goal is to analyze market shares in key countries within the automotive industry using sample data. The solution involves setting up a database, importing data from CSV files, performing data quality checks with SQL queries, and implementing a bonus script to visualize car sales trends.

## Instructions

### Prerequisites

Ensure you have the following installed on your system:

- Docker Desktop
- Python (version 3.7+)
- docker-compose

### Steps to Run the Solution

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Nadjib-BENAMROUCHE/BEEV-TEST.git
   cd BEEV-TEST

   
2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt

3. **Start the PostgreSQL Database:**

    ```bash
    docker-compose up -d

4. **Run the Python Script:**

    ```bash
    python3 beev-test.py

5. **Check Data Quality with SQL Queries:**

Review the SQL queries and their results in the provided data_quality.sql file.

6. **Bonus Script:**

Run the bonus script to generate a graph showing the amount of electric vs thermal cars sold per year.

    ```bash
    python3 bonus_script.py


## Project Structure

- 'csv_data': Directory containing sample CSV files.
- 'beev-test.py': Python script for reading, preprocessing, and loading data into the database.
- 'docker-compose.yml': Configuration file for launching a PostgreSQL instance with docker-compose.
- 'data_quality.sql': SQL queries and their results for data quality checks.
- 'bonus_script.py': Bonus script for visualizing car sales trends.
- `requirements.txt`: File specifying Python dependencies required to run the script.
- 'rapport.pdf' : A report explaining the steps taken and difficulties encountered (important).

## Contributing

Contributions are welcome! If you have suggestions, bug fixes, or new features, please open an issue or submit a pull request.

## Author

- Nadjib BENAMROUCHE
