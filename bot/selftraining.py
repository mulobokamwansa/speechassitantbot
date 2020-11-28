from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

bot = ChatBot("mwansa")

conversation = [ 
    "hello",
    "Hi there",
    "How are you doing",
    "i am doing great",
    "that is good to hear",
    "you are welcome"
]
trainer = ListTrainer(bot)
trainer.train(conversation)
trainer_corpus = ChatterBotCorpusTrainer(bot)
trainer_corpus.train( "chatterbot.corpus.english")


def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))


