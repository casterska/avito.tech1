# Баг-репорты для микросервиса https://qa-internship.avito.com
#### 1. `200 OK` при отправлении запроса с ручкой GET /api/1/`sellerId`/item, где sellerId является несуществующим(например, -1).
Шаги воспрозведения: 
```curl --location 'https://qa-internship.avito.com/api/1/-1/item'```
ОР: Статус-код 404, сообщение об ошибке "Продавец не найден"
ФР: Статус-код 200, в теле ответа массив объявлений
Приоритет: `Высокий`
Окружение: https://qa-internship.avito.com
---
#### 2. `200 OK` при отправлении запроса с ручкой GET /api/1/`sellerId`/item, где sellerId передан в неверном формате(например, "sellerId").
Шаги воспрозведения: 
```curl --location 'https://qa-internship.avito.com/api/1/sellerid/item'```
ОР: Статус-код 400, сообщение об ошибке "Неверный формат sellerId"
ФР: Статус-код 200, в теле ответа массив объявлений, где все параметры "sellerId" принимают значение 0
Приоритет: `Высокий`
Окружение: https://qa-internship.avito.com
---
### 3. `500 Internal Server Error` при отправлении запроса с ручкой POST https://qa-internship.avito.com/api/1/item и пустым объектом JSON.
Шаги воспроизведения:
```curl
curl --location 'https://qa-internship.avito.com/api/1/item' \
--header 'Content-Type: application/json' \
--data '{
}'
```
ОР: Статус-код 400, сообщение об ошибке "Обязательное поле отсутствует"
ФР: Статус-код 500, сообщение об ошибке `{"message":"internal error","code":500}`
Приоритет: `Высокий`
Окружение: https://qa-internship.avito.com
---
### 4. `200 OK` при отправлении запроса с ручкой POST https://qa-internship.avito.com/api/1/item и отрицательным значением в параметре "price".
Шаги воспроизведения:
```curl
curl --location 'https://qa-internship.avito.com/api/1/item' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Телефон",
    "price": -500,
    "sellerId": 999999,
    "statistics": {
        "contacts": 32,
        "like": 35,
        "viewCount": 14
    }
}'
```
ОР: Статус-код 400 Bad Request, сообщение об ошибке "Неверное значение цены"
ФР: Статус-код 200 OK, сообщение об ошибке `{"status": "Сохранили объявление - cb411bab-78ba-4468-82b4-0f692e9f4403"}`
Приоритет: `Высокий`
Окружение: https://qa-internship.avito.com
---
### 5. `500 Internal Server Error` при отправлении запроса с ручкой POST https://qa-internship.avito.com/api/1/item и строкой в значении параметра "price".
Шаги воспроизведения:
```curl
curl --location 'https://qa-internship.avito.com/api/1/item' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Телефон",
    "price": "Двадцать два",
    "sellerId": 999999,
    "statistics": {
        "contacts": 32,
        "like": 35,
        "viewCount": 14
    }
}'
```
ОР: Статус-код 400, сообщение об ошибке "Обязательное поле отсутствует"
ФР: Статус-код 500, сообщение об ошибке `{"message":"internal error","code":500}`
Приоритет: `Высокий`
Окружение: https://qa-internship.avito.com
---
### 6. `200 OK` при отправлении запроса с ручкой POST https://qa-internship.avito.com/api/1/item и отсутвующем параметре "sellerId" в теле запроса.
Шаги воспроизведения:
```curl
curl --location 'https://qa-internship.avito.com/api/1/item' \
--header 'Content-Type: application/json' \
--data '{
"name": "Товар без продавца",
"price": 100432,
"statistics": {
        "contacts": 32,
        "like": 35,
        "viewCount": 14
    }
}'
```
ОР: Статус-код 400 Bad Request, сообщение об ошибке "sellerId обязателен"
ФР: Статус-код 200 OK, сообщение об ошибке `{"status": "Сохранили объявление - 24eb6b76-8796-485c-a9ab-4a0f42b5bbda"}`
Приоритет: `Высокий`
Окружение: https://qa-internship.avito.com
---
### 7. `200 OK` при отправлении запроса с ручкой POST https://qa-internship.avito.com/api/1/item и отрицательными значениями в параметрах "statistics" в теле запроса.
Шаги воспроизведения:
```curl
curl --location 'https://qa-internship.avito.com/api/1/item' \
--header 'Content-Type: application/json' \
--data '{
"name": "Телефон",
"price": 13000,
"sellerId": 3452,
    "statistics": {
    "contacts": -5,
    "like": -10,
    "viewCount": -3
    }
}'
```
ОР: Статус-код 400, сообщение об ошибке "Значения статистики не могут быть отрицательными"
ФР: Статус-код 200 OK, сообщение об ошибке `{"status": "Сохранили объявление - 1c1cbe58-45c4-4731-86b4-0f49b08a527b"}`
Приоритет: `Высокий`
Окружение: https://qa-internship.avito.com
---
### 8. `500 Internal Server Error` при отправлении запроса с ручкой POST https://qa-internship.avito.com/api/1/item и целым числом в значении параметра "name".
Шаги воспроизведения:
```curl
curl --location 'https://qa-internship.avito.com/api/1/item' \
--header 'Content-Type: application/json' \
--data '{
    "name": 10,
    "price": 12131,
    "sellerId": 999999,
    "statistics": {
        "contacts": 32,
        "like": 35,
        "viewCount": 14
    }
}'
```
ОР: Статус-код 400, сообщение об ошибке "Параметр "name" некорректный ввод"
ФР: Статус-код 500, сообщение об ошибке `{"message":"internal error","code":500}`
Приоритет: `Высокий`
Окружение: https://qa-internship.avito.com
---
### 9. `500 Internal Server Error` при отправлении запроса с ручкой POST https://qa-internship.avito.com/api/1/item и строкой в значении параметра "sellerId".
Шаги воспроизведения:
```curl
curl --location 'https://qa-internship.avito.com/api/1/item' \
--header 'Content-Type: application/json' \
--data '{
"name": "Телефон",
"price": 21313,
"sellerId": "продавец",
    "statistics": {
    "contacts": 5,
    "like": 10,
    "viewCount": 3
    }
}'
```
ОР: Статус-код 400, сообщение об ошибке "Параметр "sellerId" некорректный ввод"
ФР: Статус-код 500, сообщение об ошибке `{"message":"internal error","code":500}`
Приоритет: `Высокий`
Окружение: https://qa-internship.avito.com
---
### 10. `500 Internal Server Error` при отправлении запроса с ручкой POST https://qa-internship.avito.com/api/1/item и массивом в значении параметра "statistics".
Шаги воспроизведения:
```curl
curl --location 'https://qa-internship.avito.com/api/1/item' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Телефон",
    "price": 100,
    "sellerId": 999999,
    "statistics": [
        {
            "contacts": 32,
            "like": 35,
            "viewCount": 14
        }
    ]
}'
```
ОР: Статус-код 400, сообщение об ошибке "Параметр "statistics" некорректный ввод"
ФР: Статус-код 500, сообщение об ошибке `{"message":"internal error","code":500}`
Приоритет: `Высокий`
Окружение: https://qa-internship.avito.com
---
### 11. `500 Internal Server Error` при отправлении запроса с ручкой POST https://qa-internship.avito.com/api/1/item и строкой в значении параметра "contacts".
Шаги воспроизведения:
```curl
curl --location 'https://qa-internship.avito.com/api/1/item' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Телефон",
    "price": 100,
    "sellerId": 999999,
    "statistics": {
        "contacts": "контакт",
        "like": 35,
        "viewCount": 14
    }
}'
```
ОР: Статус-код 400, сообщение об ошибке "Параметр "contacts" некорректный ввод"
ФР: Статус-код 500, сообщение об ошибке `{"message":"internal error","code":500}`
Приоритет: `Высокий`
Окружение: https://qa-internship.avito.com
---
### 12. `500 Internal Server Error` при отправлении запроса с ручкой POST https://qa-internship.avito.com/api/1/item и строкой в значении параметра "contacts".
Шаги воспроизведения:
```curl
curl --location 'https://qa-internship.avito.com/api/1/item' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Телефон",
    "price": 100,
    "sellerId": 999999,
    "statistics": {
        "contacts": "контакт",
        "like": 35,
        "viewCount": 14
    }
}'
```
ОР: Статус-код 400, сообщение об ошибке "Параметр "contacts" некорректный ввод"
ФР: Статус-код 500, сообщение об ошибке `{"message":"internal error","code":500}`
Приоритет: `Высокий`
Окружение: https://qa-internship.avito.com
---
### 13. `200 OK` при отправлении запроса с ручкой POST https://qa-internship.avito.com/api/1/item и строкой в значении параметра "like" в теле запроса.
Шаги воспроизведения:
```curl
curl --location 'https://qa-internship.avito.com/api/1/item' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Телефон",
    "price": 100,
    "sellerId": 999999,
    "statistics": {
        "contacts": 32,
        "like": "like",
        "viewCount": 14
    }
}'
```
ОР: Статус-код 400, сообщение об ошибке "Параметр "like" некорректный ввод"
ФР: Статус-код 200 OK, сообщение об ошибке `{"status": "Сохранили объявление - e074fea3-b337-4334-a26d-7f3756a8fdd9"}`
Приоритет: `Высокий`
Окружение: https://qa-internship.avito.com
---
### 14. `500 Internal Server Error` при отправлении запроса с ручкой POST https://qa-internship.avito.com/api/1/item и строкой в значении параметра "viewCount" в теле запроса.
Шаги воспроизведения:
```curl
curl --location 'https://qa-internship.avito.com/api/1/item' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Телефон",
    "price": 100,
    "sellerId": 999999,
    "statistics": {
        "contacts": 32,
        "like": 35,
        "viewCount": "viewCount"
    }
}'
```
ОР: Статус-код 400, сообщение об ошибке "Параметр "viewCount" некорректный ввод"
ФР: Статус-код 500, сообщение об ошибке `{"message":"internal error","code":500}`
Приоритет: `Высокий`
Окружение: https://qa-internship.avito.com
---
### 15. Неверное значение в теле ответа у параметра "like", при отправлении запроса с ручкой GET https://qa-internship.avito.com/api/1/item/id
Предусловие:
- Отправить запрос с ручкой POST https://qa-internship.avito.com/api/1/item и телом запроса для сохранения объявления:
```json
{
"name": "Телефон",
"price": 85566,
"sellerId": 321321,
"statistics": {
        "contacts": 32,
        "like": 35,
        "viewCount": 14
    }
}
```
Шаги воспроизведения:
```curl
curl --location 'https://qa-internship.avito.com/api/1/item/cd429a23-f32c-4bd4-bc8f-9d1e1e31de27'
```
ОР: В параметре "like" значение == переданному значению при сохранении объявления (35).
ФР: В параметре "like" значение == 0.
Приоритет: `Высокий`
Окружение: https://qa-internship.avito.com