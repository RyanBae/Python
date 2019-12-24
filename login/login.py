from flask import Flask, session, request, redirect, render_template

app = Flask
app.secret_key = b'123123as!'

@app.route('/') 
def index(): 
    if 'name' in session: 
        return '%s' % escape(session['name']) 
    return 'no login'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['name'] = request.form['name']
        return redirect(render_template('index'))
    return ''

@app.route('/logout')
def logout():
    session.pip('name', None)
    return redirect(render_template('index'))