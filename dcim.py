__author__ = 'syedaali'

'''
12/25/2014
This is a small DCIM, or data-center inventory management tool.
It stores 3 items, hostname, admin name, and a field called active.
Hostname is obvious, it's the hostname. Admin name is the name of a person
who is in-charge of the server. Active field should be yes/no, and indicates
if the server is active or not. Active server indicates whether it is being
used or not.

This program reads input from a file called servers.txt. The file should have
one server entry per line of the format:
hostname, admin-name, yes or no

This program also creates a small SQLITE database called servers.db, that
you can manually query for now. In the future querying will be supported
through this program.

Hostname has to be unique, the program needs write permissions in the directory
you are running it from.

How to run this program: python dcim.py
'''
import sqlite3

class Server(object):

    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def admin(self):
        return self.__admin

    @admin.setter
    def admin(self, admin):
        self.__admin = admin

    @property
    def active(self):
        return self.__active

    @active.setter
    def active(self, active):
        self.__active = active


def Sql_Create():
    sql_create = '''
CREATE TABLE IF NOT EXISTS servers(name TEXT PRIMARY KEY, admin TEXT, active TEXT)
'''

    try:
        with sqlite3.connect('servers.db') as con:
            cur = con.cursor()
            cur.execute(sql_create)
            con.commit()
    except Exception, e:
            print e


def Sql_Insert(h):
    sql_insert = '''
INSERT INTO servers (name,admin,active) VALUES('{0}','{1}','{2}')
'''.format(h.name, h.admin, h.active)

    try:
        with sqlite3.connect('servers.db') as con:
            cur = con.cursor()
            cur.execute(sql_insert)
            con.commit()
    except Exception, e:
            print e


def main():
    s_list = []
    Sql_Create()
    with open('servers.txt', 'r') as f:
        for line in f:
            line = line.rstrip('\n')
            line = line.lower()
            s_list = line.split(',')
            h = Server(name=s_list[0], admin=s_list[1], active=s_list[2])
            Sql_Insert(h)

main()
