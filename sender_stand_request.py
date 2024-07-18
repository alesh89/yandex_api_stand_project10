# Импортируем модуль configuration, который, мы создали выше - он содержит настройки подключения и путь к документации
import configuration

# Импортируем модуль requests, который предназначен для отправки HTTP-запросов
# Это популярная библиотека, которая позволяет взаимодействовать с веб-сервисами
import requests

#Этот код отправляет HTTP GET-запрос к заданному URL-адресу, который складывается
#из базового адреса сервиса и пути к его документации, оба определены в модуле
#конфигурации. Затем он выводит HTTP-статус код ответа от сервера, который указывает
#на результат выполнения запроса.

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data

def get_docs():
    # Выполняем GET-запрос к URL, который складывается из базового URL-адреса сервиса
    # и пути к документации, заданных в модуле конфигурации
    # Функция возвращает объект ответа от сервера
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

def post_new_user(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    # URL_SERVICE и CREATE_USER_PATH объединяются для формирования полного URL для запроса
    # json=body используется для отправки данных пользователя в формате JSON
    # headers=data.headers устанавливает заголовки запроса из модуля data
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

def post_new_client_kit(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    # URL_SERVICE и CREATE_USER_PATH объединяются для формирования полного URL для запроса
    # json=body используется для отправки данных пользователя в формате JSON
    # headers=data.headers устанавливает заголовки запроса из модуля data
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=body,
                         headers=data.headers)

def get_users_table():
    # Составление полного URL пути к данным таблицы пользователей
    # путем конкатенации базового URL сервиса и конечной точки таблицы пользователей
    # Возвращает объект ответа от сервера
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)


response_create_user = post_new_user(data.user_body)
print(response_create_user.status_code)
print(response_create_user.json())
#Создан пользователь с токеном {'authToken': '5786ca10-921d-4998-b41a-a1f2264f46f3'}
response_create_kit = post_new_client_kit(data.kit_body)
print(response_create_kit.status_code)
print(response_create_kit.json())
#создан набор 'id': 8


