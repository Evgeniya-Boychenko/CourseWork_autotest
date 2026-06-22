import pymysql

class DBHelper:
    """Класс для работы с базой данных"""
    @staticmethod
    def get_last_payment_status():
        connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='user',
            password='12345',
            database='app'
        )

        try:
            with connection.cursor() as cursor:
                sql = "SELECT status FROM payment_entity ORDER BY created DESC LIMIT 1"
                cursor.execute(sql)
                result = cursor.fetchone()

                if result:
                    return result[0]
                return None
        finally:
            connection.close()

