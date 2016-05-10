# coding:utf-8
import sys
sys.path.append('module')
from flask import Flask
from flask import request
from flask import render_template
import usemongo

app = Flask(__name__)
@app.route('/')
def root():
    return "running!"

@app.route('/api/gps/set',methods=['POST'])
def set_gps():
    usemongo.set_gps(int(request.form['lat']), int(request.form['lng']))
    return "set_gps"

@app.route('/api/gps/show_all')
def get_gps():
    res = usemongo.get_gps()
    return str(res)

@app.route('/api/gps/show_recent')
def get_log_recent():
    res = usemongo.get_recent_gps()
    return str(res)

@app.route('/web/show_spot')
def show_spot(name = None):
    lat,lng = usemongo.get_gps_now()
    print "lat:",lat
    print "lng:",lng
    return render_template('map.html',lat=lat,lng=lng)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False)
