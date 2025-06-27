
import mysql.connector

class DBUtil:

    @staticmethod
    def get_db_conn():
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="VINO",  
                database="OrderManagement"
            )
            print("MySQL database connection established.")
            return conn
        except mysql.connector.Error as e:
            print("Database connection failed:", e)
            return None
