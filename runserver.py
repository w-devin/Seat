"""
This script runs the Seats application using a development server.
"""

from os import environ
from Seats import app
from flask_apscheduler import APScheduler
import datetime
import logging

if __name__ == '__main__':


	scheduler = APScheduler()
	app.config.from_object('config')
	scheduler.init_app(app)
	scheduler.start()
	
	HOST = environ.get('SERVER_HOST', 'localhost')
	try:
		PORT = int(environ.get('SERVER_PORT', '5555'))
	except ValueError:
		PORT = 5555

	#logging setting
	LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
	logging.basicConfig(filename='msg.log', level=logging.WARNING, format=LOG_FORMAT)

	#app.run(HOST, PORT)
	app.run(host = '0.0.0.0', port = 80)
