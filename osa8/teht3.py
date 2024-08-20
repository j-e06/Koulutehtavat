import mariadb
from geopy import distance
from db_connection import cursor

country_1 = input("Lentokentän 1 ICAO-koodi: ")
country_2 = input("Lentokentän 2 ICAO-koodi: ")

def get_coords(icao,cursor):
    sql = f"SELECT latitude_deg, longitude_deg from airport where ident = '{icao}'"

    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >= 1:
        for line in result:
            return line

country_1_coords = get_coords(country_1,cursor)
country_2_coords = get_coords(country_2,cursor)

print(distance.distance(country_1_coords,country_2_coords).km, "Kilometers apart.")