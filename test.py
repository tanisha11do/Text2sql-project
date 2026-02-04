from db import get_connection

conn = get_connection()
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM inventory")
print(cursor.fetchone())
conn.close()
