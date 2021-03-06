from flask import Flask
from flask.ext.mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'DHGLYjoe521'
mysql.init_app(app)

@app.route("/helloworld")
def hello():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * from helloworld.messages')
    msgs = cur.fetchall()
    return str(msgs)

if __name__ == "__main__":
    app.run()
