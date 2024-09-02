# Способы вызова функции
def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if not recipient.endswith(('.ru', '.com', '.net')) or not sender.endswith(('.ru', '.com', '.net')) \
            or not '@' in recipient or not '@' in sender:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient == sender:  # пункт 3 письмо 4
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':  # пункт 4 письмо 1
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')