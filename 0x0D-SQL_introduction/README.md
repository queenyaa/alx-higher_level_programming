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

##Task 1: ##
Certainly! Below is an example documentation for Task 1: "Create a database."

---

# Task 1: Create a Database if Missing

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

