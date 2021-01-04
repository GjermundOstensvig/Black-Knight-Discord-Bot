# Black-Knight-Discord-Bot
Helpful Discord bot for tutoring hours with TAs.
The bot controls a queue of students that needs help with school work.

The Discord Bot needs Python 3.7 to work. At the time I wrote this bot, the Discord module did not work with newer versions of Python.

Use the requirements.txt file to install the required packages:
pip install -r requirements.txt

To use this bot, go to the config.py file and add the Token and Guild name.

Commands to use with this bot:

Everyone can use:
* !HELP    -    A student needs help and is added to the queue.
* !SHOWQUEUE    -    Show everyone standing in line.
* !KNIGHT    -     The Black Knight will cite random quotes from Monty Python The Holy Grail.
* !LEAVE    -    If you no longer wish to stand in line, you can leave the queue.

 Teachers assistants can slao use:
 * !NEXT    -    I'm done helping a student and can start helping the next one. (removes the next student from the queue).
 * !CLEARCHAT    -    Removes all messages in the chat.
 * !CLEARQUEUE    -    Removes all students in the queue.

The program reads and writes to the csv file help_queue.csv so that the data is not lost if the bot crashes.

The Discord bot no longer needs hardcoded TA usernames, they just need t have the Role "@TA"
