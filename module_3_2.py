def send_email(message, recipient, sender="university.help@gmail.com"):
    if (("@" and (".com" or ".ru" or ".net")) not in (recipient or sender) or
            ("@" or (".com" or ".ru" or ".net")) not in (recipient or sender)):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    elif sender != 'university.help@gmail.com':
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('', 'HELP.help@gmail.com', sender="niversity.help@gmail.com")
send_email('', 'university.help@gmail.com', )
send_email('', 'HELP.help@gmail.om', )
send_email('', 'HELP.helpgmail.com', )
send_email('', 'HELP.help@gmail.com', )
