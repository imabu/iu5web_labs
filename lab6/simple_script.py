import psycopg2

hostname = 'localhost'
username = 'postgres'
password = 'postgres'
database = 'bank_trans'


def dbQuery(conn):
    cur = conn.cursor()

    cur.execute("SELECT summ, created_dt FROM trans_transactsmodel")

    for summ, created_dt in cur.fetchall() :
        print(summ, created_dt)


myConnection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
dbQuery(myConnection)
myConnection.close()