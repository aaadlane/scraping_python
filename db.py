from datetime import date
import mysql.connector

def savetoDB(URL, values, tag):
    mydb= mysql.connector.connect(
        host="localhost", 
        user="adSql",
        password="kikoolol",
        database="mangas"
    )

    today = date.today()
    mycursor = mydb.cursor()

    sql = "INSERT INTO pricing (url, value, tag, datecreated) values (%s,%s,%s,%s) "
    val = (URL, values, tag, today)
    mycursor.execute(sql, val)

    mydb.commit()
    return str(mycursor) + "nouvelle entrée"
