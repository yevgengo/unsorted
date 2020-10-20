import mysql.connector
from mysql.connector import (connection)
class ourmysqlconnection:
    def __init__(self):
        self.user=''
        self.password=''
        self.database=''
        self.host=''

    def startconnectionwithcreds(self,ouruser='',ourpassword='',ourhost='',ourdatabase=''):
        self.user=ouruser
        self.password=ourpassword
        self.host=ourhost
        self.database=ourdatabase
#        self.cnx = connection.MySQConnection(user=ouruser,password=ourpassword,host=ourhost,database=ourdatabase)
        self.cnx = mysql.connector.connect(user=ouruser,password=ourpassword,host=ourhost,database=ourdatabase)
        self.cursor=self.cnx.cursor()

    def closeconnection(self):
        self.cursor.close()
        self.cnx.close()


    def samplequery(self):
        samplequery='select 1'
        self.cursor.execute(samplequery)
        myresult=self.cursor.fetchall()
        for item in myresult:
            print (item)

    def getlistoflists(self,targettable,ourcolumnlabels,whereclause,dataseparator):
        ourreturnlist=[]
        ourreturnrow=[]
        rowcounter=0
        query="select "
        for column in ourcolumnlabels:
            query=query+column+","
        query=query.rstrip(",")
        query=query+" from "+self.database+'.'+targettable
        if (whereclause!=""):
            query=query+" where "+whereclause

        try:
            self.cursor.execute(query)
#            self.cnx.commit()
        except:
            pass
            print ("issues with query")
            print (query)

        rowcounter=0
        for ourrow in self.cursor.fetchall():
#            print (ourrow)
            for element in ourrow:
                if (dataseparator==""):
                    ourreturnrow=ourreturnrow+[element]
                else:
                    ourreturnrow=element.split(dataseparator)

            ourreturnlist=ourreturnlist+[ourreturnrow]
            ourreturnrow=[]

        return ourreturnlist



    def insertlistoflists(self,targettable,ourlistoflists,ourcolumnlabels,batchsize=10):
        rowcounter=0
        query="REPLACE INTO "+self.database+'.'+targettable +' ('
        for column in ourcolumnlabels:
            query=query+column+","
        query=query.rstrip(",")
        query=query+')' + ' VALUES ('
        for row in ourlistoflists:
            for field in row:
                query=query+"\""+str(field)+"\","
            query=query.rstrip(',')
            query=query+'),('
            if (rowcounter>=batchsize):
                query=query.rstrip('(')
                query=query.rstrip(',')
                try:
                    self.cursor.execute(query)
                    self.cnx.commit()
                except:
                    pass
                    print (query)
               #     print ("issue in main insert attempt")

                rowcounter=0
                query="REPLACE INTO "+self.database+'.'+targettable +' ('
                for column in ourcolumnlabels:
                    query=query+column+','
                query=query.rstrip(',')
                query=query+')' + ' VALUES (' 
            else:
                rowcounter+=1
        try:
            query=query.rstrip(',(')
            self.cursor.execute(query)
            self.cnx.commit()

        except:
            pass

#            print (query)
        #    print ("issue with remainder query")




            









