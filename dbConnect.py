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

def executeSQL(query):
    try:
        db_config = read_db_config()
        if db_config:
            pass
        else:
            print("Failed to read database configuration.")
        connection = cx_Oracle.connect(user=db_config['username'], password=db_config['password'], dsn=db_config['dsn'])
        cursor = connection.cursor()
        cursor.execute(query)
        tables = cursor.fetchall()
        if tables:
            return tables
        else:
            print("No tables found in the database.")
        cursor.close()
        connection.close()
    except cx_Oracle.DatabaseError as e:
        print(f"Error connecting to Oracle Database: {e}")
