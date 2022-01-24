from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return "Welcome"

@app.route('/welcome/<page_name>')

def get_page(page_name):
    return f"Welcome {page_name}"
