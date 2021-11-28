import requests
import json
import mysql.connector

def covid_danger():
    response_API = requests.get('https://covid19.ddc.moph.go.th/api/Cases/today-cases-by-provinces')

    data = response_API.text
    parse_json = json.loads(data)

    connection = mysql.connector.connect(host='iot.cpe.ku.ac.th',
                                        database='b6210545963',
                                        user='b6210545963',
                                        password='thornthep.c@ku.th')
    for i in range(len(parse_json)-1):
        province = (parse_json[i]['province'])
        new_case = (parse_json[i]['new_case'])
        total_case = (parse_json[i]['total_case'])

        danger = new_case/total_case *100

        try:   
            cursor = connection.cursor()
            mySql_insert_query = """INSERT INTO covid_dangerous_province (province, danger)
                                    VALUES (%s, %s) """

            record = (province, danger)
            cursor.execute(mySql_insert_query, record)
            connection.commit()
            print('Success')

        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table {}".format(error))

    if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")


