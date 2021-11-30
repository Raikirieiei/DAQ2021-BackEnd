import csv
import mysql.connector
from collections import Counter

connection = mysql.connector.connect(host='iot.cpe.ku.ac.th',
                                        database='b6210545963',
                                        user='b6210545963',
                                        password='thornthep.c@ku.th')

with open('Covid-191.csv', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    VaccineList = []
    for row in csv_reader:
        if line_count > 0:
            VaccineList.append(row[3])
           
   
        line_count +=1  

    VaccineCount = Counter(VaccineList)
    
    for VacName,VacCount in VaccineCount.items():

            try:   
                cursor = connection.cursor()
                mySql_insert_query = """INSERT INTO covid_vaccine_count (vaccine_name, vaccine_count)
                                        VALUES (%s, %s) """

                record = (VacName, VacCount)
                cursor.execute(mySql_insert_query, record)
                connection.commit()
                print('Success')

            except mysql.connector.Error as error:
                print("Failed to insert into MySQL table {}".format(error))

        

if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")