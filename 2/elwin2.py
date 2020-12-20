host='0.0.0.0'
port='2222'

from flask import Flask
import requests
import pprint

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    return '''  <h1> Hi There! :  <h1> '''

val = input("Enter First Number: ")
val2 = input("Enter Second Number: ")


@app.route('/mean')
def add():
    url_mean = "http://localhost:1111/mean?num={}&numb={}".format(val,val2)
    mean = requests.get(url_mean)
    return mean.text

@app.route('/highest')
def highest():
    url_mean = "http://localhost:1111/highest?num={}&numb={}".format(val,val2)
    highest = requests.get(url_mean)
    return highest.text


app.run(host,port)
