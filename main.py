import secrets
from datetime import datetime, timedelta
from flask import Flask, jsonify, request
from flask_cors import CORS
from mysql_config import get_db_connection  # MySQL இணைப்பைப் பயன்படுத்துகிறது

app = Flask(__name__)
CORS(app)

# Hostinger-ல் உங்கள் Domain பெயர் மாறினால் இதை மட்டும் மாற்றவும்
BASE_FRONTEND_URL = "file:///home/saravanan/saravanan/snipper"
@app.route('/main.py', methods=['POST'])
def get_menu():
    my_val = request.form.get('test')
    title = request.form.get('title')
    durtiontime = request.form.get('durtiontime')
    slug = secrets.token_urlsafe(6)

    current_time = datetime.now()
    expiration_time = current_time + timedelta(hours=int(durtiontime))
    
    print("Current time:", current_time)
    print("Expiration time:", expiration_time)

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # SQLite3-ல் %s -க்கு பதிலாக ? பயன்படுத்தப்பட வேண்டும்
        cursor.execute(
            "INSERT INTO snippets (slug, title, content, duration, expires_at) VALUES (?, ?, ?, ?, ?)", 
            (slug, title, my_val, durtiontime, expiration_time)
        )
        conn.commit()
        conn.close()
        print("Data inserted successfully into SQLite3")
    except Exception as e:
        print("Database connection or query failed:", e)

    # file:/// -க்கு பதிலாக Hostinger Web URL போடப்பட்டுள்ளது
    share_url = f"{BASE_FRONTEND_URL}/outpage.html?data={slug}"
    return f"Snippeted successfully! Share this URL: <a href='{share_url}' target='_blank'>{share_url}</a>"

@app.route('/get_snippet')
def get_snippet():
    slug = request.args.get('slug')
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # SQLite3-ல் %s -க்கு பதிலாக ? பயன்படுத்தப்பட்டுள்ளது
        cursor.execute("SELECT * FROM snippets WHERE slug = ?", (slug,))
        result = cursor.fetchone()
        conn.close()
        
        if result:
            return jsonify({
                "title": result['title'],
                "content": result['content']
            })
    except Exception as e:
        print("Fetch Error:", e)

    return "Snippet not found", 404

if __name__ == '__main__':
    app.run(port=5000)