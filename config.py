JOBS = [
		{
			'id': 'booking',
			'func': 'tasks:booking',
			'args': '',
			'trigger': 'cron',
			'hour': '5',
			'minute': '0, 2',
			'second': '5'
		},
		{
			'id': 'checkin',
			'func': 'tasks:checkin',
			'args': '',
			'trigger': 'cron',
			'hour': '6-21',
			'minute': '45, 50'
		},
		{
			'id': 'clearLog',
			'func': 'tasks:clearLog',
			'args': '',
			'trigger': 'cron',
			'day_of_week':'0',
			'hour': '0',
			'minute': '0'
		},

]
