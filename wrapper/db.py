from config import *
import pymysql
import logging

# Connect to the database
def _create_connection():
    return pymysql.connect(host=MYSQL_HOST,
                            user=MYSQL_USER_NAME,
                            password=MYSQL_PASSWORD,
                            db=MYSQL_DB,
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)


def fetch_query(sql, arguments=None, get='all'):
    try:
        connection = _create_connection()
        cursor = connection.cursor()
        if arguments is None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, arguments)
        if get == 'one':
            result = cursor.fetchone()
        else:
            result = cursor.fetchall()
        cursor.close()
        connection.close()

    except BaseException as error:
        logging.error("Error occurred while fetching information {}".format(error))
        return None

    return result


def execute_query(sql, arguments):
    response = dict()
    try:
        connection = _create_connection()
        cursor = connection.cursor()
        cursor.execute(sql, arguments)
        cursor.close()
        connection.commit()
        connection.close()

        response["message"] = "Success"
        response["success"] = True
        response["last_id"] = cursor.lastrowid

    except pymysql.err.MySQLError as error:
        response["message"] = "Error while executing {}".format(error)
        response["success"] = False

    return response
