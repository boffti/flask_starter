from flask import Flask, render_template, request
import json
import utils

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/trending-posts')
def trending():
    return render_template('index.html', trendingPosts=utils.getTrendingPosts())

@app.route('/getTrendingPostJson')
def trendingJson():
    return json.dumps(utils.getTrendingPosts())

@app.route('/pushUserData', methods=['POST'])
def pushUserData():
    userName = request.form['userName']
    userEmail = request.form['userEmail']
    #Do something with the data. Push to DB etc.
    utils.updatePostDB(userName, userEmail)
    return '', 204
    