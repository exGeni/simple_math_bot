import requests
import time
import json
from math_generator import generate_examples, format_number
from config import TELEGRAM_BOT_TOKEN

import logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log'
)

# Set up the bot URL using the token from config
URL = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/'

def get_updates(offset=0):
    """
    Get updates from Telegram server
    :param offset: ID of the first update to be returned
    :return: JSON object of updates
    """
    url = URL + f'getUpdates?offset={offset}'
    response = requests.get(url)
    return json.loads(response.content)

def send_message(chat_id, text):
    """
    Send a message to a specific chat
    :param chat_id: ID of the chat to send the message to
    :param text: Text of the message to be sent
    """
    url = URL + f'sendMessage?chat_id={chat_id}&text={text}&parse_mode=HTML'
    requests.get(url)

def format_examples(examples):
    """
    Format the generated examples for output
    :param examples: List of generated examples
    :return: Formatted string of examples
    """
    operations = ["Сложение", "Вычитание", "Умножение", "Деление"]
    formatted = ""
    for i, operation in enumerate(operations):
        formatted += f"<b>{operation}:</b>\n"
        for example in examples[i]:
            formatted += f"{example}\n"
        formatted += "\n"  # Add an empty line between operations
    return formatted.strip()  # Remove trailing whitespace

def handle_message(message):
    """
    Handle incoming messages and commands
    :param message: Message object from Telegram
    """
    chat_id = message['chat']['id']
    text = message.get('text', '').lower()

    if text == '/start':
        send_message(chat_id, "Привет! Я бот для генерации математических примеров. Я могу помочь тебе попрактиковаться в решении задач разной сложности. Используй следующие команды:\n\n/easy - для получения легких примеров\n/medium - для примеров средней сложности\n/hard - для сложных примеров\n/help - для получения справки\n\nУдачи в тренировках!")
    elif text == '/help':
        send_message(chat_id, "Я могу генерировать математические примеры трех уровней сложности:\n\n/easy - легкие примеры\n/medium - примеры средней сложности\n/hard - сложные примеры\n\nПросто выбери команду, и я пришлю тебе набор примеров для практики!")
    elif text in ['/easy', '/medium', '/hard']:
        level = 1 if text == '/easy' else (2 if text == '/medium' else 3)
        examples = generate_examples(level, 5)
        formatted_examples = format_examples(examples)
        difficulty = "легкие" if level == 1 else ("средней сложности" if level == 2 else "сложные")
        send_message(chat_id, f"Вот {difficulty} примеры для тебя:\n\n<pre>{formatted_examples}</pre>\n\nУдачи в решении!")
    else:
        send_message(chat_id, "Извини, я не понимаю эту команду. Используй /help, чтобы узнать, какие команды я понимаю.")

def main():
    """
    Main function to run the bot
    """
    logging.info("Bot started")
    offset = 0
    while True:
        try:
            updates = get_updates(offset)
            for update in updates['result']:
                offset = update['update_id'] + 1
                message = update.get('message', {})
                if message:
                    handle_message(message)
        except requests.RequestException as e:
            logging.error(f"Network error occurred: {e}")
        except json.JSONDecodeError as e:
            logging.error(f"JSON decoding error: {e}")
        except Exception as e:
            logging.error(f"Unexpected error occurred: {e}", exc_info=True)
        time.sleep(1)