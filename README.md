# 🎵 Telegram Genius Lyrics Bot

Telegram bot for searching song lyrics and covers through Genius API

## 📋 Description

This bot allows users to find song lyrics and their covers by sending the song title and artist. The bot is integrated with Genius API to get up-to-date music information.

## 🚀 Features

- 🔍 Search songs by title and artist
- 🎨 Display song cover art
- 📝 Send full song lyrics
- 📱 Convenient Telegram interface
- ⚡️ Long text handling (automatic splitting)
- 🔄 Error handling and search status notifications

## 🛠 Installation

### Requirements

- Python 3.7+
- Internet connection
- Telegram account
- Genius Developer account

### Installing Dependencies

pip install pytelegrambotapi requests python-dotenv beautifulsoup4 lxml

Or use requirements.txt:

pip install -r requirements.txt

## 🔧 Configuration

### 1. Creating a Telegram Bot

1. Find [@BotFather](https://t.me/BotFather) on Telegram
2. Send the command /newbot
3. Follow the instructions to create a new bot
4. Copy the received token

### 2. Getting Genius API Token

1. Go to [Genius API Clients](https://genius.com/api-clients)
2. Create an account or sign in to an existing one
3. Click "New API Client"
4. Fill in the required information
5. Copy the Client Access Token

### 3. Configuration

Create a .env file in the project root directory:

TELEGRAM_TOKEN=your_telegram_bot_token
GENIUS_TOKEN=your_genius_api_token

Example:
TELEGRAM_TOKEN=1234567890:AAH123abcDEF456ghiJKL789mnoPQRstu
GENIUS_TOKEN=RuUcX123abc456DEF789ghiJKL0987654321

## ▶️ Running

### Local Run

python bot.py

### Background Run (Linux/Mac)

nohup python bot.py &

## 📱 Usage

### Bot Commands

- /start - Welcome message and instructions
- /help - Help with bot usage

### Searching Songs

Simply send a message with the song title and artist:

Bohemian Rhapsody Queen
Yesterday Beatles
Shape of You Ed Sheeran

## 📁 Project Structure

telegram-genius-bot/
│
├── bot.py              # Main bot file
├── .env               # Configuration file (create manually)
├── requirements.txt   # Project dependencies
└── README.md          # This file

## 📦 Dependencies

pytelegrambotapi>=4.0.0
requests>=2.25.1
python-dotenv>=0.19.0
beautifulsoup4>=4.10.0
lxml>=4.6.0

## ⚠️ Limitations

- Genius API rate limiting
- Some lyrics may be unavailable due to Genius restrictions
- Possible delays when processing very long texts

## 🐛 Troubleshooting

### Bot Not Responding

1. Check the correctness of tokens in the .env file
2. Make sure the bot is running
3. Check internet connection

### Lyrics Not Displaying

1. Some songs may be unavailable through the API
2. Try changing the query format
3. Make sure both title and artist are specified

### Installation Errors

# Update pip
pip install --upgrade pip

# Install dependencies individually
pip install pytelegrambotapi
pip install requests
pip install python-dotenv
pip install beautifulsoup4
pip install lxml

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details

## 👨‍💻 Author

Developed for music and Telegram enthusiasts

## 🤝 Support

If you encounter problems or have questions:

1. Check this README file
2. Make sure all dependencies are installed
3. Verify configuration correctness
4. Create an issue on GitHub (if repository is available)

## 🔄 Updates

Regularly check for dependency updates:

pip install --upgrade -r requirements.txt

---

🎵 Enjoy music with your Telegram bot!
