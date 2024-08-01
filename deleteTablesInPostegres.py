import psycopg2
from psycopg2 import sql

tables=['business','entertainment','health','science','sports','technology',
            'education', 'general', 'domestic', 'environment', 'food', 'lifestyle',
            'politics', 'top', 'tourism', 'world', 'nation', 'other', 'crime']

DATABASE_NAME = '' # your db name
USER_NAME = ''     # your user name
PASSWORD = ''      # your password

def delete_tables(table_names, db_name, user, password, host='localhost', port='5432'):
    """
    Delete multiple tables from a PostgreSQL database.

    Parameters:
    table_names (list): List of table names to delete.
    db_name (str): Name of the database.
    user (str): Database user.
    password (str): Database password.
    host (str): Database host (default: 'localhost').
    port (str): Database port (default: '5432').
    """
    try:
        conn = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        conn.autocommit = True
        
        cur = conn.cursor()
        
        for table in table_names:
            try:
                delete_table_query = sql.SQL("DROP TABLE IF EXISTS {} CASCADE").format(sql.Identifier(table))
                cur.execute(delete_table_query)
                print(f"Table {table} deleted successfully.")
            except Exception as e:
                print(f"Error deleting table {table}: {e}")
        
        cur.close()
        conn.close()
    
    except Exception as e:
        print(f"Error connecting to the database: {e}")

# Example usage
if __name__ == "__main__":
    delete_tables(tables, DATABASE_NAME, USER_NAME, PASSWORD)
