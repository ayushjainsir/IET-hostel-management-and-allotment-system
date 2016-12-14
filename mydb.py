import MySQLdb



class mydb:

    def getsdata(self,v,bname):
        database = MySQLdb.connect (host="localhost", user = "root", passwd = "root", db = "iethostel")
        cursor = database.cursor()
        bname=bname+"%"
        v=v+"%"
        query="""SELECT * FROM block where block LIKE %s  and roomno LIKE %s"""
        arg=[bname,v]
        cursor.execute(query,arg)
        data = cursor.fetchall()
        for row in data:
            print(row[0],row[1],row[2],row[3],row[4])
        cursor.close()
        database.commit()
        database.close()
        return data


