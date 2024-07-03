from database.DB_connect import DBConnect
from model.contiguity import Contiguity
from model.country import Country


class DAO():
    @staticmethod
    def get_contiguity_year(year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "select *  from contiguity c where c.`year` <= %s and c.conttype = 1"

        cursor.execute(query, (year,))

        for row in cursor:
            result.append(Contiguity(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all_countries(year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT co.StateAbb, co.CCode, co.StateNme 
                from contiguity c, country co
                where c.`year` <= %s
                and c.state1no = co.CCode 
                group by c.state1no ORDER BY co.StateAbb"""

        cursor.execute(query, (year,))

        for row in cursor:
            result.append(Country(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getCountries():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select * from country c"""

        cursor.execute(query, ())

        for row in cursor:
            result.append(Country(**row))

        cursor.close()
        conn.close()
        return result
if __name__ == "__main__":
    dao = DAO()
    print(dao.get_contiguity_year('1980'))