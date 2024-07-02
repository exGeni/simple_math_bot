# Math Example Generator Bot

This Telegram bot generates mathematical examples of varying difficulty levels for practice.

## Architecture

The project consists of the following components:

1. `bot.py`: Main bot logic and message handling
2. `math_generator.py`: Example generation functions
3. `config.py`: Configuration file for bot token
4. `run_bot.py`: Entry point for running the bot

```
Math Example Generator Bot
│
├── bot.py
├── math_generator.py
├── config.py
├── run_bot.py
├── requirements.txt
└── README.md
```

## Setup

1. Clone the repository
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Create a `config.py` file with your bot token:
   ```python
   TELEGRAM_BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'
   ```
4. Run the bot:
   ```
   python run_bot.py
   ```

## Usage

The bot responds to the following commands:
- `/start`: Introduces the bot and lists available commands
- `/help`: Provides information about the bot's functionality
- `/easy`: Generates easy math examples
- `/medium`: Generates medium difficulty math examples
- `/hard`: Generates hard math examples

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).