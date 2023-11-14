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

