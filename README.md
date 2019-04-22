# kahootBot
Bot which joins kahoot quizzes and answers questions

This project was a fun idea brought about by one of my classmates.

What this project does is offer you an easy way through which you can join kahoot games with multiple bots using the BotInstance
class.

# packages

This Bot requires selenium, in order to install it copy the following line in the terminal:

pip install selenium

#files

kahootBot.py is the file containing the bot class

with main.py you can make bots enter the games and answer questions at random.

with sprawler.py you can make bots answer the questions like you do.

note: special_names() is a method with which you can make multiple variations of one name (interspersed with spaces or dots) and
the option for naming the bots this way will be shown

#issues

if the quiz is private the bots will not be able to join it
the bots cannot automatically answer to questions (if anyone knows how to remotely get the quizID message me)
the bots do not run concurrently which can be an issue (say one of the bots gets kicked and the ones following after him are waiting for it to answer the question)
