from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<name>")
def say(name):
    return "Hi, " + name.capitalize() + "!"

@app.route("/repeat/<int:number>/<name>")
def repeat(name, number):
    return f"{name} " * number

if __name__=="__main__":
    app.run(debug=True)