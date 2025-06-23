from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'Chave-secreta'

# Usuário e senha fixos
USUARIO_CORRETO = 'Camilo'
SENHA_CORRETA = 'Huxiaobestship'

# Lista de produtos (frutas)
produtos = ['Maçã', 'Banana', 'Laranja']

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == USUARIO_CORRETO and password == SENHA_CORRETA:
        session['username'] = username
        return redirect(url_for('produto'))
    else:
        return '<h2>Usuário ou senha incorreta. Tente novamente.</h2>'

@app.route('/produto')
def produto():
    if 'username' in session:
        username = session['username']
        return render_template('produto.html', username=username, produtos=produtos)
    else:
        return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)