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
        return conn
    elif db == 'mysql':
        conn = MySQLdb.connect(host=host,port=port,user=user,passwd=password,db=database_name)
        return conn

class Database:
    def __init__(self):
        self._conn = connect()
        self._cursor = self._conn.cursor()
    def set_parking(self,parking_num,value):
        print value,type(value),parking_num,type(parking_num),'\n\n\n'
        self._conn = connect()
        response = self._cursor.execute("""UPDATE parking_status
                                SET parking_status = {0}
                                WHERE parking_number = {1}
                                """.format(value,parking_num))
        
        self._conn.commit()
    def get_parking(self):
       self._conn = connect()
       self._cursor = self._conn.cursor()
       self._cursor.execute("SELECT * FROM parking_status")

       st = self._cursor.fetchall()
       status_dict = {}
       for park in st:
           status_dict[park[0]] = bool(park[1])
       return status_dict
    def pr(self):
        st = self.get_parking()
        print "status:",st 
        
