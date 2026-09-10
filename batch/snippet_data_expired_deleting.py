from mysql_config import get_db_connection
from datetime import datetime

db = get_db_connection()
if db:
    try:
        cursor = db.cursor()
        cursor.execute("DELETE FROM snippets WHERE expires_at < now()")
        db.commit()
        deleted_rows = cursor.rowcount
        print(f"Expired snippets deleted successfully: {deleted_rows}")
        log_file = "deleted_snippets_log.txt"
        with open(log_file, "a") as log:
            log.write(f"{datetime.now()}: Deleted {deleted_rows} expired snippets\n")
    except Exception as e:
        print("Error occurred while deleting expired snippets:", e)
    finally:
        cursor.close()
        db.close()
else:
    print("Database connection failed")