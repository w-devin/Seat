import datetime
import requests
import json
import time
import logging
from Seats import app
from Seats.db import select_all_tasks

def Token(username, password):
	url = "http://seat.ujn.edu.cn/rest/auth?username=%s&password=%s" % (username, password)
	msg_login = requests.get(url).json()
	if msg_login.get('status') == 'success':
		return msg_login.get('data').get('token')
	else:
		logging.warning('username: %s, paswd = %s, %s' % (username, password, msg_login))

	return None


def booking():
	tasks = select_all_tasks()
	
	for x in tasks:
		token = Token(x[1], x[2])
				
		if token:
			freeBook_url = "http://seat.ujn.edu.cn/rest/v2/freeBook"
			date = time.strftime('%Y-%m-%d', time.localtime(time.time() + 24 * 60 * 60))
			datas = {'token': token, 'startTime': x[3], 'endTime': x[4], 'seat': x[5], 'date': date}
			msg_book = requests.post(freeBook_url, data = datas).json()

			if msg_book.get('status') == 'success':
				logging.info('%s, %s' % (x[1], msg_book))
			else:
				logging.warning('%s, %s, %s' % (x[1], msg_book, datas))


def checkin():
	tasks = select_all_tasks()

	for x in tasks:
		if x[8] == 1:
			token = Token(x[1], x[2])
			if token:
				header = {'X-Forwarded-For': '10.167.159.118'}
				checkin_url = "http://seat.ujn.edu.cn/rest/v2/checkIn?token=%s" % (token)
				msg_checkin = requests.get(checkin_url, headers = header).json()

				if msg_checkin.get('status') == 'success':
					logging.info('%s, %s' % (x[1], msg_checkin))
				else:
					logging.warning('%s, %s' % (x[1], msg_checkin))
		

def clearLog():
	logFile = open('msg.log', 'w+')
	logFile.truncate()
	logFile.close()
