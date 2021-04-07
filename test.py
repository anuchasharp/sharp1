ffrom flask import Flask
server = Flask(__name__)

@server.route("/")
def hello():
    return "<h1>Hello Anucha Moonladab</h1>"


if __name__ == '__main__':
    #app.run(debug=True)
    server.run(host='0.0.0.0', port=80)
