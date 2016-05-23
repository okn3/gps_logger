# coding:utf-8
import sys
sys.path.append('/var/www/gps_logger/server/module')
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
    usemongo.set_gps(float(request.form['lat']), float(request.form['lng']))
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
def show_spot():
    lat,lng = usemongo.get_gps_now()
    print "lat:",lat
    print "lng:",lng
    return render_template('spot.html',lat=lat,lng=lng)

# 複数データを読み取り表示経路の表示
@app.route('/web/show_route')
def show_route():
    gps_list = usemongo.get_gps_all()
    print gps_list
    return render_template('route.html', path = gps_list)

@app.route('/web/test_geo_api')
def test_geo_api():
    return render_template('geo.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False)
