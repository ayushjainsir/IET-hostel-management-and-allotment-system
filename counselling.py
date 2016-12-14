import MySQLdb


class counselling:


    def getsdata(self,limit):
        database = MySQLdb.connect (host="localhost", user = "root", passwd = "root", db = "iethostel")
        cursor = database.cursor()
        query="""SELECT * FROM counselling ORDER BY percentage DESC"""
        cursor.execute(query)
        limit = map(int, limit)
        data = cursor.fetchall()
        listoflist=[[],[],[],[],[]]
        for row in data:
            choice=4
            print ord(str(row[choice])[0])-65 + limit[0]
            while (choice<8 and limit[ord(str(row[choice])[0])-65]==0):
                choice += 1
            if(choice<8):
                print row[2]+" is alloted block "+row[choice]
                limit[ord(str(row[choice])[0])-65] -=1
                lis=[row[1],row[2],row[8]]
                listoflist[ord(str(row[choice])[0])-65].append(lis)
            else:
                print row[2] +" is not alloted anywhere"
            print(row[0],row[1],row[2],row[3],row[4],row[5], row[6],row[7],row[8])
        print listoflist
        cursor.close()
        database.commit()
        database.close()
        return listoflist
counselling().getsdata([1,1,1,1,1])

