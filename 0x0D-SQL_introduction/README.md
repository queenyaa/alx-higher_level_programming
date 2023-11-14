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

