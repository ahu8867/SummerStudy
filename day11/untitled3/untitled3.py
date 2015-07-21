from flask import Flask, render_template, redirect, request, session
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'serverstudy'
app.config['MYSQL_DATABASE_PASSWORD'] = 'serverstudy!@#'
app.config['MYSQL_DATABASE_DB'] = 'serverstudy'
app.config['MYSQL_DATABASE_HOST'] = 'data.khuhacker.com'
app.config['MYSQL_CHARSET'] = 'utf-8'
app.secret_key ='safdsfasffaasaf'
mysql.init_app(app)
con = mysql.connect()
cur = con.cursor()
cur.execute("SELECT * FROM hu")
data = cur.fetchall()
@app.route('/', methods=['POST', 'GET'])
def basic():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logincheck', methods=['POST'])
def check():
    inputID=request.form['id']
    inputPW=request.form['pw']

    if 'logged_in' in session.keys() and session['logged_in'] == True:
        return render_template('loginFile.html', message="You have already log-in")
    else:
        for user in data:
            ID = user[1]
            PW = user[2]
            if inputID == ID and inputPW == PW:
                session['logged_in'] = True
                return render_template('loginFile.html', message="Login Success")
            else:
                return render_template('loginFile.html', message="Login Failed")

@app.route('/logout')
def logout():
    if session['logged_in']==True:
        session['logged_in']=False
        return render_template('loginFile.html', message="Logout Success")
    else:
        return render_template('loginFile.html', message="Logout Failed")



if __name__ == '__main__':
    app.run()
