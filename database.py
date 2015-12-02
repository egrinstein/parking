import sqlite3

class Database:
    def __init__(self):
        self._cursor = sqlite3.connect('db.sqlite')
    def set_parking(self,parking_num,value):
        self._cursor.execute("""UPDATE parking_status
                                SET status = %(value)
                                WHERE parking_num = %(adr)
                                """ %{"value":value,"adr":address})
        self._cursor.commit()
    def get_parking(self):
       st =self._cursor.execute("SELECT * FROM parking_status")
       st = st.fetchall()
       status_dict = {}
       for park in st:
           status_dict[park[0]] = bool(park[1])
       return status_dict

