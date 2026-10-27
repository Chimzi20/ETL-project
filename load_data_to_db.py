
from extract import extract_data

from db_connect import connection, cursor

fema_data = []
api_data = extract_data()

fema_data.extend(api_data)

postgres_data = [ (data['disasterNumber'], data['incidentType'], data['projectSize'])
                 for data  in fema_data]

insert_query = """
    INSERT INTO fema_data(disasterNumber, incidentType, projectSize)
    VALUES(%s, %s, %s)
"""
cursor.executemany(insert_query, postgres_data)

connection.commit()
print('Data loaded successfully')

cursor.close()
connection.close()


