#!/usr/bin/python3
import MySQLdb
import sys


def list_states(mysql_user, mysql_password, db_name):
    """Connect to MySQL database and list all states ordered by id."""
    try:

        # Connect to the MySQL database
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_user,
            passwd=mysql_password,
            db=db_name,
            charset="utf8"
        )

        # Create a cursor object
        cur = conn.cursor()

        # Execute SQL query
        cur.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all rows
        query_rows = cur.fetchall()

        # Print each row
        for row in query_rows:
            print(row)

    except MySQLdb.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        if cur:
            cur.close()
        if conn:
            conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./0-sele_stes.py <mysql_user> <mysql_pswrd> <db_name>")
   
   else:
        mysql_user = sys.argv[1]
        mysql_password = sys.argv[2]
        db_name = sys.argv[3]
        list_states(mysql_user, mysql_password, db_name)
