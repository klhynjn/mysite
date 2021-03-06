from django.db import connection

def my_custom_sql( sql ):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        row = cursor.fetchone()
    return row
