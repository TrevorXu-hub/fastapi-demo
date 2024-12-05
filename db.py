# db.py
import os
import mysql.connector
from mysql.connector import Error

# Set up connection parameters
DBHOST = "ds2022.cqee4iwdcaph.us-east-1.rds.amazonaws.com"
DBUSER = "admin"
DBPASS = os.getenv('DBPASS')  # Password from environment variable
DB = "pxg6af"  # Replace with your actual database name

def get_db_connection():
    try:
        db = mysql.connector.connect(
            user=DBUSER,
            host=DBHOST,
            password=DBPASS,
            database=DB
        )
        return db
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

