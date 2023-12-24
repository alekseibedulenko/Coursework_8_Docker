# Atomic Habits App

Добро пожаловать в приложение "Atomic Habits"! Это приложение поможет вам управлять вашими привычками и целями, соблюдать регулярность и отслеживать свой прогресс. В этом README мы предоставим вам информацию о проекте и его настройках.

## Описание проекта

Atomic Habits - это веб-приложение, разработанное для помощи пользователям создавать, отслеживать и поддерживать полезные привычки. Приложение предоставляет возможность создавать привычки, устанавливать напоминания и отслеживать выполнение целей.

## Стек технологий

Проект разработан с использованием следующего технологического стека:

- Python 3.11
- Django: веб-фреймворк для создания веб-приложений
- Django REST framework: библиотека для создания RESTful API
- Celery: для асинхронных задач
- Redis: как брокер сообщений для Celery
- HTML/CSS: для пользовательского интерфейса

## Инструкция по установке

Чтобы развернуть проект и начать использовать его, выполните следующие шаги:

1. **Склонируйте репозиторий**: Выполните команду Git для клонирования репозитория на свой локальный компьютер.

   ```bash
   git clone https://github.com/alekseibedulenko/Coursework_7_DRF
2. **Установите зависимости::**

   ```bash
   cd atomic_habits
   pip install -r requirements.txt
3. **Настройте файл .env: Создайте файл .env в корневой директории проекта и добавьте в него переменные среды, например:**
- SECRET_KEY='your_secret_key'
- DOMAIN_NAME='http://127.0.0.1:8000/'
- DATABASES_NAME='your_database_name'
- DATABASES_PASSWORD='your_database_password'
- EMAIL_HOST_USER='your_email@gmail.com'
- EMAIL_HOST_PASSWORD='your_email_password'
- CACHES_LOCATION='redis://127.0.0.1:6379'
- ADMIN_PASSWORD='your_admin_password'
- CHAT_ID_ADMIN='your_chat_id'
- MODERATOR_EMAIL='your_moderator_email'
- STRIPE_API_KEY='your_stripe_api_key' #необязательно
- CELERY_BROKER_HOST='redis://127.0.0.1:6379/0'
- TELEGRAM_API_TOKEN='your_telegram_api_token'
4. **Выполните миграции для создания базы данных:**

   ```bash
   python manage.py migrate
5. **Запустите приложение:**
   
   ```bash
   python manage.py runserver
6. **Откройте приложение:** Перейдите в веб-браузере по адресу http://127.0.0.1:8000/ и начните использовать приложение.
## Краткая инструкция по эндпоинтам
В приложении "Atomic Habits" есть несколько важных эндпоинтов:
* /habits/ - список и создание привычек.
* /habits/<int:pk>/ - просмотр, обновление и удаление привычки.
* /habits/public/ - список публичных привычек.

## Обратите внимание Celery для Windows
**Запустите Celery для асинхронной обработки задач, таких как отправка уведомлений:**
  ```bash
  celery -A atomic_habits worker -l info -P eventlet
  celery -A atomic_habits beat
  ```

## Автор проекта
Этот проект создан, и поддерживается Алексеем Бедуленко.

Если у вас есть вопросы или предложения по улучшению проекта, свяжитесь со мной по адресу levabox1@mail.ru

<em>Спасибо, что выбрали "Atomic Habits" для управления вашими привычками!</em>

# Курсовая 8. Docker


## Установите Docker и Docker Compose:

* Установите Docker, следуя инструкциям для вашей операционной системы: [Docker Install](https://docs.docker.com/get-docker/).
* Установите Docker Compose: [Docker Compose Install](https://docs.docker.com/compose/install/).

## Создайте файл .env-non-dev:

* Создайте файл .env-non-dev в той же директории, где находится ваш файл docker-compose.yml. В этом файле укажите все необходимые переменные окружения для ваших сервисов (например, базы данных, Redis, вашего приложения и Celery).
## Запустите приложение:

* Откройте терминал в директории с файлом docker-compose.yml.
* Выполните следующую команду:
    ```bash
        docker-compose up
Docker Compose загрузит образы, создаст и запустит контейнеры для ваших сервисов.
## Проверьте приложение:

После успешного запуска, ваше приложение atomic_habits должно быть доступно по адресу http://localhost:7777.
## Остановите приложение:

* В терминале, где была запущена команда docker-compose up, нажмите Ctrl+C для остановки контейнеров.