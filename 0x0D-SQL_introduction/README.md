Readme of 0x0D-SQL_introduction

This is an introduction to SQL scripting.

##Task 0: Listing Databases##
===================================================
Script to list all databases of MySQL server

Input
```
0-list_databases.sql | mysql -hlocalhost -uroot -p
```

Output
```
Enter password: 
Database                                                                                     
hbtn_0c_0                                                                                    
information_schema                                                                           
mysql                                                                                        
performance_schema                                                                           
sys        
```

Additional Information

-   Ensure that the MySQL server is running before executing the script.
-   Make sure to replace -hlocalhost, -uroot, and -p with the appropriate host, username, and password if they differ in your MySQL setup.

---

---

# Task 1: Create a Database if Missing
==========================================================

## Objective

The objective of this task is to create the database `hbtn_0c_0` on the MySQL server. If the database already exists, the script should not fail.

## Instructions

### Step 1: Create the SQL Script

Create a file named `1-create_database_if_missing.sql` with the following content:

```sql
-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
```

### Step 2: Execute the Script

Run the script using the following command in the terminal:

```bash
cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
```

You will be prompted to enter the MySQL root password.

### Step 3: Verify Database Creation

After entering the password, the script will execute and create the database `hbtn_0c_0` if it doesn't already exist. If the database already exists, the script will not fail.

Example Output:

```plaintext
Enter password:
```

## Additional Information

- Ensure that the MySQL server is running before executing the script.
- Make sure to replace `-hlocalhost`, `-uroot`, and `-p` with the appropriate host, username, and password if they differ in your MySQL setup.
- The script uses the `CREATE DATABASE IF NOT EXISTS` statement to create the database only if it doesn't already exist.

## Troubleshooting

If you encounter any issues, verify the following:

- MySQL server is running.
- You have the correct root credentials.
- The script file (`1-create_database_if_missing.sql`) is in the correct location.

---

---

# Task 2: Remove a Database
===========================================================

## Objective

The objective of this task is to create a script that deletes the `hbtn_0c_0` database from the MySQL server. If the database `hbtn_0c_0` doesn't exist, the script should not fail.

## Prerequisites

- MySQL 8.0 is installed on Ubuntu 20.04 LTS.
- Access to the MySQL server with the root user credentials.

## Instructions

### Step 1: Create the SQL Script

Create a file named `2-remove_database.sql` with the following content:

```sql
-- Drop database if it exists
DROP DATABASE IF EXISTS hbtn_0c_0;
```

### Step 2: Execute the Script

Run the script using the following command in the terminal:

```bash
cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
```

You will be prompted to enter the MySQL root password.

### Step 3: Verify Database Removal

After entering the password, the script will execute and attempt to delete the `hbtn_0c_0` database. If the database doesn't exist, the script will not fail.

Example Output:

```plaintext
Enter password:
```

## Additional Information

- Ensure that the MySQL server is running before executing the script.
- Make sure to replace `-hlocalhost`, `-uroot`, and `-p` with the appropriate host, username, and password if they differ in your MySQL setup.
- The script uses the `DROP DATABASE IF EXISTS` statement to delete the database only if it exists.

## Troubleshooting

If you encounter any issues, verify the following:

- MySQL server is running.
- You have the correct root credentials.
- The script file (`2-remove_database.sql`) is in the correct location.

---

---

# Task 3: List Tables in a Database
=======================================================

## Objective

The objective of this task is to create a script that lists all the tables in a specified database on the MySQL server. The database name will be passed as an argument to the `mysql` command.

## Instructions

### Step 1: Create the SQL Script

Create a file named `3-list_tables.sql` with the following content:

```sql
-- List all tables in the specified database
SHOW TABLES;
```

### Step 2: Execute the Script

Run the script by passing the database name as an argument to the `mysql` command. Use the following command in the terminal:

```bash
cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
```

You will be prompted to enter the MySQL root password.

### Step 3: Verify Table Listing

After entering the password, the script will execute and list all the tables in the specified database (`mysql` in the example).

