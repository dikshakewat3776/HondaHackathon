import pymysql

DATABASE_CONFIGS = {
    'DB_NAME': 'honda',
    'DB_USER': 'root',
    'DB_PASSWORD': 'root',
    'DB_HOST': 'localhost',
    'DB_PORT': '3306',
}


def make_mysql_connection():
    try:
        server = DATABASE_CONFIGS['DB_HOST']
        username = DATABASE_CONFIGS['DB_USER']
        password = DATABASE_CONFIGS['DB_PASSWORD']
        database_name = DATABASE_CONFIGS['DB_NAME']
        return pymysql.connect(server, username, password, database_name)
    except Exception as e:
        print("Could not establish a connection with the remote server: " + str(e))


def execute_sql_query(query):
    cursor = None
    connection = None
    try:
        try:
            connection = make_mysql_connection()
        except Exception as e:
            connection = None
            print("Could not establish a connection with the remote server: " + str(e))
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query)
        if cursor.rowcount == 1:
            row = cursor.fetchone()
        else:
            row = cursor.fetchall()
        connection.commit()
        return {"Success": True, "Row": row}
    except Exception as e:
        raise Exception("Procedure Call failed with query: " + query + " and Error: " + str(e))
    finally:
        cursor.close()
        connection.close()


# Driver function
if __name__ == "__main__":
    conn = execute_sql_query(query="SELECT count(*) FROM honda.mytable")
    print(conn)