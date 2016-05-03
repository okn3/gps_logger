# coding:utf-8
import sys
sys.path.append('module')
from flask import Flask
import usemongo

app = Flask(__name__)
@app.route('/')
def root():
    return "running!"

#@app.route('/@@@')
#def @@@():
#    return @@@

@app.route('/set_gps')
def set_gps():
    return usemongo.set_gps(111,222)


if __name__ == '__main__':
    app.run()
