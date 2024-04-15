#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    """
    Check if the script is beigng run directly
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    """
    Retrieves username, password, and database name from command-line
    """

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    """
    connects to the MySQL server with the provided credentials """

    cursor = db.cursor()
    """
    creates a cursor object to execute SQL queries
    """
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    """
    Executes MySQL query
    select all rows from the table 'states'
    sorted by the 'id' column in ascending order
    """
    states = cursor.fetchall()
    """
    fetch all the results
    """
    for state in states:
        """
        iterate through fetched results
        and prints each row

        Args:
            state: the name of the state to be printed
        """
        print(state)

    cursor.close()
    """ closes the cursor object """
    db.close()
    """ closes the database connection object """
