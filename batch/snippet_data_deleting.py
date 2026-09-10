# from mysql_config import get_db_connection
# from datetime import datetime

# db = get_db_connection()
# if db:
#     cursor = db.cursor()
#     currect_time = datetime.now()
#     current_data = currect_time.strftime("%Y-%m-%d")
#     print("Current date:", current_data)
#     cursor.execute("select * FROM snippets where expires_at like %s", (f"{current_data}%",))
#     result = cursor.fetchall()
#     cursor.close()
#     print("result", result)
#     for row in result:
#         print("Deleting expired snippet with slug:", row[1])  # Assuming the slug is in the first column
#         expires = row[9]
#         expires_time = expires.strftime("%H:%M:%S")
#         now_time = currect_time.strftime("%H:%M:%S") 
#         if(expires_time[0:5] < now_time[0:5]):
#             if db:
#                 cursor = db.cursor()
#                 cursor.execute("DELETE FROM snippets WHERE slug = %s", (row[1],))
#                 db.commit()
#                 cursor.close()
#                 db.close()
#             else:
#                print("Database connection failed")
#         else:
#             print("Snippet with slug", row[0], "has not expired yet. Expires at:", expires_time)
        
#     print("Expired snippets deleted successfully")
# else:
#     print("Database connection failed")