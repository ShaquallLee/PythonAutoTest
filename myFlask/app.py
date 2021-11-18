'''
Descripttion: 
Author: lishaogang
version: 
Date: 2021-11-16 11:02:08
LastEditors: lishaogang
LastEditTime: 2021-11-16 14:15:02
'''
from flask import Flask, jsonify,request

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"code":100, "message":"success", "data":"hello world"})

@app.route('/hello/<string:name>/<int:n>', methods=['GET'])
def hello_name(name,n):
    res = ''
    for i in range(n):
        res += f"hello,{name}"+"<br/>"
    return res


@app.route('/hello/get', methods=['GET'])
def hello_get():
    name = request.args.get('name')
    if name:
        return f"hello,{name}"
    else:
        return "NONE"

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('user')
    psd = request.form.get('password')
    return f"hello, {user}, your password is {psd}."

if __name__ == "__main__":
    # app.run() #以默认方式启动项目
    app.run(host='0.0.0.0', port=80, debug=True)    
    #host设置为0.0.0.0使得这个项目能够以127.0.0.1、localhost或者本机ip来进行访问