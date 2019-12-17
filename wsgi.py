from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Simple python application by SMC!"

if __name__ == "__main__":
    application.run()
