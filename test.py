import sqlite3
import bcrypt
def get_password_hash(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


# Connect to the SQLite database
conn = sqlite3.connect("forum.db")
cursor = conn.cursor()
pss = get_password_hash("20050624")
# cursor.execute('''delete from users where username = ?''', ("admin",))
# Delete rows where condition is met
cursor.execute("INSERT INTO users (username, hashed_password, email,is_admin, is_active) VALUES (?, ?, ?,?,?)",
               ("admin", pss,"giorgi@gmail.com",1,1))

# Commit the changes and close the connection
conn.commit()
conn.close()