Example Output:

```plaintext
Enter password:
Tables_in_mysql
columns_priv
component
db
default_roles
engine_cost
func
general_log
...
user
```

## Additional Information

- Ensure that the MySQL server is running before executing the script.
- Make sure to replace `-hlocalhost`, `-uroot`, and `-p` with the appropriate host, username, and password if they differ in your MySQL setup.
- The script uses the `SHOW TABLES;` statement to display a list of all tables in the specified database.

## Troubleshooting

If you encounter any issues, verify the following:

- MySQL server is running.
- You have the correct root credentials.
- The script file (`3-list_tables.sql`) is in the correct location.

---

---

# Task 4: Create Table `first_table`
=============================================================

## Objective

The objective of this task is to create a table named `first_table` in the current database on the MySQL server. If the table already exists, the script should not fail.

## Instructions

### Step 1: Create the SQL Script

Create a file named `4-first_table.sql` with the following content:

```sql
-- Create table if it doesn't exist
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
```

### Step 2: Execute the Script

Run the script by passing the database name as an argument to the `mysql` command. Use the following command in the terminal:

```bash
cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

You will be prompted to enter the MySQL root password.

### Step 3: Verify Table Creation

After entering the password, the script will execute and create the `first_table` in the specified database (`hbtn_0c_0` in the example). If the table already exists, the script will not fail.

Example Output:

```plaintext
Enter password:
```

## Additional Information

- Ensure that the MySQL server is running before executing the script.
- Make sure to replace `-hlocalhost`, `-uroot`, and `-p` with the appropriate host, username, and password if they differ in your MySQL setup.
- The script uses the `CREATE TABLE IF NOT EXISTS` statement to create the table only if it doesn't already exist.
- The `name` column is defined as `VARCHAR(256)`, allowing variable-length character strings with a maximum length of 256 characters.

## Troubleshooting

If you encounter any issues, verify the following:

- MySQL server is running.
- You have the correct root credentials.
- The script file (`4-first_table.sql`) is in the correct location.

---

---

# Task 5: Print Full Table Description

## Objective

The objective of this task is to create a script that prints the full description of the table `first_table` from the database `hbtn_0c_0` on the MySQL server.

## Instructions

### Step 1: Create the SQL Script

Create a file named `5-full_table.sql` with the following content:

```sql
-- Print full table description
SHOW CREATE TABLE first_table;
```

### Step 2: Execute the Script

Run the script by passing the database name as an argument to the `mysql` command. Use the following command in the terminal:

```bash
cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

You will be prompted to enter the MySQL root password.

### Step 3: Verify Table Description

After entering the password, the script will execute and print the full description of the `first_table` in the specified database (`hbtn_0c_0` in the example).

Example Output:

```plaintext
Enter password:
Table   Create Table
first_table     CREATE TABLE `first_table` (\n  `id` int DEFAULT NULL,\n  `name` varchar(256) DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

## Additional Information

- Ensure that the MySQL server is running before executing the script.
- Make sure to replace `-hlocalhost`, `-uroot`, and `-p` with the appropriate host, username, and password if they differ in your MySQL setup.
- The script uses the `SHOW CREATE TABLE` statement to display the CREATE TABLE statement that includes the full table description.

## Troubleshooting

If you encounter any issues, verify the following:

- MySQL server is running.
- You have the correct root credentials.
- The script file (`5-full_table.sql`) is in the correct location.

---

---

# Task 6: List All Rows of `first_table`
==================================================

## Objective

The objective of this task is to create a script that lists all rows of the table `first_table` from the database `hbtn_0c_0` on the MySQL server. All fields (columns) should be printed.

## Instructions

### Step 1: Create the SQL Script

Create a file named `6-list_values.sql` with the following content:

```sql
-- List all rows of the table first_table
SELECT * FROM first_table;
```

### Step 2: Execute the Script

Run the script by passing the database name as an argument to the `mysql` command. Use the following command in the terminal:

```bash
cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

