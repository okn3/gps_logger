# -*- coding:utf-8 -*-

import sys, os
sys.path.append('/var/www/gps_logger/server/')
import logging
# apache$B$N%m%0$K=P$9$?$a$KI,MW(B
logging.basicConfig(stream = sys.stderr)

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from flask_app import app as application
