from app.mac import mac, signals

'''
Signals this module listents to:
1. When a message is received (signals.command_received)
==========================================================
'''
@signals.command_received.connect
def handle(message):
    if message.command == "hi":
        hi(message)
    elif message.command == "help": 
        help(message)
    elif message.command == "dev" or message.command == "creator" or message.command == "developer" or message.command == "barreiro": 
        creator(message)
    elif message.command == "makeroid": 
        makeroid(message)

'''
Actual module code
==========================================================
'''
def hi(message):
    who_name = message.who_name
    answer = "Hi " + who_name
    mac.send_message(answer, message.conversation)

def help(message):
    answer = "*Bot called BarrePolice* \nWhatsApp Bot made in Python \n*Version:* 0.1.0 \n*Status:* Beta \nhttps://github.com/barreeeiroo/WhatsApp-Bot"
    mac.send_message(answer, message.conversation)

def makeroid(message):
    answer = "*Check Makeroid!* \nhttps://www.makeroid.io"
    mac.send_message(answer, message.conversation)
    
def creator(message):
    answer = "*Developed by Diego Barreiro* \nhttps://barreeeiroo.github.io"
    mac.send_message(answer, message.conversation)
