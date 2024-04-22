IAM_TOKEN = 't1.9euelZqSz83Pko3GyseMz5mXi4mcku3rnpWajc6WmM-Mlc-axs-UjY6Yksvl8_cLHmhO-e8sZFN5_N3z90tMZU757yxkU3n8zef1656Vmsiex8uXnYqLk8qVnp2dzpCP7_zF656Vmsiex8uXnYqLk8qVnp2dzpCPveuelZqWmcmTysyPmMqPzMqcjs2Mm7XehpzRnJCSj4qLmtGLmdKckJKPioua0pKai56bnoue0oye.AacSPWeTu9qRbcmUg8RG5UDla2ZDrEJPxXU9GCrFHdYdE3leMQXJw_oG6mOcgHk20M1O4pNFW4gXx3GBgPUfBw'
FOLDER_ID = 'b1g6m8id5nb5e6q5vqv1'
TOKEN = '6802015710:AAEtTwywOdf3ITfXkVHSIGHDsKDRneZBHtU'

MAX_USERS = 3  # максимальное кол-во пользователей
MAX_GPT_TOKENS = 120  # максимальное кол-во токенов в ответе GPT
COUNT_LAST_MSG = 4  # кол-во последних сообщений из диалога

# лимиты для пользователя
MAX_USER_STT_BLOCKS = 10  # 10 аудиоблоков
MAX_USER_TTS_SYMBOLS = 5000  # 5 000 символов
MAX_USER_GPT_TOKENS = 2000  # 2 000 токенов

HOME_DIR = '/home/student/gpt_bot'  # путь к папке с проектом
LOGS = f'{HOME_DIR}/logs.txt'  # файл для логов
DB_FILE = f'{HOME_DIR}/messages.db'  # файл для базы данных

IAM_TOKEN_PATH = f'{HOME_DIR}/creds/iam_token.txt'  # файл для хранения iam_token
FOLDER_ID_PATH = f'{HOME_DIR}/creds/folder_id.txt'  # файл для хранения folder_id
BOT_TOKEN_PATH = f'{HOME_DIR}/creds/bot_token.txt'  # файл для хранения bot_token
SYSTEM_PROMPT = [{'role': 'system', 'text': 'Ты веселый собеседник. Общайся с пользователем на "ты" и используй юмор. '
                                            'Поддерживай диалог. Не объясняй пользователю, что ты умеешь и можешь. '
                                            'Изображай человека'}]  # список с системным промтом