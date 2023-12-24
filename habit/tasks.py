import os
from datetime import datetime

import pytz
import requests
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from habit.models import Habit
from habit.services import _check_frequency_weekly, _check_starting, _get_mailing_time


@shared_task
def send_message():
    """
    Отправляет уведомления о привычках, которые нужно выполнить сегодня.

    Получает текущее время и просматривает все привычки для определения, следует ли отправлять уведомление.
    """
    tz = pytz.timezone('Europe/Moscow')
    # Получаем текущее время
    current_time = datetime.now(tz).time()
    current_day = datetime.now(tz).day

    # Получаем все привычки
    habits = Habit.objects.all()

    for habit in habits:
        _check_starting(habit, current_day)
        # Разбиваем текущее время и время уведомления привычки на день, часы и минуты
        current_hour, current_minute = current_time.hour, current_time.minute
        habit_day, habit_hour, habit_minute = _get_mailing_time(habit)

        # Сравниваем часы и минуты
        if (
            habit.is_starting
            and habit_day == current_day
            and current_hour == habit_hour
            and current_minute == habit_minute
        ):
            # Получите сообщение о привычке
            message = habit.get_message()

            notifcation = habit.notification
            if notifcation == "email":
                # Отправьте уведомление по электронной почте
                subject = "Напоминание о привычке"
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [habit.user.email]
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=from_email,
                    recipient_list=recipient_list,
                    fail_silently=False,
                )
            else:
                # Отправьте уведомление по телеграму
                chat_id = habit.user.chat_id
                url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_API_TOKEN')}/sendMessage?chat_id={chat_id}&text={message}"
                requests.get(url).json()

            _check_frequency_weekly(habit)
