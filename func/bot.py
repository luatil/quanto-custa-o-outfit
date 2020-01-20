from random_outfit import random_outfit_generator

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

TELEGRAM_TOKEN = '1019291881:AAGx82A3PUae12VB6aCDwPXJRq7Uf_2F_js'


def start(bot, update):
    response_message = "hey"
    bot.send_message(
        chat_id=update.message.chat_id, text=response_message
    )

def unknown(bot, update):
    response_message = "Sorry, gal"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=response_message
    )

def get_outfit(bot, update, args):
    num_of_outfits = int(args[0])
    max_shirt_price = int(args[1])
    max_pants_price = int(args[2])
    outfit_list = random_outfit_generator(num_of_outfits, max_shirt_price, max_pants_price)
    outfit_str = "The generated outfits are:\n"
    for i, e in enumerate(outfit_list):
        new_shirt_str = e[0]['formality'] + ' ' + e[0]['color'] + ' shirt by '+ e[0]['brand'] 
        new_pants_str = e[1]['formality'] + ' ' + e[1]['color'] + ' ' + e[1]['style'] + ' pants by '+ e[1]['brand']
        outfit_price = e[0]['price'] + e[1]['price']
        outfit_str += f'Outfit number {i+1}: '+ new_shirt_str + '\n' + new_pants_str + f'.\n QuANoto cuSTa o OuTfiT:${outfit_price}k dols\n'
    bot.send_message(
        chat_id=update.message.chat_id,
        text=outfit_str
    )

def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(token=TELEGRAM_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(
        CommandHandler('start', start)
    )
    dispatcher.add_handler(
        CommandHandler('outfit', get_outfit, pass_args=True)
    )
    dispatcher.add_handler(
        MessageHandler(Filters.command, unknown)
    )

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()
