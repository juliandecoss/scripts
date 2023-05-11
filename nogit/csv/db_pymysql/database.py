import os
import pymysql

db_params = {}
def decrypt_db_vars(shard):
    db = "KONFIO"
    used_host = "KONFIO"
    host = "main-ro.db.private.konfio.mx"
    user = "julian_decoss"
    password = "4j9o:a9DNWVCPh=m"
    ssl={'ssl':{'ca': '/Users/intern/Downloads/rds-ca-2019-root.pem'}}
    return {"db": db, "password": password, "user": user, "host": host, "ssl":ssl}

def get_db_params(shard):
    if not db_params.get(shard):
        db_params[shard] = decrypt_db_vars(shard)
    return db_params[shard]

def db_connection(shard: str) -> pymysql.connections.Connection:
    # Connect to the database
    connection_params = get_db_params(shard)
    return pymysql.connect(
        **connection_params, charset="utf8mb4", cursorclass=pymysql.cursors.DictCursor
    )


def execute_query(query: str, args: list, shard: str, commit: bool = False) -> pymysql.cursors.Cursor:
    connection = db_connection(shard)
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, args)
            result = cursor
        if commit:
            connection.commit()
    finally:
        connection.close()
    return result

def database(args, shard="KONFIO"):
    sql = """ 
        SELECT id 
        FROM NATURAL_PERSON
        WHERE email = %s;
     """
    cursor = execute_query(sql, args, shard)
    return cursor.fetchone()

