#! /usr/bin/dev python
# -*- coding utf-8 -*-
# @Time: 2018-09-09 22:53
# @Author: Binyou
# @Site: 
# @File: db.py

from sqlobject import *
from sqlobject.sqlbuilder import *

connection_str = "mysql://root:1615160629@localhost:3306/Seats?driver=connector"
connection = connectionForURI(connection_str)
sqlhub.processConnection = connection


class Seat(SQLObject):
    class sqlmeta:
        table = "seats"
        fromDatabase = True


class Room(SQLObject):
    class sqlmeta:
        table = "rooms"
        fromDatabase = True


class Task(SQLObject):
    class sqlmeta:
        table = "tasks"
        fromDatabase = True


class Admin(SQLObject):
    class sqlmeta:
        table = "admin"
        fromDatabase = True


def show_rooms():
    rows = connection.queryAll(str(Room.select(orderBy='floor')))
    return rows
    # return [json.dumps({'id': r[0], 'room_name': r[1], 'campus': r[2], 'floor': r[3], 'seat_num': r[4]})
    #         for r in rows]


def show_seats(room_id):
    rows = connection.queryAll(str(Seat.selectBy(roomID=room_id).orderBy('seat_id')))
    return rows
    # return [json.dumps({'id': r[0], 'seat_id': r[1], 'seat_name': r[2], 'room_id': r[3]})
    #         for r in rows]


def select_all_tasks():
    #print(Task.select(orderBy='tasks.id'))
    rows = connection.queryAll(str(Task.select(orderBy='tasks.id')))
    return rows
    # return [json.dumps({'id': r[0], 'username': r[1], 'password': r[2], 'start': r[3], 'end': r[4], 'seat': r[5], 'remark': r[6], 'creator_id': r[7], 'auto_checkin': r[8]})
    #         for r in rows]


def show_tasks(log_id):
    rows = connection.queryAll(str(Task.select(orderBy='id')))
    res = list()
    for r in rows:
        if log_id == 0 or r[7] == log_id:
            res.append([r[0], r[1], r[2], round(int(str(r[3]))/60),round(int(str(r[4]))/60), Seat.get(int(str(r[5]))).seatName, r[6], Admin.get(int(str(r[7]))).name])
    return res
    # return [json.dumps({'id': r[0], 'seat_id': r[1], 'seat_name': r[2], 'room_id': r[3]})
    #         for r in rows]


def add_task(task):
    #print(task)
    insert_sql = Insert('tasks', values={'username': task[0], 'password': task[1],
                                        'start': task[2], 'end': task[3], 'seat': task[4], 'remark': task[5], 'creator_id': task[6], 'auto_checkin': task[7]})
    query = connection.sqlrepr(insert_sql)
    connection.query(query)


def edit_task(task, id):
    #print(task)
    update_sql = Update('tasks', values={'username': task[0], 'password': task[1],
                                        'start': task[2], 'end': task[3], 'seat': task[4], 'remark': task[5], 'creator_id': task[6], 'auto_checkin': task[7]}, where='id=%d' % (id))
    query = connection.sqlrepr(update_sql)
    connection.query(query)

# print(show_rooms())
# print(show_seats(8))
