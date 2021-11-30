import requests
import json
import mysql.connector


def covid_all_day():
    response_API = requests.get('https://covid19.ddc.moph.go.th/api/Cases/timeline-cases-all')

    data = response_API.text
    data_json = json.dumps(data)
    parse_json = json.loads(data)

    connection = mysql.connector.connect(host='iot.cpe.ku.ac.th',
                                                database='b6210545963',
                                                user='b6210545963',
                                                password='thornthep.c@ku.th')

    for i in range(len(parse_json)):
        txn_date = (parse_json[i]['txn_date'])
        new_case = (parse_json[i]['new_case'])
        total_case = (parse_json[i]['total_case'])
        new_death = (parse_json[i]['new_death'])
        total_death = (parse_json[i]['total_death'])
        new_recovered = (parse_json[i]['new_recovered'])
        total_recovered = (parse_json[i]['total_recovered'])

        try:
           
            cursor = connection.cursor()
            mySql_insert_query = """INSERT INTO covid_all (date, new_case, total_case, new_death, total_death, new_recovered, total_recovered)
                                    VALUES (%s, %s, %s, %s, %s, %s, %s) """

            record = (txn_date, new_case, total_case, new_death, total_death, new_recovered, total_recovered)
            cursor.execute(mySql_insert_query, record)
            connection.commit()
            print('Success')

        except mysql.connector.Error as error:
            print("Failed to insert into MySQL table {}".format(error))

     
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")