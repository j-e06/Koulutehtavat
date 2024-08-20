import mariadb

from db_connection import cursor

area_code = input("Areakoodi: ")
#area_code = "FI"
sql = f"SELECT name, type FROM airport WHERE  iso_country = '{area_code}' order by type"
cursor.execute(sql)
tulos = cursor.fetchall()
counts = {}
if cursor.rowcount >0 :
    for line in tulos:
        if line[1] not in counts:
            counts[line[1]] = 1
        else:
            counts[line[1]] += 1

print(counts)