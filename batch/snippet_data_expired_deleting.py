from mysql_config import get_db_connection  # உங்கள் SQLite இணைப்பைக் கொண்ட ஃபைல்
from datetime import datetime

db = get_db_connection()
if db:
    try:
        cursor = db.cursor()
        
        # SQLite-ல் தற்போதைய நேரத்தை சரிபார்க்க datetime.now() பயன்படுத்துகிறோம்
        current_time = datetime.now()
        cursor.execute("DELETE FROM snippets WHERE expires_at < ?", (current_time,))
        
        db.commit()
        deleted_rows = cursor.rowcount
        print(f"Expired snippets deleted successfully: {deleted_rows}")
        
        # Log ஃபைலில் பதிவு செய்ய
        log_file = "deleted_snippets_log.txt"
        with open(log_file, "a") as log:
            log.write(f"{datetime.now()}: Deleted {deleted_rows} expired snippets\n")
            
    except Exception as e:
        print("Error occurred while deleting expired snippets:", e)
    finally:
        db.close() # SQLite-ல் db connection க்ளோஸ் செய்தால் போதுமானது
else:
    print("Database connection failed")