

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index ():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


@app.route("/print/<string>")
def print_string(string):
    print(string)
    return string

@app.route("/count/<integer>")
def count (integer):
    if  isinstance (integer, int):
        return range(0,integer)
    
@app.route("/math/<num1>/<operation>/<num2")
def math(num1, operation, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1-num2
    elif operation == "*":
        return num1*num2
    elif operation == "%":
        return num1/num2






if __name__ == '__main__':
    app.run(port=5555, debug=True)
