#!/usr/bin/python3
import MySQLdb
import sys


def filter_states(mysql_user, mysql_password, db_name, state_name):
    """Connect to MySQL dbse and list states matching the given name."""
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

        # Use parameterized queries to prevent SQL injection
        query = "SELECT * FROM stes WHERE name LIKE %s ORDER BY id ASC"
        cur.execute(query, (state_name,))

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
    if len(sys.argv) != 5:
        print("Use:./2-my_flter_sts.py <sql_usr><sql_pwd><db_name> <ste_name>")
    else:
        mysql_user = sys.argv[1]
        mysql_password = sys.argv[2]
        db_name = sys.argv[3]
        state_name = sys.argv[4]
        filter_states(mysql_user, mysql_password, db_name, state_name)
