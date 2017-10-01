from flask import Flask
from flask import request

application = Flask(__name__)

@application.route("/", methods=['GET', 'POST'])
def hello():
    token=request.args.get('token', 'not found')
    return "Hello World!- {}".format(token)

@application.route("/list/<password>")
def show_list(password):
    return "A list for {}".format(password)

if __name__ == "__main__":
    application.run()
