import sqlite3

def get_db_connection():
    # snippets.db என்ற SQLite கோப்பு தானாகவே உருவாகும்
    conn = sqlite3.connect('snippets.db')
    conn.row_factory = sqlite3.Row  # Dictionary வடிவில் தரவுகளை பெற
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS snippets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        slug TEXT UNIQUE NOT NULL,
        title TEXT,
        content TEXT NOT NULL,
        duration TEXT,
        expires_at DATETIME,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')
    conn.commit()
    conn.close()

# ஆப் தொடங்கும்போது டேபிள் தானாகவே செட் ஆகும்
init_db()