You will be prompted to enter the MySQL root password.

### Step 3: Verify Row Listing

After entering the password, the script will execute and list all rows of the `first_table` in the specified database (`hbtn_0c_0` in the example). All fields (columns) will be printed.

Example Output:

```plaintext
Enter password:
id  | name
1   | John
2   | Alice
3   | Bob
...
```

## Additional Information

- Ensure that the MySQL server is running before executing the script.
- Make sure to replace `-hlocalhost`, `-uroot`, and `-p` with the appropriate host, username, and password if they differ in your MySQL setup.
- The script uses the `SELECT * FROM first_table;` statement to retrieve all rows and columns from the specified table.

## Troubleshooting

If you encounter any issues, verify the following:

- MySQL server is running.
- You have the correct root credentials.
- The script file (`6-list_values.sql`) is in the correct location.

---

---

# Task 7: Insert a New Row into `first_table`
==========================================================

## Objective

The objective of this task is to create a script that inserts a new row into the table `first_table` from the database `hbtn_0c_0` on the MySQL server.

## Instructions

### Step 1: Create the SQL Script

Create a file named `7-insert_value.sql` with the following content:

```sql
-- Insert a new row into the table first_table
INSERT INTO first_table (id, name) VALUES (89, 'Best School');
```

### Step 2: Execute the Script

Run the script by passing the database name as an argument to the `mysql` command. Use the following command in the terminal:

```bash
cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

You will be prompted to enter the MySQL root password.

### Step 3: Verify Row Insertion

After entering the password, the script will execute and insert a new row into the `first_table` in the specified database (`hbtn_0c_0` in the example).

Example Output:

```plaintext
Enter password:
```

### Step 4: Verify Insertion by Listing Values

To verify the insertion, you can list all values in the table using the following command:

```bash
cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

## Additional Information

- Ensure that the MySQL server is running before executing the script.
- Make sure to replace `-hlocalhost`, `-uroot`, and `-p` with the appropriate host, username, and password if they differ in your MySQL setup.
- The script uses the `INSERT INTO` statement to add a new row with the specified values into the `first_table`.

## Troubleshooting

If you encounter any issues, verify the following:

- MySQL server is running.
- You have the correct root credentials.
- The script file (`7-insert_value.sql`) is in the correct location.

---

---

# Task 8: Display Count of Records with `id = 89`
=====================================================

## Objective

The objective of this task is to create a script that displays the number of records with `id = 89` in the table `first_table` from the database `hbtn_0c_0` on the MySQL server.

## Instructions

### Step 1: Create the SQL Script

Create a file named `8-count_89.sql` with the following content:

```sql
-- Display the number of records with id = 89
SELECT COUNT(*) FROM first_table WHERE id = 89;
```

### Step 2: Execute the Script

Run the script by passing the database name as an argument to the `mysql` command. Use the following command in the terminal:

```bash
cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
```

You will be prompted to enter the MySQL root password.

### Step 3: View Count of Records

After entering the password, the script will execute, and the count of records with `id = 89` will be displayed.

Example Output:

```plaintext
Enter password:
3
```

## Additional Information

- Ensure that the MySQL server is running before executing the script.
- Make sure to replace `-hlocalhost`, `-uroot`, and `-p` with the appropriate host, username, and password if they differ in your MySQL setup.
- The script uses the `SELECT COUNT(*) FROM first_table WHERE id = 89;` statement to retrieve the count of records that match the specified condition.

## Troubleshooting

If you encounter any issues, verify the following:

- MySQL server is running.
- You have the correct root credentials.
- The script file (`8-count_89.sql`) is in the correct location.

---

---

# Task 9: Create `second_table` and Add Multiple Rows
==========================================================

## Objective

The objective of this task is to create a script that creates a table named `second_table` in the database `hbtn_0c_0` on the MySQL server. Additionally, the script should add multiple rows to this table with specified values.

## Instructions

### Step 1: Create the SQL Script

Create a file named `9-full_creation.sql` with the following content:

