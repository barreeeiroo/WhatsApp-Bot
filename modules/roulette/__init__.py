'''
Roulette module
----------------------------------------------------------------------------
'''

from app.mac import mac, signals
import requests, os
import random

'''
Main funciton, all happens after this
'''
@signals.command_received.connect
def handle(message):
    if message.command == "click" or message.command == "roulette":
        if message.predicate == "-h":
            show_help(message)
        else:
            handle_command(message)
        
    
'''
Handles command
!click
'''
def handle_command(message):
    actions = ['🔫 💨 CLICK', '🔫 💨 CLICK', '🔫 💨 CLICK', '🔫 💨 CLICK', '🔫 💨 CLICK', '🔫💥😵 BANG!']
    response = random.choice(actions)
    mac.send_message(response, message.conversation)
        
        

'''
Prints help (how to use example)
'''
def show_help(message):
    answer = "*Roulette*\n*Usage:* !click \n*Example:* !click"
    mac.send_message(answer, message.conversation)
