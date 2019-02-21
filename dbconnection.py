from mysql.connector import connect

class DBconnection:

    def __init__(self, user='root', password='', database='task_app', host="127.0.0.1"):
        self.cnx = connect(user=user, password=password,
                      host=host, database=database)
        self.cursor = self.cnx.cursor()



    def select(self, table, column="", where=""):
        sql = "SELECT * FROM {}". format(table)
        if where:
            sql += 'WHERE {} = "{}"'.format(column,where)
        self.cursor.execute(sql)
        #self.cnx.commit()
        results = []
        for record in self.cursor:
            results.append(record)
        return results