```sql
-- Create table if it doesn't exist
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Insert multiple rows into second_table
INSERT INTO second_table (id, name, score) VALUES
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);
```

### Step 2: Execute the Script

Run the script by passing the database name as an argument to the `mysql` command. Use the following command in the terminal:

```bash
cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

You will be prompted to enter the MySQL root password.

### Step 3: Verify Table Creation and Row Insertion

After entering the password, the script will execute, and the table `second_table` will be created if it doesn't already exist. Additionally, multiple rows with the specified values will be added to the table.

Example Output:

```plaintext
Enter password:
```

## Additional Information

- Ensure that the MySQL server is running before executing the script.
- Make sure to replace `-hlocalhost`, `-uroot`, and `-p` with the appropriate host, username, and password if they differ in your MySQL setup.
- The script uses the `CREATE TABLE IF NOT EXISTS` statement to create the table only if it doesn't already exist.
- The `INSERT INTO` statement adds multiple rows with specified values into the `second_table`.

## Troubleshooting

If you encounter any issues, verify the following:

- MySQL server is running.
- You have the correct root credentials.
- The script file (`9-full_creation.sql`) is in the correct location.

---

---

# Task 10: List Records of `second_table` Ordered by Top Score
==================================================================

## Objective

The objective of this task is to create a script that lists all records of the table `second_table` from the database `hbtn_0c_0` on the MySQL server. The results should display both the score and the name, and the records should be ordered by score in descending order (top scores first).

## Instructions

### Step 1: Create the SQL Script

Create a file named `10-top_score.sql` with the following content:

```sql
-- List all records of the table second_table
SELECT score, name FROM second_table ORDER BY score DESC;
```

### Step 2: Execute the Script

Run the script by passing the database name as an argument to the `mysql` command. Use the following command in the terminal:

```bash
cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

You will be prompted to enter the MySQL root password.

### Step 3: View Records Ordered by Top Score

After entering the password, the script will execute, and the records of the `second_table` will be listed with both scores and names. The records will be ordered by score in descending order, displaying the top scores first.

Example Output:

```plaintext
Enter password:
score   name
14      Bob
10      John
8       George
3       Alex
```

## Additional Information

- Ensure that the MySQL server is running before executing the script.
- Make sure to replace `-hlocalhost`, `-uroot`, and `-p` with the appropriate host, username, and password if they differ in your MySQL setup.
- The script uses the `SELECT score, name FROM second_table ORDER BY score DESC;` statement to retrieve and order the records.

## Troubleshooting

If you encounter any issues, verify the following:

- MySQL server is running.
- You have the correct root credentials.
- The script file (`10-top_score.sql`) is in the correct location.

---

---

# Task 11: List Records with Score >= 10 in `second_table`
=============================================================

## Objective

The objective of this task is to create a script that lists all records with a score greater than or equal to 10 in the table `second_table` from the database `hbtn_0c_0` on the MySQL server. The results should display both the score and the name, and the records should be ordered by score in descending order (top scores first).

## Instructions

### Step 1: Create the SQL Script

Create a file named `11-best_score.sql` with the following content:

```sql
-- List records with a score >= 10 in the table second_table
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
```

### Step 2: Execute the Script

Run the script by passing the database name as an argument to the `mysql` command. Use the following command in the terminal:

