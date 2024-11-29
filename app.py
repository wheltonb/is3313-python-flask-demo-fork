from flask import Flask

import mymath
from mymath import *

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return f'Done.

if __name__ == '__main__':
  app.run()
