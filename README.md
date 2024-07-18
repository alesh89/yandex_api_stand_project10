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
|   1                                                        | Допустимое количество символов (1):kit_body = {"name": "a"}  | Код ответа — 201 В ответе поле name совпадает с полем name в запросе      |
|   2                                                        | 10.32.252.31  | ksis-srv-db-new   |
