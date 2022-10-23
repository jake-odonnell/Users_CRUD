from flask import Flask, render_template, redirect, request
from user import User
app = Flask(__name__)

@app.route('/')
def r_home():
    users = User.get_all()
    return render_template('read.html', users = users)

@app.route('/create')
def r_create():
    return render_template('create.html')

@app.route('/update', methods = ['POST'])
def p_update():
    data = {
        "fn": request.form['f_name'],
        "ln": request.form['l_name'],
        "email": request.form['email'],
    }
    User.add_user(data)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug = True)