```bash
cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

You will be prompted to enter the MySQL root password.

### Step 3: View Records with Score >= 10

After entering the password, the script will execute, and the records of the `second_table` with a score greater than or equal to 10 will be listed with both scores and names. The records will be ordered by score in descending order, displaying the top scores first.

Example Output:

```plaintext
Enter password:
score   name
14      Bob
10      John
```

## Additional Information

- Ensure that the MySQL server is running before executing the script.
- Make sure to replace `-hlocalhost`, `-uroot`, and `-p` with the appropriate host, username, and password if they differ in your MySQL setup.
- The script uses the `SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;` statement to retrieve and filter the records.

## Troubleshooting

If you encounter any issues, verify the following:

- MySQL server is running.
- You have the correct root credentials.
- The script file (`11-best_score.sql`) is in the correct location.

---

---

# Task 12: Update Score of 'Bob' to 10 in `second_table`
==============================================================

## Objective

The objective of this task is to create a script that updates the score of "Bob" to 10 in the table `second_table` from the database `hbtn_0c_0` on the MySQL server. It's important to note that using Bob's id value is not allowed; only the name field should be used.

## Instructions

### Step 1: Create the SQL Script

Create a file named `12-no_cheating.sql` with the following content:

```sql
-- Update the score of Bob to 10 in the table second_table
UPDATE second_table SET score = 10 WHERE name = 'Bob';
```

### Step 2: Execute the Script

Run the script by passing the database name as an argument to the `mysql` command. Use the following command in the terminal:

```bash
cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

You will be prompted to enter the MySQL root password.

### Step 3: Verify Score Update for 'Bob'

After entering the password, the script will execute, and the score of "Bob" in the `second_table` will be updated to 10.

Example Output:

```plaintext
Enter password:
```

## Additional Information

- Ensure that the MySQL server is running before executing the script.
- Make sure to replace `-hlocalhost`, `-uroot`, and `-p` with the appropriate host, username, and password if they differ in your MySQL setup.
- The script uses the `UPDATE second_table SET score = 10 WHERE name = 'Bob';` statement to update the score of "Bob" without using Bob's id value.

## Troubleshooting

If you encounter any issues, verify the following:

- MySQL server is running.
- You have the correct root credentials.
- The script file (`12-no_cheating.sql`) is in the correct location.

---

---

# Task 13: Remove Records with Score <= 5 in `second_table`
==============================================================

## Objective

The objective of this task is to create a script that removes all records with a score less than or equal to 5 in the table `second_table` from the database `hbtn_0c_0` on the MySQL server.

## Instructions

### Step 1: Create the SQL Script

Create a file named `13-change_class.sql` with the following content:

```sql
-- Remove all records with a score <= 5 in the table second_table
DELETE FROM second_table WHERE score <= 5;
```

### Step 2: Execute the Script

Run the script by passing the database name as an argument to the `mysql` command. Use the following command in the terminal:

```bash
cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

You will be prompted to enter the MySQL root password.

### Step 3: Verify Records Removed

After entering the password, the script will execute, and all records with a score less than or equal to 5 in the `second_table` will be removed.

Example Output:

```plaintext
Enter password:
```

## Additional Information

- Ensure that the MySQL server is running before executing the script.
- Make sure to replace `-hlocalhost`, `-uroot`, and `-p` with the appropriate host, username, and password if they differ in your MySQL setup.
- The script uses the `DELETE FROM second_table WHERE score <= 5;` statement to remove records with scores less than or equal to 5.

## Troubleshooting

If you encounter any issues, verify the following:

- MySQL server is running.
- You have the correct root credentials.
- The script file (`13-change_class.sql`) is in the correct location.

---

---

# Task 14: Compute the Score Average of All Records in `second_table`
======================================================================

## Objective

The objective of this task is to create a script that computes the score average of all records in the table `second_table` from the database `hbtn_0c_0` on the MySQL server.

## Instructions

### Step 1: Create the SQL Script

Create a file named `14-average.sql` with the following content:

```sql
-- Compute the score average of all records in the table second_table
SELECT AVG(score) AS average FROM second_table;
```

### Step 2: Execute the Script

Run the script by passing the database name as an argument to the `mysql` command. Use the following command in the terminal:

```bash
cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

You will be prompted to enter the MySQL root password.

### Step 3: View the Score Average

After entering the password, the script will execute, and the average score of all records in the `second_table` will be computed and displayed.

Example Output:

```plaintext
Enter password:
average
9.3333
```

## Additional Information

- Ensure that the MySQL server is running before executing the script.
- Make sure to replace `-hlocalhost`, `-uroot`, and `-p` with the appropriate host, username, and password if they differ in your MySQL setup.
- The script uses the `SELECT AVG(score) AS average FROM second_table;` statement to compute the average of the `score` column.

