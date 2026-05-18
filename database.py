""" This file handles the database connection and queries"""

import os
import sqlite3

# DB_Config - for SQLite, just the db file

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_FILE = os.path.join(BASE_DIR, 'app.db')

def get_db_connection():
    """Connect to the SQLite database and return connection"""
    try:
        connection = sqlite3.connect(DB_FILE)
        connection.row_factory = sqlite3.Row  # to get dict-like rows
        return connection
    except sqlite3.DatabaseError as e:
        print(f"Database connection failed: {e}")
        return None


def query_db(query, params=()):
    """Execute a database query with parameters."""
    # open the connection
    connection = get_db_connection()

    # Store the params as a dictionary instead of plain text
    cursor = connection.cursor()

    # execute query with params - prevents SQL injection
    cursor.execute(query, params)

    # fetch results as dictionaries
    results = cursor.fetchall()

    # close cursor 
    cursor.close()
    connection.close()

    # results
    return results
