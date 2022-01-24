from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route('/add')
def add_val():
    """Add a and b."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    print(request.args)
    return str(add(a,b))

@app.route('/sub')
def sub_val():
    """Substract b from a."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return  str(sub(a,b))

@app.route('/mult')
def mult_val():
    """Multiply a and b."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return  str(mult(a,b))

@app.route('/div')
def div_val():
    """Divide a by b."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return  str(div(a,b))

