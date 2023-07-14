import Oror
import datetime

def message(messenger_user_id, messenger_user_name, messenger_channel_id, channel_type, text, date_time):
    result = Oror.message(messenger_user_id, messenger_user_name, messenger_channel_id, channel_type, text, date_time)
    text = result[0]
    messenger_channel_id = result[1]
    print (text , messenger_channel_id)

def history(messenger_channel_id):
    result = Oror.history(messenger_channel_id)
    text = result[0]
    messenger_channel_id = result[1]
    print (text , messenger_channel_id)

def delete(messenger_channel_id):
    Oror.delete(messenger_channel_id)

message("jgwfueg", "Ігор", "7253672", "Public", "Привіт", datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

history("7253672")

delete("7253672")
