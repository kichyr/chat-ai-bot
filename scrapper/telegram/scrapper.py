import re

from telethon import TelegramClient
from telethon.tl.types import InputPeerChat

chat_id = -1001598191827
api_id=17447832
api_hash = 'f97d220bc8b95f04a0dbf20c40473fe8'
russian_filter = re.compile('[А-Яа-яЁё_\-,!?()\ ]+')

client = TelegramClient('session_id', api_id=api_id, api_hash=api_hash)

with client:
    # 10 is the limit on how many messages to fetch. Remove or change for more.
    for msg in client.iter_messages(chat_id):
        print('<s>', msg.text, '</s>')


def message_filter(message):
    pass