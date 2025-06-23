from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "Chave-secreta"  

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    session['username'] = username 
    return redirect(url_for('login'))

@app.route('/profile')
def profile():
    username = session.get('username')
    return render_template('login.html', username=username)