## Troubleshooting

If you encounter any issues, verify the following:

- MySQL server is running.
- You have the correct root credentials.
- The script file (`14-average.sql`) is in the correct location.
---

---

## Task 15 - List the Number of Records##
===========================================================

Explanation:

    The SELECT score, COUNT(*) AS number statement is used to select the score and the count of records for each score, labeled as "number."
    The FROM second_table clause specifies the table from which to select data.
    The GROUP BY score groups the results by the score column.
    The ORDER BY number DESC, score clause orders the results first by the number of records in descending order and then by the score in ascending order.

You can execute this script by passing the database name as an argument to the mysql command, as shown in your example:

bash

cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

After entering the MySQL root password, the script will execute, and the result will display the score and the number of records for each score, sorted by the number of records in descending order.
---

---
## Task 16 - List Records in Descending Order ##
==========================================================

Explanation:

    The SELECT score, name statement is used to select the score and name columns.
    The FROM second_table clause specifies the table from which to select data.
    The WHERE name IS NOT NULL condition excludes rows where the name value is null.
    The ORDER BY score DESC clause orders the results by the score column in descending order.

You can execute this script by passing the database name as an argument to the mysql command, as shown in your example:

bash

cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

After entering the MySQL root password, the script will execute, and the result will display the score and name for all records in descending order of score, excluding rows without a name value.
---

---
## Task 17 - List in a certain order ##
==============================================================

Explanation:

    The first ALTER DATABASE statement is used to convert the entire hbtn_0c_0 database to UTF8 with the specified collation.
    The second ALTER TABLE statement is used to convert the first_table table to UTF8 with the specified collation.
    The CONVERT TO CHARACTER SET clause within the ALTER TABLE statement is used to specify the character set and collation for the table.

You can execute this script by running the following command:

```bash

cat 100-move_to_utf8.sql | mysql -hlocalhost -uroot -p
```
After entering the MySQL root password, the script will execute, and the specified database, table, and field will be converted to UTF8 with the specified collation.
---

---
## Task 18 - Display temperature by City in an order ##
===============================================================

Explanation:

    SELECT city, AVG(temperature) AS avg_temp: This part of the script selects the city column and calculates the average temperature (AVG(temperature)) for each city. The result of this calculation is given the alias avg_temp.

    FROM temperatures: Specifies the table from which to select the data. In this case, it's assumed that the temperatures are stored in a table named temperatures.

    GROUP BY city: Groups the results by the city column. This is necessary because we want to calculate the average temperature for each city.

    ORDER BY avg_temp DESC;: Orders the results by the calculated average temperature (avg_temp) in descending order (DESC).

The script essentially retrieves data from the temperatures table, calculates the average temperature for each city, and presents the results with the city names and their corresponding average temperatures in descending order. This provides a list of cities ordered by their average temperatures in Fahrenheit.
---

---

##Task 19 - Display top City highest temperatures ##
=================================================================

Explanation:

    SELECT city, AVG(temperature) AS avg_temp: This part of the script selects the city column and calculates the average temperature (AVG(temperature)) for each city. The result of this calculation is given the alias avg_temp.

    FROM temperatures: Specifies the table from which to select the data. In this case, it's assumed that the temperatures are stored in a table named temperatures.

    WHERE MONTH(date) IN (7, 8): Filters the records to include only those with a date in July or August. This ensures that the script considers only temperatures from these two months.

    GROUP BY city: Groups the results by the city column. This is necessary because we want to calculate the average temperature for each city.

    ORDER BY avg_temp DESC: Orders the results by the calculated average temperature (avg_temp) in descending order (DESC).

    LIMIT 3: Limits the output to only the top 3 cities based on the average temperature.

The script essentially retrieves data from the temperatures table, filters it to include only records from July and August, calculates the average temperature for each city, and presents the top 3 cities with the highest average temperatures during these months.
