# mysql_test.py

import mysql.connector
from mysql.connector import errorcode

import dotenv
from dotenv import dotenv_values

# Load secrets from the .env file
secrets = dotenv_values(".env")

# Database config
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}

try:
    # Connect to MySQL
    db = mysql.connector.connect(**config)

    # Output success message
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(
        config["user"], config["host"], config["database"]
    ))

    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
    else:
        print(err)

finally:
    # Close connection
    if 'db' in locals() and db.is_connected():
        db.close()