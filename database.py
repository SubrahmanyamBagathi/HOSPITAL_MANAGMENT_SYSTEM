
import mysql.connector # type: ignore

class DatabaseManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'subrahmanyam@123',
            database = 'hospital_db'
        )
        
        self.cursor = self.connection.cursor()
        
    def execute(self,query,values=None):
        if values:
            self.cursor.execute(query,values)
        else:
            self.cursor.execute(query)
    def commit(self):
        self.connection.commit()
        
    def fetch_all(self):
        return self.cursor.fetchall()
    
    def fetch_one(self):
        return self.cursor.fetchone()
    
    def close(self):
        self.cursor.close()
        self.connection.close()
        
        
