import requests
import telebot
from telebot import types
import os
from dotenv import load_dotenv

# Loading environment variables from a .env file
load_dotenv()

# Tokens
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
GENIUS_TOKEN = os.getenv('GENIUS_TOKEN')

# Bot initialization
bot = telebot.TeleBot(TELEGRAM_TOKEN)

GENIUS_HEADERS = {
    'Authorization': f'Bearer {GENIUS_TOKEN}'
}


def search_song(query):
    """Search for a song using the Genius API"""
    search_url = 'https://api.genius.com/search'
    params = {'q': query}

    try:
        response = requests.get(search_url, params=params, headers=GENIUS_HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error while searching: {e}")
        return None


def get_song_info(song_id):
    """getting information about a song"""
    song_url = f'https://api.genius.com/songs/{song_id}'

    try:
        response = requests.get(song_url, headers=GENIUS_HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error retrieving information: {e}")
        return None


def get_lyrics(url):
    """Getting lyrics from a web page"""
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Simple HTML parsing to extract text
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # We are looking for an element with song lyrics
        lyrics_div = soup.find('div', class_='lyrics')
        if lyrics_div:
            return lyrics_div.get_text().strip()

        # An alternative way to search for text
        lyrics_divs = soup.find_all('div', attrs={'data-lyrics-container': 'true'})
        if lyrics_divs:
            lyrics = '\n'.join([div.get_text('\n') for div in lyrics_divs])
            return lyrics.strip()

        return "Song lyrics not found"
    except Exception as e:
        print(f"Error receiving text: {e}")
        return "Error receiving text"


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = """
🎵 *Song Lyrics Search*

Send me the song title and artist, for example:
`Bohemian Rhapsody by Queen`
`Yesterday by Beatles`
`Shape of You by Ed Sheeran`

The bot will find the lyrics and cover art!
"""
    bot.reply_to(message, welcome_text, parse_mode='Markdown')


@bot.message_handler(func=lambda message: True)
def search_song_handler(message):
    query = message.text.strip()

    if not query:
        bot.reply_to(message, "Please enter the title of the song")
        return

    # Sending a search message
    search_msg = bot.reply_to(message, "🔍 I'm looking for a song...")

    try:
        # Search for a song
        search_result = search_song(query)

        if not search_result or not search_result['response']['hits']:
            bot.edit_message_text("😔 Song not found. Try changing your search.",
                                  message.chat.id, search_msg.message_id)
            return

        # We take the first result
        hit = search_result['response']['hits'][0]
        song = hit['result']

        song_id = song['id']
        title = song['title']
        artist = song['primary_artist']['name']
        song_url = song['url']
        thumbnail_url = song.get('song_art_image_thumbnail_url') or song.get('header_image_thumbnail_url')

        # We get complete information about the song
        song_info = get_song_info(song_id)
        if song_info and 'response' in song_info:
            song_data = song_info['response']['song']
            # Getting the lyrics
            lyrics = get_lyrics(song_url)
        else:
            lyrics = get_lyrics(song_url)

        # Forming a response
        caption = f"🎵 *{title}*\n🎤 {artist}\n\n"

        # We send the cover with a signature
        if thumbnail_url:
            try:
                bot.send_photo(
                    message.chat.id,
                    thumbnail_url,
                    caption=caption + "The lyrics are posted below. ⬇️",
                    parse_mode='Markdown'
                )
            except:
                # If you were unable to send a photo, we will send only the text.
                bot.send_message(message.chat.id, caption, parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, caption + "Cover not found", parse_mode='Markdown')

        # Sending song lyrics
        if lyrics and lyrics != "Error retrieving text":
            # Break long text into parts if necessary
            if len(lyrics) > 4096:
                parts = [lyrics[i:i + 4096] for i in range(0, len(lyrics), 4096)]
                for part in parts:
                    bot.send_message(message.chat.id, part)
            else:
                bot.send_message(message.chat.id, lyrics)
        else:
            bot.send_message(message.chat.id, "😔 The lyrics are unavailable.")

        # Removing the search message
        bot.delete_message(message.chat.id, search_msg.message_id)

    except Exception as e:
        bot.edit_message_text(f"❌ An error occurred: {str(e)}",
                              message.chat.id, search_msg.message_id)


if __name__ == '__main__':
    print("The bot has been launched...")
    bot.infinity_polling()