# Объявления - Django RESTful API

Этот проект представляет собой небольшое приложение, разработанное на базе Django и Django REST framework, для управления объявлениями. Приложение включает модели для категорий объявлений, городов и объявлений, а также предоставляет API для просмотра списка объявлений и получения детальной информации о каждом объявлении.
Перейдите в директорию проекта:

shell

cd advert-management

Создайте и активируйте виртуальное окружение (рекомендуется, но не обязательно):

shell

python -m venv venv
source venv/bin/activate  # Для Unix/Linux
venv\Scripts\activate  # Для Windows

Установите зависимости:

shell

pip install -r requirements.txt

Примените миграции:

shell

python manage.py migrate

Запустите сервер разработки:

shell

    python manage.py runserver

После этого, проект будет доступен по адресу http://localhost:8000/.

### Получение детальной информации об объявлении

- Эндпоинт: `/api/advert/<id>/`
- Метод: GET
- Описание: Получите детальную информацию о конкретном объявлении. Просмотр данного объявления увеличивает счетчик просмотров.

## Установка и Запуск

Следуйте этим инструкциям, чтобы установить и запустить проект локально:

1. Склонируйте репозиторий:

   ```shell
   git clone https://github.com/adcurse22/advert-management.git


   python -m venv venv
source venv/bin/activate   Для Unix/Linux
venv\Scripts\activate  Для Windows

Установите зависимости:



pip install -r requirements.txt

Запустите миграции:



python manage.py migrate

Запустите сервер разработки:

python manage.py runserver
