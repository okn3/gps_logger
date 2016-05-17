# -*- coding:utf-8 -*-

import sys, os
sys.path.append('/var/www/gps_logger/server/')
import logging
# apacheのログに出すために必要
logging.basicConfig(stream = sys.stderr)

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from flask_app import app as application
