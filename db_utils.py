import os
from dotenv import load_dotenv

if os.getenv("IS_DOCKER"):
    load_dotenv(".env.docker")
else:
    load_dotenv(".env.local")

import time
import mysql.connector
from mysql.connector import Error



def get_test_users():
    is_local = os.getenv("IS_LOCAL", "false").lower() == "true"
    if is_local:
        user = "root"
        password = os.getenv("LOCAL_DB_PASSWORD", "")
        host = "127.0.0.1"
    else:
        user = os.getenv("DB_USER", "testuser")
        password = os.getenv("DB_PASSWORD", "testpass")
        host = os.getenv("DB_HOST", "mysql")

    print(f"Connecting to DB at {host} with user={user}")

    for i in range(10):
        try:
            conn = mysql.connector.connect(
                host=host,
                port=os.getenv("DB_PORT", "3306"),
                user=user,
                password=password,
                database=os.getenv("DB_NAME", "testdb"),
            )
            cursor = conn.cursor()
            cursor.execute("SELECT username, password FROM test_users")
            return cursor.fetchall()
        except Error as e:
            print(f"⏳ Waiting for DB... {e}")
            time.sleep(3)
        finally:
            if 'conn' in locals() and conn.is_connected():
                conn.close()
    raise RuntimeError("❌ Could not connect to database after retries.")
