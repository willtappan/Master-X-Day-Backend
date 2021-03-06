from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL



# initializations
app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = '' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''
mysql = MySQL(app)

# settings
app.secret_key = "mysecretkey"

# routes
@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    data = cur.fetchall()
    cur.close()
    return 0


if __name__ == "__main__":
    app.run(port=5000, debug=True)
    