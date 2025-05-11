from flask import Flask,render_template,request
import mysql.connector
app = Flask(__name__)

@app.route('/index', methods=['GET','POST'])
def login ():
    msg=""
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        mydb = mysql.connector.connect(
        host ="remotemysql.com",
        user ="Rz8hqn1dk4",
        password = 'nd0WKO3xeO',
        database = 'Rz8hqnldK4'
        )
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM LoginDetails WHERE Name = %s AND Password = %s', (username, password))
        account = mycursor.fetchone()
        if account:
            print('login success')
            name = account[1]
            id = account[0]
            msg = 'Logged in Successfully'
            print('Login Successfull')
            return render_template('index.html', msg=msg, name=name, id=id)
        else:
            msg = "incorrect Credentials. Kindy check"
            return render_template('index.html', msg=msg)
    else:
        return render_template('index.html')
    
    #----------/logout

@app.route('/logout')
def logout():
    name  = ''
    id = ''
    msg = 'Logged out successfully'
    return render_template('index.html', msg=msg, name=name, id=id)