import mariadb
conn = mariadb.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='jani',
    password='pirkka',
    autocommit=True
)
cursor = conn.cursor()