import mariadb
from db_connection import cursor

icao_koodi = input("Lentokentän icao koodi: ")



sql = f"SELECT * from airport where ident = '{icao_koodi}';"

cursor.execute(sql)
tulos = cursor.fetchall()
if cursor.rowcount >0 :
    result = tulos[0]
    print(result)
    print(result[3])
    print(result[10])
