import mysql.connector
from time import sleep
cnx = mysql.connector.connect(user='****', password='***',
                              port = ****,
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
