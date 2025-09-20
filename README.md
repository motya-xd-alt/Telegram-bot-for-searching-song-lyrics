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


### Installation Errors


🎵 Enjoy music with your Telegram bot!
