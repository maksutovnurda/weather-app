# Weather App 

> Видео демонстрация приложении [Смотрите здесь](https://s3.twcstorage.ru/d7b5f88d-sheber-education/for_myself/for_github.mp4)

Django-приложение для просмотра погоды

## Онлайн версия

Приложение также доступно онлайн по адресу: http://195.133.146.14:8083/

> **Примечание**: Я загрузил его в свой тестовый сервер, если сервер недоступен, вы можете запустить приложение локально, следуя инструкциям ниже 👇🏻

## Требования

- Python 3.8+
- Django 4.2+
- requests

## Установка

1. Клонируйте репо:
```bash
git clone https://github.com/maksutovnurda/weather-app
cd weather-app
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```


## Запуск проекта

1. Перейдите в src:
```bash
cd src
```

3. Запустите сервер:
```bash
python manage.py runserver
```

Приложение будет доступно по адресу `http://localhost:8000`

## API

### История поиска
Для просмотра истории последних поисков:
```
GET /api/search-history/
```

## Функциональность

- Поиск информации о погоде
- Отслеживание истории поиска
- Интеграция с https://open-meteo.com/