from database.DB_connect import DBConnect
from model.artist import Artist


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def getNodi(ruolo):
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor(dictionary=True)

        query="""select distinctrow a.*
                from artsmia.artists a ,artsmia.authorship a2 
                where a.artist_id =a2.artist_id 
                and a2.`role` =%s
                order by a.artist_id asc """

        cursor.execute(query,(ruolo,))

        risultato=[]
        for a in cursor:
            risultato.append(Artist(**a))

        cursor.close()
        cnx.close()
        return risultato

    @staticmethod
    def getRuoliDAO():
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor(dictionary=False)

        query="""select distinct a.`role` 
                from artsmia.authorship a 
                order by a.`role` 
                """
        cursor.execute(query)

        risultato=[]
        for a in cursor:
            risultato.append(a[0])

        cursor.close()
        cnx.close()
        return risultato

    @staticmethod
    def getArchi(ruolo):

        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=False)

        query = """select ao1.artist_id,ao2.artist_id, count(distinct ao1.exhibition_id) as mostre
                    from (
                    select distinctrow a.artist_id ,eo.exhibition_id 
                    from artsmia.authorship a , artsmia.exhibition_objects eo 
                    where a.`role` =%s
                    and a.object_id =eo.object_id ) ao1,
                    (select distinctrow a.artist_id ,eo.exhibition_id 
                    from artsmia.authorship a , artsmia.exhibition_objects eo 
                    where a.`role` =%s
                    and a.object_id =eo.object_id ) ao2
                    where ao1.exhibition_id=ao2.exhibition_id
                    and ao1.artist_id< ao2.artist_id
                    group by ao1.artist_id, ao2.artist_id
                    order by ao1.artist_id, ao2.artist_id
                    """

        cursor.execute(query, (ruolo,ruolo,))

        risultato = []
        for a in cursor:
            risultato.append(a)

        cursor.close()
        cnx.close()
        return risultato
