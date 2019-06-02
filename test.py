from flask import Flask, render_template, request, redirect, json, url_for
import requests, json
app = Flask(__name__)
domain = ['kinopoisk', 'tnull', 'fckbrain', 'prukl', 'amfet1']
token = 'c6722212c6722212c6722212dcc618cb33cc672c67222129a81ed77a138d1b63897531b'
answer = []
ret = []
flag = 0
@app.route('/', methods=['GET'])
def index_get():
    return render_template('conuctivit.html',answer=ret, flag=flag)
@app.route('/', methods=['POST'])
def index_post():
    ret = []
    for i in domain:
        url = "https://api.vk.com/method/wall.search?domain={}&count=100&access_token={}&query={}&v=5.74".format(i, token, request.form.get('find'))
        response = requests.get(url)
        answer = json.loads(response.text)
        for post in answer['response']['items']:
            post['key'] = i
        ret += answer['response']['items']
    a = 0
    for i in ret:
        if i["post_type"] == "post":
            a+=1
    if a == 0:
        flag = 0
    else:
        flag = 1
    ret = sorted(ret, key=lambda x:x['likes']['count'], reverse=True)
    return render_template('conuctivit.html',answer=ret, flag=flag)
app.run(debug=True, port=8111)