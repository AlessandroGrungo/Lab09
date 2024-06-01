from database.DB_connect import DBConnect
from model.airport import Airport
from model.rotta import Rotta

class DAO():
    @staticmethod
    def getAllAirports():
        result=[]
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute('SELECT * FROM airports')
        for row in cursor:
            result.append(Airport(**row))
        cursor.close()
        cnx.close()
        return result
    @staticmethod
    def getAllRotte():
        result = []
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = ("""SELECT F.ORIGIN_AIRPORT_ID AS a1, F.DESTINATION_AIRPORT_ID as a2,
                    SUM(F.DISTANCE) AS totDistanza, COUNT(*) AS nVoli FROM flights F
                    GROUP BY F.ORIGIN_AIRPORT_ID, F.DESTINATION_AIRPORT_ID""")

        cursor.execute(query)
        for row in cursor:
            result.append(Rotta(**row))
        cursor.close()
        cnx.close()
        return result

