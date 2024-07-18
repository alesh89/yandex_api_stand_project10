# Тесты на проверку параметра name при создании набора продуктов в Яндекс.Прилавок с помощью API Яндекс.Прилавок.
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполянется командой pytest

## Описание проекта
Проект содержит следующие файлы:
- configuration.py: URL и пути запросов;
- sender_stand_request.py: файл отправки запросов;
- data.py: файл с данными;
- create_kit_name_kit_test.py: файл с написанными тестами;
- README.md;
- .gitignore.

## Проверки выполнялись по следующему чек-листу:
| №                                                          | Описание | ОР      |
|-----------------------------------------------------------------------------|---------------|-------------------|
|   1                                                        | Допустимое количество символов (1):<br>kit_body = {"name": "a"}  | Код ответа — 201<br> В ответе поле name совпадает с полем name в запросе      |
|   2                                                        | Допустимое количество символов (511):<br>kit_body = {"name":"Тестовое значение для этой проверки будет ниже"}  | Код ответа — 201<br>В ответе поле name совпадает с полем name в запросе   |
|   3                                                        | Количество символов меньше допустимого (0):<br>kit_body = {"name": ""}  | Код ответа — 400   |
|   4                                                        | Количество символов больше допустимого (512):<br>kit_body = {"name":"Тестовое значение для этой проверки будет ниже"} | Код ответа — 400   |
|   5                                                        | Разрешены английские буквы:<br>kit_body = {"name": "QWErty"}  | Код ответа — 201<br>В ответе поле name совпадает с полем name в запросе   |
|   6                                                        | Разрешены русские буквы:<br>kit_body = {"name": "Мария"}  | Код ответа — 201<br>В ответе поле name совпадает с полем name в запросе   |
|   7                                                        | Разрешены спецсимволы:<br>kit_body = {"name": ""№%@","}  | Код ответа — 201<br>В ответе поле name совпадает с полем name в запросе   |
|   8                                                        | Разрешены пробелы:<br>kit_body = {"name": " Человек и КО "}  | Код ответа — 201<br>В ответе поле name совпадает с полем name в запросе   |
|   9                                                        | Разрешены цифры:<br>kit_body = {"name": "123"}  | Код ответа — 201<br>В ответе поле name совпадает с полем name в запросе   |
|   10                                                        | Параметр не передан в запросе:<br>kit_body = {}  | Код ответа — 400   |
|   11                                                        | Передан другой тип параметра (число):<br>kit_body = {"name": 123}  | Код ответа — 400   |

_Тестовые значения для проверок №2 и №4:_
# _Допустимое количество символов (511):_
kit_body = {    "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}
