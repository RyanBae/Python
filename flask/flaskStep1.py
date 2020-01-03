from flask import Flask, render_template, request, session, jsonify, redirect, url_for
from pymongo import MongoClient
#from werkzeug import secure_filename


app = Flask(__name__)
app.secret_key = b'123123as!'

client = MongoClient('mongodb://localhost:27017/')
db = client.test
collection = db.mongotest

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

#@app.route('/test')
#def test():
#    return render_template('post.html')
#@app.route('/post', methods=['POST'])
#def post():
#    value = request.form['test']
#    return value
#@app.route('/test', method=['GET', 'POST'])
#    def test():
#        if request.method =='GET':
#            return render_template('post.html')
#        elif request.method =='POST':
#            value = request.form['test']
#            return render_template('default.html')

@app.route('/in')
def index():
    if 'id' in session:
        return render_template('main.html',id=session['id'])
    return render_template('nologin.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'id' in session:
        return redirect(url_for('index'))
    else :
        if request.method =='GET':
            return render_template('login.html')
        elif request.method =='POST':
            userid = request.form['id']
            password = request.form['password']
            x = collection.find_one({"id": userid})
            client.close();
            if x == None:
               return render_template('login.html') 
            else:
                if x['password'] == password:
                    session['id'] = x['id']
                    session['name'] = x['name']
                    print(session['id'])
                    return render_template('main.html',id=session['id'])
                else :
                    session.pop('id', None)
                    return render_template('login.html')




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
    data = request.get_json()
    print(data['name'])
    return data

@app.route("/upload")
def upload():
    return render_template('upload.html')

@app.route("/fileUpload", methods=['GET', 'POST'])
def fileUpload():
    if request.method == 'POST':
        file = request.files['file']
        #경로, 파일명
        #file.save("./file/"+secure_filename(file.filename))
        return "파일 업로드 성공"






@app.route('/mongo', methods=['GET'])
def mongoTest():
    results = collection.find()
    client.close();
    return render_template('mongo.html', data=results)


@app.route('/mongoinput', methods=['GET'])
def mongoinput():
    return render_template('insert.html')

@app.route('/mongoinsert', methods=['POST'])
def mongoinseft():
    userid = request.form['id']
    password = request.form['password']
    name = request.form['name']
    print(userid +" / "+password+" / "+name)
    user = {"id": userid, 
            "password":password,
             "name":name}
    print(user)
    collection.insert(user)
    client.close();
    return render_template('login.html')

@app.route('/mypage', methods=['GET'])
def mypage():
    if 'id' in session:
        return render_template('mypage.html', id=session['id'], name=session['name'])
    else:
        return redirect(url_for('login'))

@app.route('/passwordCh', methods=['GET','POST'])
def passwordCh():
    if request.method == 'GET':
        return render_template('passCh.html');
    elif request.method == 'POST':
        print(session['id'])
        x = collection.find_one({"id": session['id']})
        if request.form['pass'] == x['password']:
            newpass = request.form['newpass']
            collection.update({"id":session['id']}, {"$set":{"password":newpass}})
            client.close();
            session.pop('id', None)
            return redirect(url_for('login'))
        else :
            return redirect(url_for('passwordCh'))

@app.route('/delete', methods=['GET'])
def delete():
    userid = session['id']
    session.pop('id', None)
    collection.remove({"id":userid})
    return redirect(url_for('index'))

@app.route('/replace', methods=['GET','POST'])
def replace():
    if request.method == 'GET':
        if 'id' in session :
            userid = session['id']
            name = session['name']
            return render_template('replace.html', userid = userid, name=name)
        else:
            return redirect(url_for('login'))
    elif request.method == 'POST':
        userid = session['id']
        name = session['name']
        address = request.form['address']
        phone = request.form['phone']
        x = collection.find_one({"id":userid})
        collection.replace_one({"id":userid}, 
            {"id":userid, "name":name, "address":address, "phone":phone, "password":x['password']})
        client.close();
        return redirect(url_for('mongoTest'))
        

host_addr = "0.0.0.0"
port_num = "8080"

if __name__ == "__main__":
    app.run(host=host_addr, port=port_num)

#jinja2 사용하기
# request body 에 body -> json 데이터 받기 (딕셔너리, 맵 받기)
# 파일 업로드하기
# 세션 사용해서 로그인, 로그아웃.
#이거 이후에 몽고db연결
#몽고 DB 리플레이스 사용해보기

#find더 해보기 
# 대소 비교, like 검색
# 정규식 집어 넣을수 있음. 
# 어그리레이션(집계) *어려움
