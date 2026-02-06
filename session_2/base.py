import sqlite3
# you will need to pip install pandas matplotlib
import pandas as pd
import matplotlib as mpl

def get_connection(db_path="orders.db"):
    """
    Establish a connection to the SQLite database.
    Returns a connection object.
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def top_five_spenders(conn):
    query = '''
            SELECT c.customer_id, first_name, last_name, total_amount
            FROM customers c
            LEFT JOIN orders o
            ON c.customer_id = o.customer_id
            ORDER BY total_amount DESC
            LIMIT 5;
            '''
    cursor = conn.execute(query)
    results = cursor.fetchall()

    return results

def orders_per_category(conn):
    query = '''
            SELECT category, COUNT(*) AS amount
            FROM products p
            LEFT JOIN order_items oi
            ON p.product_id = oi.product_id
            GROUP BY category
            ORDER BY amount;
            '''
    cursor = conn.execute(query)
    results = cursor.fetchall()

    return results

def top_ten_products():
    query = '''
            SELECT p.product_id, p.name, 
            '''

def main():

    db = get_connection()

    db.close()


if __name__=="__main__":
    main()
