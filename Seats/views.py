"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, g, session, redirect
from Seats import app
from .db import show_seats, show_rooms, add_task, show_tasks, edit_task, Room, Admin, Task


@app.route('/')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )


@app.route('/add')
def add():
    user_id = session.get('user_id')

    #print(user_id)


    if user_id is None:
        return render_template('login.html')

    """Renders the contact page."""
    return render_template(
        'add.html',
        rooms=show_rooms(),
    )


@app.route('/room/<int:id>')
def room(id):
    r = Room.get(id)
    room_name = r.name
    room_id = r.id
    return render_template(
        'room.html',
        name=room_name,
        seats=show_seats(room_id),
    )


@app.route('/seat/new', methods=['GET'])
def seat():
    id = request.args.get('seat_id')
    if id:
        return render_template('seat.html', id=id)


@app.route('/task', methods=['POST', 'GET'])
def task():
    user_id = session.get('user_id')
    if user_id is None:
        return render_template('login.html')

    """Renders the about page."""
    if request.method == 'POST':
        uname = request.form['username']
        passwd = request.form['password']
        s = int(request.form['start']) * 60
        e = int(request.form['end']) * 60
        seat = request.form['seat']
        remark = request.form['remark'].strip()
        auto = request.form['autocheck']
        add_task([uname, passwd, s, e, seat, remark, user_id, auto])
        return render_template('task.html', tasks=show_tasks(user_id))
    return render_template('task.html', tasks=show_tasks(user_id))


@app.route('/task/edit/<int:id>', methods=['POST', 'GET'])
def task_edit(id):
    user_id = session.get('user_id')
    if user_id is None:
        return render_template('login.html')
    if request.method == 'GET':
        return render_template('seat_edit.html', task=Task.get(id))
    elif request.method == 'POST':
        uname = request.form['username']
        passwd = request.form['password']
        s = int(request.form['start'])
        e = int(request.form['end'])
        seat = request.form['seat']
        remark = request.form['remark']
        auto = request.form['autocheck']
        edit_task([uname, passwd, s, e, seat, remark, user_id, auto], id)
        return render_template('task.html', tasks=show_tasks(user_id))
    else:
        return render_template('task.html', tasks=show_tasks(user_id))


@app.route('/task/delete/<int:id>', methods=['GET'])
def task_delete(id):
    user_id = session.get('user_id')
    if user_id is None:
        return render_template('login.html')
    if request.method == 'GET':
        if Task.get(id):
            Task.delete(id)
        return render_template('task.html', tasks=show_tasks(user_id))
    return render_template('task.html', tasks=show_tasks(user_id))


@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        g.user = Admin.selectBy(password=password, name=username)[0]
        session.clear()
        session['user_id'] = g.user.id
        return redirect('/')

    return render_template('login.html')
