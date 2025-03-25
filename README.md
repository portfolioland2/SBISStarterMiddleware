### Установка
>python - windows, python3 - linux
1. `python -m venv venv`
2. Windows: `.\venv\Scripts\Activate.ps1` Linux: `source ./venv/bin/activate`
3. `pip install -r ./reqs.txt`
4. `uvicorn --host 0.0.0.0 --port 7777 application.app:app --reload`

### Управление

`curl --location --request POST 'http://127.0.0.1:7777/sync-pos'` 		-- Отправить на шлюз категории и блюда
`curl --location --request POST 'http://127.0.0.1:7777/webhook/orders'` -- Отправить вебхук для создания заказа

### Переменные среды

```.env
BASE_URL=												# Адрес, на котором работает сервис интеграции (этот)
SBIS_BASE_URL=https://api.sbis.ru/retail				# API СБИС Presto
SBIS_AUTH_URL=https://online.sbis.ru/oauth/service/		# API OAuth2 CБИС
SBIS_APP_CLIENT_ID=										# Данные для получения токена СБИС
SBIS_APP_SECRET=										# Данные для получения токена СБИС
SBIS_SECRET_KEY=										# Данные для получения токена СБИС
STARTER_BASE_URL=https://pos-gateway.starterapp.ru/api	# API Стартер
STARTER_API_KEY=										# Токен Стартер
#CRON_SYNC_MENUS=*/5 * * * *							# (не оттестированно) правило CRON для меню (каждые 5 минут)
#CRON_SYNC_SHOPS=0 0 * * *								# (не оттестированно) правило CRON для точек (н/д)
#CRON_SYNC_ORDERS=* * * * *								# (не оттестированно) правило CRON для заказов (каждую минуту)
```

