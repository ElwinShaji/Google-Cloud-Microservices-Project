host='0.0.0.0'
port='1111'
import pprint

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/mean')
def add():
    num = request.args.get('num')
    numb = request.args.get('numb')
    a = int(num)
    b = int(numb)
    c = a + b
    return "The mean of the values are: " + str(c/2)

@app.route('/highest')
def highest():
    num = request.args.get('num')
    numb = request.args.get('numb')
    a = int(num)
    b = int(numb)

    if(a > b):
        return "The higher value is: " + str(a)
    elif(b > a):
        return "The higher value is: " + str(b)
    else:
        return "Both values are equal to each other"



app.run(host,port)
