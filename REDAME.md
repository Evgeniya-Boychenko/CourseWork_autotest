# "Автоматизация тестирования сервиса Aqa-Shop"

Курсовой проект по профессии "Инженер по тестированию".  
Автоматизация тестирования сервиса покупки туров. Тестируем форму оплаты дебетовой картой. Проверяем UI (сообщения об успехе/ошибке, валидация полей) и БД (статусы APPROVED/DECLINED). Язык Python, инструменты: Selenium, pytest, Allure.

## Начало работы

Клонируйте репозиторий командой git clone [по ссылке](https://github.com/Evgeniya-Boychenko/CourseWork_autotest)

### Prerequisites

ОС Windows 10/11  
Python версии 3.10 и выше  
браузер (Chrome) - для выхода в Интернет, запуска автотестов  
PyMySQL -библиотека для подключения к БД  
Git - для доступа к проекту  
Docker + Docker Compose - для запуска БД MySQL в контейнере  
Java - для работы приложения  
Selenium - для автоматизации веб-тестирования  
pytest - фреймворк для запуска тестов  
allure-pytest - для генерации визуальных HTML отчетов  
Любой текстовый редактор (VS Cоde) - для доступа к коду  
Необходимо скачать файл [aqa-shop.jar](https://github.com/netology-code/aqa-qamid-diplom/blob/main/aqa-shop.jar)  
Файл с учетными данными и подключениями [application.properties](https://github.com/netology-code/aqa-qamid-diplom/blob/main/application.properties)  

### Установка и запуск

1. Клонирование репозитория: 
   командой git clone [по ссылке](https://github.com/Evgeniya-Boychenko/CourseWork_autotest)
   
2. Установка зависимостей Python
- Cоздание виртуального окружения: python -m venv venv
- Активация: venv/Scripts/activate
- Установка библиотек: pip install -r requirements.txt

3. Запуск базы данных (Docker)
- Команда: docker-compose up -d
- Чтобы проверить, что база запустилась:
  1. Открыть программу Docker Desktop.
  2. В левом меню нажать вкладку Containers
  3. В списке должна быть строка с именем aqa_shop
  4. Слева от имени должен быть зеленый кружок.
  

4. Запуск тестируемого приложения
- Команда: java -jar aqa-shop.jar
- Адрес по которому открывается приложение: http://localhost:8080
- Чтобы проверить, что приложение запустилось перейти по ссылке http://localhost:8080

### Запуск тестов
- Команда для запуска тестов: pytest
- Команда для запуска с генерацией Allure:  
1 Команда собирает данные
  pytest tests/ --alluredir=./allure-results  
2 Команда открывает отчет в браузере
  allure serve ./allure-results

### Остановка окружения
Остановить приложение: в терминале команда Ctrl + C  
Остановить базу данных:  в терминале docker-compose down

### Примеры
После запуска тестов в терминале отображается: 16 passed, 1 xfailed   
Отчёт Allure автоматически открывается в браузере с детальной статистикой.
[скрин отчета](docs/screenshots/report_allure_all_tests.png)

### Лицензия
Проект создан в учебных целях

### Ссылки на документацию

- [План автоматизации](docs/Plan.md) 
- [Отчёт о тестировании](docs/Report.md)
- [Отчёт об автоматизации](docs/Summary.md) 

### Важно
Если у вас установлен локальный MySQL, остановите его перед запуском Docker, чтобы не было конфликта порта 3306
   
