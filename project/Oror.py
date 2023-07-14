import inspect
import os
import Database_func
import thirt

# Функція збереження повідомлення та повернення ехо
def message(messenger_user_id, messenger_user_name, messenger_channel_id, channel_type, text, date_time):
    info = inspect.getframeinfo(inspect.currentframe().f_back)
    name_module = os.path.splitext(os.path.basename(info.filename))[0]
    messenger = {
        'Igor': 1,
        'Anton': 2
    }.get(name_module, None)

    # перевірка та вставка юзера
    Check1 = Database_func.Check_user(messenger_user_id)
    if not Check1:
        Database_func.Insert_user(messenger_user_id, messenger_user_name, messenger)

    # перевірка та вставка юзера з каналом(чатом)
    Check2 = Database_func.Check_user_channel(messenger_user_id, messenger_channel_id)
    if not Check2:
        Database_func.Insert_user_channel(messenger_user_id, messenger_channel_id, channel_type)

    # вставка повідомлення
    Database_func.Insert_message(text, date_time, messenger_user_id, messenger_channel_id)

    # Виклик функції ехо
    text = thirt.echo(text)

    # Повернення ехо(тексту) та каналу(чату)
    return text, messenger_channel_id


# Функція виведення історії
def history(messenger_channel_id):
    result = Database_func.history(messenger_channel_id)
    return result[0], result[1]

# Видалення всіх повідомлень в каналі
def delete(messenger_channel_id):
    Database_func.Delete_all_messenges(messenger_channel_id)


