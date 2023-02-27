import telegram

# Replace YOUR_TOKEN with your bot token obtained from BotFather
bot = telegram.Bot(token='6166592308:AAHFI7yM1qq9HtbI7ki5OCpIUL_uNCsrsNQ')

# Replace PERFORMER_CHAT_ID with the chat ID of the performer
performer_chat_id = '332376718'

# Prompt the user for their username
username = input('Please enter your username: ')

# Prompt the user for their phone number
phone_number = input('Please enter your phone number: ')

# Prompt the user for their cadastral number
cadastral_number = input('Please enter your land cadastral number: ')

# Prompt the user for their photo copyright
photo_copyright = input('Please enter your photo copyright: ')

# Send the collected data to the performer
message = f'Username: {username}\nPhone number: {phone_number}\nCadastral number: {cadastral_number}\nPhoto copyright: {photo_copyright}'
bot.send_message(chat_id=performer_chat_id, text=message)
