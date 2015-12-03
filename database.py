#!/usr/bin env python

import psycopg2,sqlite3,MySQLdb
from ConfigParser import SafeConfigParser

def connect():
    config = SafeConfigParser()
    config.read("database.ini")
    db =  config.get('database','database')
    if db == 'sqlite':
        filename = config.get(db,"filename)")
        return sqlite3.connect(filename)
    database_name = config.get(db,'database_name')
    user = config.get(db,'user')
    host = config.get(db,'host')
    port = int(config.get(db,'port'))
    password = config.get(db,'password')
    print port,type(port)
    if db == 'postgresql':
        
        conn = psycopg2.connect("""dbname=\'{0}\' user=\'{1}\' host=\'{2}\' 
                                password=\'{3}\'""".format(database_name,user,host,password))
        return conn.cursor()
    elif db == 'mysql':
        conn = MySQLdb.connect(host=host,port=port,user=user,passwd=password,db=database_name)
        return conn.cursor()

class Database:
    def __init__(self):
        self._cursor = connect()
    def set_parking(self,parking_num,value):
        self._cursor.execute("""UPDATE parking_status
                                SET status = %(value)
                                WHERE parking_num = %(adr)
                                """ %{"value":value,"adr":address})
        self._cursor.commit()
    def get_parking(self):
       self._cursor.execute("SELECT * FROM parking_status")
       
       st = self._cursor.fetchall()
       status_dict = {}
       for park in st:
           status_dict[park[0]] = bool(park[1])
       return status_dict

