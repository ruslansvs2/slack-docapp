from app import app
from .doc import *



#@app.route('/', methods=['POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return "Hello, This is Jot"

@app.route('/doc', methods=['GET', 'POST'])
def doc():
    #if token_based_authentification() is not True:
    #    return abort()
    return(get_doc())

@app.route('/add', methods=['GET', 'POST'])
def add():
    if token_based_authentification() is not True:
        return abort()
    return(put_doc())

@app.route('/help', methods=['GET', 'POST'])
def help():
    if token_based_authentification() is not True:
        return abort()
    return(help_doc())

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if token_based_authentification() is not True:
        return abort()
    return(delete_doc())

