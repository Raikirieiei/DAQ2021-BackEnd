import fetch_covid_all
import fetch_covid_per_day
import requests
import mysql.connector

try:   

    connection = mysql.connector.connect(host='iot.cpe.ku.ac.th',
                                database='b6210545963',
                                user='b6210545963',
                                password='thornthep.c@ku.th')
    cursor = connection.cursor()
    mySql_insert_query1 = """ DELETE FROM covid_per_day """
    mySql_insert_query2 = """ DELETE FROM covid_all """

    cursor.execute(mySql_insert_query1)
    cursor.execute(mySql_insert_query2)
    connection.commit()
    print('Success')

except mysql.connector.Error as error:
    print("Failed to insert into MySQL table {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

fetch_covid_all.covid_all_day()
fetch_covid_per_day.covid_per_day()
