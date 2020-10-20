# Asyncio client/server

## Description
**Есть пакет REQ (реквест) и его ожидаемая репрезентация RESP (респонс).
Используя asyncio cоздать клиент и сервер.**

### Клиент:
1) Шлёт реквест

2) Ожидает респонс от сервера


### Сервер:
1) Ожидает любой входящий пакет и превращает его в ожидаемую репрезентацию.

2) Ожидает случайный таймаут от 1 до 5 секунд.

3) Реквесты принимаются и обрабатываются асинхронно.

Это значит, что если клиент ~ одновременно отправит два реквеста на которые выпадает таймаут 2 и 3 секунды соответственно, то первый респонс будет получен спустя ~ 2 секунды после отправки, а второй спустя ~ 3.

`&&` - разделитель параметров
`%%` - разделитель сущностей

Формат пакета JSON:
Пакет содержит:
`request_id` - уникальный идентификатор реквеста
`data` - поле с данными которые нужно конвертить в ожидаемый формат

### Структура `data`:
`{Entity_name}&&{param1name}&&{param1value}&&{param2name}&&{param2value}...%%{Entity_name}...`

Пустые элементы не должны входить в конечный результат.
Пример:
Формат: JSON с полями request_id и data

`REQ =
{ 
	"request_id": "01",
	"data": "Hub&&name&&qwe&&id&&123&&%%Device&&name&&wqe&&id&&234&&"
	}`


`RESP =
{ 
	'request_id': '01', 
	'data': {
		'Hub': {'name': 'qwe', 'id': '123'},
		'Device': {'name': 'wqe', 'id': '234'} 
			}
}`

-----

## Running

Firstly you have to download python modules from requirements.txt using:
```bash
pip install -r requirements
```

or
```bash
pip install websockets
```

After that you have to execute `python3 server.py` and after that you can test how it works, launching `python3 client.py`.

-----

## How it works

When the server is running it can concurrently serve to miliple clients and their requests due to `asyncio` built-in library.
Due to the task condition server randomly picks from 1 to 5 seconds timeout for **each request** - that means that a single client can send many requests - work on this requests using `make_response()` function and then send the result back.  
Also it displays in concole - what timeout was for this particular request:
```bash
Timeout 3.4 seconds for this one.
Timeout 1.7 seconds for this one.
```

The `make_response()` function takes string, that had to be a dict (becouse it was jsonifyied) and does a pretty dict-response to this particular request by converting information by splitting `data`-key values by **%%** and **&&**
 Then we send this RESP to the server, usning `json.dumps(RESP)`.