import cx_Oracle
import configparser

def read_db_config():
    config = configparser.ConfigParser()
    config.read('db_config.ini')
    if 'oracle' not in config:
        print("The 'oracle' section is missing in the configuration file.")
        return None
    db_config = {}
    try:
        db_config['username'] = config['oracle']['username']
        db_config['password'] = config['oracle']['password']
        db_config['dsn'] = config['oracle']['dsn']
    except KeyError as e:
        print(f"Missing key in configuration file: {e}")
        return None
    return db_config

def execute_sql(db_config, sql):
    try:
        connection = cx_Oracle.connect(user=db_config['username'], password=db_config['password'], dsn=db_config['dsn'])
        cursor = connection.cursor()
        cursor.execute(sql)
        
        if sql.strip().lower().startswith("select"):
            result=[]
            result = cursor.fetchall()
            if result:
                for row in result:
                    print(row)
            else:
                print("No results found.")
        else:
            connection.commit()
            print("SQL statement executed successfully.")
        
        cursor.close()
        connection.close()
        return result
    except cx_Oracle.DatabaseError as e:
        print(f"Error executing SQL statement: {e}")

if __name__ == "__main__":
    db_config = read_db_config()
    if db_config:
        # Example usage:
        execute_sql(db_config, "SELECT * FROM studentmaster")  # Select query
        execute_sql(db_config, "INSERT INTO studentmaster (id, name) VALUES (1, 'John Doe')")  # Insert query
        execute_sql(db_config, "UPDATE studentmaster SET name='Jane Doe' WHERE id=1")  # Update query
        execute_sql(db_config, "DELETE FROM studentmaster WHERE id=1")  # Delete query
    else:
        print("Failed to read database configuration.")
