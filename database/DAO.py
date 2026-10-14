
from database.DB_connect import DBConnect
from model.regista import Regista


class DAO:
    @staticmethod
    def getAllMovies():
        conn = DBConnect.get_connection()
        results = []

        cursor = conn.cursor(dictionary=True)
        query = """
                select * from movie m """

        cursor.execute(query)

        for row in cursor:
            results.append(row)

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllDirector():
        conn = DBConnect.get_connection()
        results = []

        cursor = conn.cursor(dictionary=True)
        query = """
                    select n.*
                    from director_mapping dm , names n 
                    where dm.name_id = n.id  """

        cursor.execute(query)

        for row in cursor:
            results.append(
                Regista(**row)
            )

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getDirectorNodes(dataInizio, dataFine):
        conn = DBConnect.get_connection()
        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct (dm.name_id)
                    from director_mapping dm , movie m 
                    where dm.movie_id = m.id 
                    and m.date_published >= %s
                    and m.date_published <= %s
                      """

        cursor.execute(query, (dataInizio, dataFine))

        for row in cursor:
            results.append(
                row["name_id"]
            )

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getDirectorGenre(dataInizio, dataFine):
        conn = DBConnect.get_connection()
        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select dm.name_id, g.genre 
                    from director_mapping dm , movie m, genre g 
                    where dm.movie_id = m.id and g.movie_id =m.id 
                    and m.date_published >= %s
                    and m.date_published <= %s
                         """

        cursor.execute(query, (dataInizio, dataFine))

        for row in cursor:
            results.append(
                (row["name_id"], row["genre"])
            )

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getAllInfoFilm(direttore, dataInizio, dataFine):
        conn = DBConnect.get_connection()
        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct m.*
                    from director_mapping dm , movie m 
                    where dm.movie_id = m.id 
                    and m.date_published >= %s
                    and m.date_published <= %s
                    and dm.name_id =%s
                            """

        cursor.execute(query, (dataInizio, dataFine, direttore.id))

        for row in cursor:
            results.append(
                {
                    "id" : row["id"],
                    "title": row["title"],
                    "year": row["year"],
                    "date_published": row["date_published"],
                    "duration": row["duration"],
                    "country": row["country"],
                    "worlwide_gross_income": row["worlwide_gross_income"],
                    "languages": row["languages"],
                    "production_company": row["production_company"]
                }
            )


        cursor.close()
        conn.close()
        direttore.lista_film = results








