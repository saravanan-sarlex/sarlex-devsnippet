import secrets

from flask import Flask, jsonify, request
from flask_cors import CORS
from mysql_config import get_db_connection
from secrets import token_urlsafe
from datetime import datetime, timedelta
app =Flask(__name__)
CORS(app)

@app.route('/main.py', methods=['POST'])
def get_menu():

    my_val = request.form.get('test')
    title = request.form.get('title')
    durtiontime = request.form.get('durtiontime')
    slug = secrets.token_urlsafe(6)

    db = get_db_connection()
    current_time = datetime.now()
    expiration_time = current_time + timedelta(hours=int(durtiontime))
    print("Current time:", current_time)
    print("Expiration time:", expiration_time)
    print("Database connection:", db)

    if db:

        print("Database connection successful")
        cursor = db.cursor(dictionary=True)

        cursor.execute("INSERT INTO snippets (slug,title,content,duration,expires_at) VALUES(%s,%s,%s,%s,%s)", (slug, title, my_val, durtiontime, expiration_time))
        db.commit()
        cursor.close()
        db.close()
        print("Data inserted successfully")
    else:
        print("Database connection failed")

    # cursor =db.cursor(dictionary=True)
    # cursor.execute("SELECT * FROM snippets WHERE slug = %s", (slug,))
    # result = cursor.fetchone()
    # cursor.close()
    # db.close()

    print("value",my_val)

    print("title",title)
    print("durtiontime",durtiontime)
    
    share_url = f"file:///home/saravanan/saravanan/snipper/outpage.html?data={slug}"
    return f"Snippeted successfully! Share this URL: <a href='{share_url}' target='_blank'>{share_url}</a>"

@app.route('/get_snippet')
def get_snippet():
    slug = request.args.get('slug')
    db = get_db_connection()
    if db:
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM snippets WHERE slug = %s", (slug,))
        result = cursor.fetchone()
        cursor.close()
        db.close()
        print("result", result)
       
        if result:
            return jsonify({
                "title": result['title'],
                "content": result['content']
            })
            
    return "Snippet not found", 404

if __name__ == '__main__':
    app.run(port=5000)

