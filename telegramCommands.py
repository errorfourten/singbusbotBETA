from singbusbot import send_message_to_owner
import logging

def check_commands(bot, update, message):
    message = message.split(" ")
    if message[0] == "/help":
        return "<b>Help Menu</b>\n/help - For a list of commands\n/settings - To add favourite bus stops\n/about - About page\n/feedback - Send feedback straight to the developer by using this format - /feedback [text]\n/stop - Stops the bot"
    elif message[0] == "/about":
        return "<b>About Page</b>\nThank you for using SingBusBot. \nPlease do check out the code at https://github.com/errorfourten/singbusbot and new ideas are always welcome."
    elif message[0] == "/start":
        return "Welcome to Singapore Bus Bot! Just enter a bus stop code or bus number to find the next bus. For example, try entering 53009 or Bishan Int or 284.\n\nDon't know what your bus stop code is? Take a look at the top right of the information boards or simply enter your bus number. \n\nYou can also send your location and it'll return the 5 nearest bus stops! \n\nTo add your favourite bus stops, use /settings \n\n /help for more information"
    elif message[0] == "/feedback":
        if message == False:
            return "Please enter feedback"
        else:
            if message[1:] == []:
                return "Please enter some feedback"
            else:
                send_message_to_owner(bot, " ".join(message[1:]))
                return "Thank you for your feedback! \"{}\"".format(" ".join(message[1:]))
    elif message[0] == "/broadcast":
        if message[1:] == False:
            return False
        else:
            return " ".join(message[1:])
    elif message[0] == "/stop":
        return "Thank you for using SingBusBot! Please use /start to restart it anytime."
    else:
        return False
