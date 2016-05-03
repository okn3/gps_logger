import serial
from datetime import datetime

if __name__ == "__main__":
    ser = serial.Serial("/dev/tty.usbserial",4800,timeout=10)

    def convert(lat,lng):
        lat = float(lat) / 100
        lng = float(lng) / 100
        return lat,lng
   
    while True:
        line = ser.readline()
        if line.startswith("$GPGGA"):
            data = line.split(",")
            print "raw_data: "+line
            lat,lng = convert(data[2],data[4])
            print lat , "," , lng , "\n"
            # http通信実装
