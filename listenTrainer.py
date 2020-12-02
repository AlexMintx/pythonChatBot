from chatterbot import ChatBot

bot = ChatBot(
    'Math & Time Bot',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ]
)

# Print an example of getting one math or time based response
x = input()
response = bot.get_response(x)
print(response)

y = input()
response = bot.get_response(y)
print(response)