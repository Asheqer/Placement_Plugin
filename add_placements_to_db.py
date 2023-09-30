from mysql.connector import connect, Error
from getpass import getpass
from plugin_queries import insert_placement_records_query,check_duplicates_query

class MySQLconnector:
    def __init__(self, host, username, password, database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        if not self.connection:
            self.connection = connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.database
            )
    
    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def execute_query(self, sql, params=None):
        self.connect()
        try:
            with self.connection.cursor(buffered=True) as cursor:
                if params:
                    cursor.execute(sql, params)
                    self.connection.commit()
                else:
                    cursor.execute(sql)
                result = cursor.fetchall()
                return result
        except Exception as e:
            print(f"Error executing query: {e}")
        finally:
            self.close()

db_conn = MySQLconnector('localhost', 'root', 'Sparke1128345!', 'placements_db')



