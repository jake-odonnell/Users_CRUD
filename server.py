from re import U
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

@app.route('/add', methods = ['POST'])
def p_add():
    data = {
        "fn": request.form['f_name'],
        "ln": request.form['l_name'],
        "email": request.form['email'],
    }
    User.add_user(data)
    return redirect('/')

@app.route('/show/<id>')
def r_show_one(id):
    users = User.get_all()
    id = int(id) - 1
    user = users[id]
    return render_template('read_one.html', user = user)

@app.route('/update/<id>')
def r_update(id):
    users = User.get_all()
    id = int(id)-1
    user = users[id]
    print(user.id)
    return render_template('/update.html', user = user)

@app.route('/update_user/<id>', methods = ['POST'])
def p_update(id):
    data = {
        'id': id,
        'fn': request.form['f_name'],
        'ln': request.form['l_name'],
        'email': request.form['email']
    }
    User.update_user(data)
    return r_show_one(id)

@app.route('/delete/<id>')
def p_delete(id):
    data = {
        'id': id
    }
    User.delete_user(data)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)

