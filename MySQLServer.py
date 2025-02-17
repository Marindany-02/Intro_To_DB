import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish connection to MySQL Server (Change credentials if needed)
        connection = mysql.connector.connect(
            host='localhost',  # Update if using a remote server
            user='root',       # Update with your MySQL username
            password='yourpassword'  # Update with your MySQL password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
