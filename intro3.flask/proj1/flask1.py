from flask import Flask

app=Flask(__name__)

@app.route("/home/<ch>")
def home(ch):
    return "hello,"+ch;
