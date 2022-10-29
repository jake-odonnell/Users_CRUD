from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

@app.route('/')
def r_home():
    users = User.get_all()
    session.clear()
    return render_template('read.html', users = users)

@app.route('/create')
def r_create():
    if session:
        data = session['data']
    else:
        data = {
            'fn': '',
            'ln': '',
            'email': ''
        }
    return render_template('create.html', data = data)

@app.route('/add', methods = ['POST'])
def p_add():
    data = {
        "fn": request.form['f_name'],
        "ln": request.form['l_name'],
        "email": request.form['email'],
    }
    session['data'] = data
    if User.val_user(data):
        print('Valid')
        User.add_user(data)
        return redirect('/')
    return redirect('/create')

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