from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)

@app.route('/')
def r_home():
    users = User.get_all()
    print(users)
    return render_template('read.html')


if __name__ == '__main__':
    app.run(debug = True)

