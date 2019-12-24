from flask import Flask, render_template, request, session, jsonify, redirect, url_for


app = Flask(__name__)
app.secret_key = b'123123as!'


@app.route("/")
def hello():
    print("==========> hello ")
    #return "<h1>Hello World!</h1>"
    return render_template('hello.html', title = 'Hello Jinja2!!' , h1 ='Hello jinja2!')


@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method =='GET':
        return render_template('post.html')
    elif request.method =='POST':
        value = request.form['test']
        print(value)
        return render_template('default.html')

@app.route('/in')
def index():
    if 'id' in session:
        return render_template('main.html',id=session['id'])
    return 'no login'    

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method =='GET':
        return render_template('login.html')
    elif request.method =='POST':
        session['id'] = request.form['id']
        print(session['id'])
        return render_template('main.html',id=session['id'])


@app.route('/logout')
def logout():
    #print(session['id'])
    session.pop('id', None)
    return redirect(url_for('index'))

@app.route("/one")
def hellOne():
    print("==========> hello One ")
    return "<h1>Hello One!!</h1>"

@app.route("/member/<user>")
def member(user):
    print("==========> member" + user)
    return "<h3> Hello " + user + "!</h3>"

@app.route("/msg/<int:msgId>")
def getMsg(msgId):
    return "message id : %d" % msgId

@app.route("/first/<int:msgId>")
def getFirst(msgId):
    #print("==========>" + msgId)
    return "<h1>%d</h1>" % (msgId +5)


@app.route("/api/test", methods=['POST'])
def apiTest():
    data = jsonify(data)
    print(data)
    return data



host_addr = "0.0.0.0"
port_num = "8080"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")

#jinja2 사용하기
# request body 에 body -> json 데이터 받기 (딕셔너리, 맵 받기)
# 파일 업로드하기
# 세션 사용해서 로그인, 로그아웃.
#이거 이후에 몽고db연결
