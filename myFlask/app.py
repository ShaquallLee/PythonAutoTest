'''
Descripttion: 
Author: lishaogang
version: 
Date: 2021-11-16 11:02:08
LastEditors: lishaogang
LastEditTime: 2021-11-18 19:13:21
'''
# from typing_extensions import ParamSpecKwargs
from flask import Flask, json, jsonify,request
from requests.models import Request
from static.sql import sql4login

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
    datas = request.values
    print(datas)
    user = datas.get('user')
    pwd = datas.get('password')
    if user=='' or pwd == '':
        return jsonify({'code':"10002", 'message':'parameter error'})
    else:
        res = sql4login(user, pwd)
        print(user, pwd, ': ', res)
        if res:
            return jsonify({'code':"10000", 'message':'login success', 
            'data':f'hello,{user}'})
        else:
            return jsonify({'code':"10004", 'message':'account or password error'})

if __name__ == "__main__":
    # app.run() #以默认方式启动项目
    app.run(host='0.0.0.0', port=80, debug=True)    
    #host设置为0.0.0.0使得这个项目能够以127.0.0.1、localhost或者本机ip来进行访问