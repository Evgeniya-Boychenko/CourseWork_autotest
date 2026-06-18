import pymysql
import allure


def test_check_database_structure():
    """Проверяем структуру базы данных"""
    # Подключаемся к БД
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='user',
        password='12345',
        database='app'
    )

    try:
        with connection.cursor() as cursor:
            # Получаем список всех таблиц
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()

            print("\n СПИСОК ТАБЛИЦ В БАЗЕ")
            for table in tables:
                print(f"- {table[0]}")

            # Для каждой таблицы показываем структуру
            for table in tables:
                table_name = table[0]
                print(f"\n СТРУКТУРА ТАБЛИЦЫ '{table_name}'")
                cursor.execute(f"DESCRIBE {table_name}")
                columns = cursor.fetchall()
                for column in columns:
                    print(f"  {column[0]} - {column[1]}")

                # Показываем первые 5 записей
                print(f"\n ПЕРВЫЕ 5 ЗАПИСЕЙ В ТАБЛИЦЕ '{table_name}'")
                cursor.execute(f"SELECT * FROM {table_name} LIMIT 5")
                rows = cursor.fetchall()
                for row in rows:
                    print(f"  {row}")
    finally:
        connection.close()