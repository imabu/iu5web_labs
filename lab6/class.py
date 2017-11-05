import psycopg2
import datetime


class Connection:
    def __init__(self, user, password, db, host='localhost'):
        self.user = user
        self.host = host
        self.password = password
        self.db = db
        self._connection = None

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        if not self._connection:
            self._connection = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                dbname=self.db
            )

    def disconnect(self):
        if self._connection:
            self._connection.close()


class Transacts:
    def __init__(self, db_connection, summ, type, comment=None):
        self.db_connection = db_connection.connection
        self.summ = summ
        self.type = type
        self.comment = comment

    def save(self):
        c = self.db_connection.cursor()
        c.execute("SELECT max(id) from trans_transactsmodel")
        d = c.fetchone()[0]
        c.execute("INSERT INTO trans_transactsmodel(user_id, id, type_id, summ, comment, created_dt) "
                  "VALUES (1, %s, %s, %s, %s, %s);",
                  (d+1, self.type, self.summ, self.comment, datetime.datetime.now()))
        self.db_connection.commit()
        c.close()

username = 'postgres'
password = 'postgres'
database = 'bank_trans'
conn = Connection(username, password, database)

with conn:
    t = Transacts(conn, 1000, 1, 'Концерт')
    t.save()