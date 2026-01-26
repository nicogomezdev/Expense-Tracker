import sqlite3

DB_NAME="expenses.db"
def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn=get_connection()
    cursor=conn.cursor()

    cursor.execute(""" 
                   CREATE TABLE IF NOT EXISTS expenses(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   type TEXT NOT NULL,
                   amount REAL NOT NULL,
                   category TEXT NOT NULL,
                   date TEXT NOT NULL,
                   description TEXT
                   )
                   """)
    
    conn.commit()
    conn.close()

def save_expense(data:dict)->int:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO expenses (type, amount, category, date, description)
        VALUES(?,?,?,?,?)
    """,(
        data["type"],
        data["amount"],
        data["category"],
        data["date"],
        data["description"]
    ))
    conn.commit()
    expense_id=cursor.lastrowid
    conn.close()
    return expense_id