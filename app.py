from flask import Flask

application = Flask(__name__)

from views import *

if  __name__ == '__main__':
    application.run(host='127.0.0.1', debug=True)