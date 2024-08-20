import mariadb


conn = mariadb.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='jani',
    password='pirkka',
    autocommit=True
)
sql = f"SELECT * from country;"
cursor = conn.cursor()
cursor.execute(sql)
tulos = cursor.fetchall()
if cursor.rowcount >0 :
        for rivi in tulos:
            print(rivi)