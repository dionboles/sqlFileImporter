import mysql.connector
cnx = mysql.connector.connect(user='****', password='***',
                              port = 3306
                              host='127.0.0.1',
                              database='populate')
cursor = cnx.cursor()

for line in open("./data.sql"):
    try:
         print(line);
         cursor.execute(line);
    except expression as identifier:
        pass
   
cnx.commit();
