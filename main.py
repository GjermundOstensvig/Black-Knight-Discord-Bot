import discord
import random
from config import *

# Commands:
#
# Everyone can use:
#     !HELP    -    A student needs help and is added to the queue.
#     !SHOWQUEUE    -    Show everyone standing in line.
#     !KNIGHT    -     The Black Knight will cite random quotes from
#     Monty Python The Holy Grail.
#     !LEAVE    -    If you no longer wish to stand in line,
#     you can leave the queue.
#
# Teachers assistants can slao use:
#     !NEXT    -    I'm done helping a student and can start helping
#     the next one. (removes the next student from the queue).
#     Do this before each Teachers assistants class:
#     !CLEARCHAT    -    Removes all messages in the chat.
#     !CLEARQUEUE    -    Removes all students in the queue.
#
# The program reads and writes to the csv file help_queue.csv so that the data is not lost if the bot crashes.

help_queue = []
client = discord.Client()


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name} (id: {guild.id})'
    )
    with open('help_queue.txt', 'r') as txt_file:
        temp = txt_file.read().splitlines()
        for line in temp:
            help_queue.append(line)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    knight_quotes = [
        'None shall pass.',
        'Then you shall die.',
        'I move for no man.',
        '\'Tis but a scratch.',
        'I\'ve had worse.',
        'Come on you pansy!',
        'Have at you!',
        'Just a flesh wound.',
        'Chicken! Chicken!',
        'The Black Knight always triumphs! Have at you! Come on then.',
        'I\'ll bite your legs off!!'
    ]

    if message.content == '!KNIGHT':
        response = random.choice(knight_quotes)
        await message.channel.send(response)

    elif message.content == '!QUEUE':
        # Checks if the student is already in the list.
        for member in help_queue:
            if str(message.author) == str(member):
                response = f'Hold your horses there {message.author}! You are already in line!'
                await message.channel.send(response)
                return
        # Append to file
        with open('help_queue.txt', 'a') as txt_file:
            txt_file.write(f'{str(message.author)}\n')

        # Append to in-program list
        help_queue.append(str(message.author))
        response = f'You, {message.author} will have to stand in line! \nYou are number {len(help_queue)}.'
        await message.channel.send(response)

    elif message.content == '!SHOWQUEUE':
        # Lists all of the waiting students.
        if len(help_queue) > 0:
            response = 'These are the peasants standing in line: '
            count = 1
            for member in help_queue:
                response += f'\n {count}. {member}'
                count += 1
            await message.channel.send(response)
        else:
            response = 'Victory is mine 🗡 🗡 🗡 There are no more peasants standing in line.'
            await message.channel.send(response)

    elif message.content == '!NEXT':
        authorized = False
        for role in message.author.roles:
            if role.name == "@TA":
                authorized = True

        if not authorized:
            response = f'Nice try {message.author}, but you lack the authority to do that!💢'
            await message.channel.send(response)
        elif not len(help_queue) > 0:
            response = f'Haha, I\'m invincible! There are no students in line. Have at you!'
            await message.channel.send(response)
        else:
            response = f'Next student in line is {help_queue[0]}. \nI have taken this person out of the queue.'
            help_queue.pop(0)

            # Create new list to override old list with
            temp = ''
            for student in help_queue:
                temp += f'{student}\n'
            with open('help_queue.txt', 'w') as txt_file:
                txt_file.write(temp)

            await message.channel.send(response)

    elif message.content == '!CLEARCHAT':
        authorized = False
        for role in message.author.roles:
            if role.name == "@TA":
                authorized = True

        if not authorized:
            response = f'Nice try {message.author}, but you lack the authority to do that!'
            await message.channel.send(response)
        else:
            # Delete 100 messages in chat
            await message.channel.purge(limit=100)

    elif message.content == '!CLEARQUEUE':
        authorized = False
        for role in message.author.roles:
            if role.name == "@TA":
                authorized = True

        if not authorized:
            response = f'Nice try {message.author}, but you lack the authority to do that!'
            await message.channel.send(response)
        else:
            # Clear out the queue
            help_queue.clear()
            with open('help_queue.txt', 'r+') as txt_file:
                txt_file.truncate(0)

            response = f'All students in the list have been deleted by {message.author}'
            await message.channel.send(response)

    elif message.content == '!LEAVE':
        # Check if the student is in the liste.
        if str(message.author) in help_queue:
            help_queue.remove(str(message.author))
            response = f'So you figured it out yourself huh?\nYou {message.author} have been removed from the queue.'
            # Create new list to override old list with
            temp = ''
            for student in help_queue:
                temp += f'{student}\n'
            with open('help_queue.txt', 'w') as txt_file:
                txt_file.write(temp)

            await message.channel.send(response)
        else:
            response = f'You can\'t leave the queue if you\'re not in the queue!'
            await message.channel.send(response)
client.run(TOKEN)