#----------RECYCLE BIN----------

'''if db["responding"]:
        options = starter_encouragements
        if "encouragements" in db.keys():
            options = options + db["encouragements"]

    if msg.startswith("$new"):
        encouraging_message = msg.split("$new", 1)[1]
        update_encouragements(encouraging_message)
        await message.channel.send("New encouraging message added.")
        await message.channel.send("New encouraging message  added.")

    if msg.startswith("$del"):
        encouragements = []
        if "encouragements" in db.keys():
            index = int(msg.split("$del", 1)[1])
            delete_encouragement(index)
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)

    if msg.startswith("$list"):
        encouragements = []
        if "encouragements" in db.keys():
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)
        
def list_loop(name, x, list_1, list_2): 
  value = 0
  for i in range(x): 
    value+=1
    l=list_1[value]
    d=list_2[value]
    setheading(name,l,d) 
        '''

'''
    json_data = response.json()
    main = json_data['main']
		temperature = main['temp']
		humidity = main['humidity']
		pressure = main['pressure']
		report = json_data['weather']
		return(main)
		return(temperature)
		return(humidity)
		return(pressure)
		return(report)
		await message.channel.send(main)
		await message.channel.send(temperature)
		await message.channel.send(humidity)
		await message.channel.send(pressure)
		await message.channel.send(report)
'''
'''#--------Datetime----------------      

    if msg.startswith('$time'):
        await message.channel.send ("Hour : ", end = "") 
        await message.channel.send (current_time.hour)
        await message.channel.send ("Minute : ", end = "")
        await message.channel.send (current_time.minute)
        await message.channel.send ("Second : ", end = "")
        await message.channel.send (current_time.second)
        await message.channel.send ("Microsecond : ", end = "") 
        await message.channel.send (current_time.microsecond) 
            
    if msg.startswith('$date'):
        await message.channel.send ("Year : ", end = "") 
        await message.channel.send (current_time.year)
        await message.channel.send ("Month : ", end = "")
        await message.channel.send (current_time.month)
        await message.channel.send ("Day : ", end = "") 
        await message.channel.send (current_time.day)'''
     
    #-----------Trivia--------------
		
'''if msg.startswith('$trivia'):
			await channel.send(f"Let's play a game of trivia! There are {len(trivia_questions)} questions")
        for i in range(len(trivia_questions)):
            await message.channel.send (trivia_questions[i - 1])
            await message.channel.send ('Are you ready to see the answer?')
            if msg.startswith('yes'):
                await message.channel.send (trivia_answers[i-1])
                await message.channel.send ('Did you get it correct?')
                if msg.startswith('yes'):
                    await message.channel.send('Good job!')
                else:
                    await message.channel.send('Better luck next time')
										'''

'''if msg.startswith('$numberguess'):
	for i in range(len(numbers)):
		r = (random.choice(numbers))
		message.channel.send('Pick a number 1-10')
		message.channel.send('Type your number in the chat now!')
		message.channel.send(r)
		message.channel.send('Did you guess correctly?')
		if msg.startswith('yes'):
			message.channel.send('Good job!')
		else:
			message.channel.send('Better luck next time')'''

#----------IMPORTS----------

import discord
import os
import requests
import json
import random
from datetime import date, datetime
from replit import db
from discord.ext import commands
from urllib import parse, request
import re
import random

#----------VARIABLES----------

client = discord.Client()
#current_time = datetime.datetime.now() 
bot = commands.Bot(command_prefix='>', description="This is a Helper Bot")

#----------LISTS----------

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encouragements = ["Cheer up!", "Hang in there.", "You are a great person / bot!"]

zodiacMeanings = ['You are eager, dynamic, quick, and competetive', 'You are strong, dependable, sensual, and creative', 'You are versatile, expresive, curious, and kind', 'You are intuitive, sentimental, compassionite, and protective', 'You are dramatic, outgoing, fiery, and self-assured', 'You are practical, loyal, gentle, and analytical', 'You are social, fair-minded, diplomatic, and gracious', 'You are passionate, stubborn, resourceful, and brave', 'You are extroverted, optimistic, funny, and generous', 'You are serious, independent, diciplined, tenacious', 'You are deep, imaginitive, original, and uncomprovising', 'You are affectionate, empathetic, wise, and artistic']

trivia_questions = ['True or false: Glow Worm caves exist in New Zealand ', 
  'Prarie dogs greet each other with ____ ', 
  'How many questions does a four year old ask each day? ',
  'Han Son Doong cave in Vietnam is the biggest cave in the world. It has its own___, a) jungle, b) river, c) climate, d) all of the above ',
  'True or false: M&M stands for Mars and Moordale ']

trivia_answers = ['true', 'kisses', '300', 'd', 'false']

numbers = ['1','2','3','4','5','6','7','8','9','10']

#----------DEFINITIONS----------

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)


def get_weather():
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?")
    json_data = json.loads(response.text)
    weather = json_data
    return(weather)


def update_encouragements(encouraging_message):
    if "encouragements" in db.key():
        encouragements = db["encouragements"]
        encouragements.append(encouraging_message)
        db["encouragements"] = encouragements
    else:
        db["encouragements"] = [encouraging_message]

def delete_encouragement(index):
    encouragements = db["encouragements"]
    if len(encouragements) > index:
        del encouragements[index]
        db["encouragements"] = encouragements


#----------MAIN-CODE----------

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    

@client.event
async def on_message(message):
    #--------!if statements----------
    if message.author == client.user:
        return

    if "responding" not in db.keys():
        db["responding"] = True
    
    #--------!Variables----------
    msg = message.content

    channel = message.channel

    #------!Discord Functions-----

    #------Help-------------------
    if msg.startswith('$help'):
        await channel.send('Bot Commands:\n$inspire: get a motivational quote \n$zodiacaries: aries horoscope reading \n$zodiactaurus: taurus horoscope reading \n$zodiacgemini: gemini horoscope reading \n$zodiaccancer: cancer horoscope reading \n$zodiacleo: leo horoscope reading \n$zodiacvirgo: virgo horoscope reading \n$zodiaclibra: libra horoscope reading \n$zodiacscorpio: scorpio horoscope reading \n$zodiacsagittarius: sagittarius horoscope reading \n$zodiaccapricorn: capricorn horoscope reading \n$zodiacaquarius: aquarius horoscope reading \n$zodiacpisces: pisces horoscope reading')
        
    #------------Responding---------
    if msg.startswith("$responding"):
        value = msg.split("$responding", 1)[1]

        if value.lower() == "true":
            db["responding"] = True
            await message.channel.send("Responding is on.")
        else: 
            db["responding"] = False
            await message.channel.send("Responding is off.")

    #------Quotes API----------------
    if msg.startswith('$inspire'):
        quote = get_quote()
        await channel.send(quote)

    #-----Weather API----------------
    if msg.startswith("$weather"):
        await message.channel.send(get_weather())  

    #-----Sad Word Trigger--------
    if any(word in msg for word in sad_words):
            await channel.send(random.choice(starter_encouragements))
            
    #------reply -------------------
    if msg.startswith('$greet'):
        await channel.send('Say hello!')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send('Hello {.author}!'.format(msg))
    #------Zodiac----------------------     
    if msg.startswith('$zodiacaries'):
            await channel.send(zodiacMeanings[0])
    if msg.startswith('$zodiactaurus'):
            await channel.send(zodiacMeanings[1])
    if msg.startswith('$zodiacgemini'):
            await channel.send(zodiacMeanings[2])
    if msg.startswith('$zodiaccancer'):
            await channel.send(zodiacMeanings[3])
    if msg.startswith('$zodiacleo'):
            await channel.send(zodiacMeanings[4])
    if msg.startswith('$zodiacvirgo'):
            await channel.send(zodiacMeanings[5])
    if msg.startswith('$zodiaclibra'):
            await channel.send(zodiacMeanings[6])
    if msg.startswith('$zodiacscorpio'):
            await channel.send(zodiacMeanings[7])
    if msg.startswith('$zodiacsagittarius'):
            await channel.send(zodiacMeanings[8])
    if msg.startswith('$zodiaccapricorn'):
            await channel.send(zodiacMeanings[9])
    if msg.startswith('$zodiacaquarius'):
            await channel.send(zodiacMeanings[10])
    if msg.startswith('$zodiacpisces'):
            await channel.send(zodiacMeanings[11])

	#----------Number Guess-----------
    if msg.startswith('$numberguess'):
        for i in range(len(numbers)):
            def yesorno(n):
                return n.content == 'hello' and n.channel == channel
            msg = await client.wait_for('message', check=check)
            await channel.send('Hello {.author}!'.format(msg))
            r = (random.choice(numbers))
            await message.channel.send('Pick a number 1-10')
            await message.channel.send('Type your number in the chat now!')
            await message.channel.send(r)
            await message.channel.send('Did you guess correctly?')
            if msg.startswith('yes'):
                await message.channel.send('Good job!')
            elif msg.startswith('no'):
                await message.channel.send('Better luck next time')
			
		#--------Counting----------------
    
    if msg.startswith('$count'):
        n = 1
        while n < 101:
            return (n)
            await channel.send(n)
            n = n+1
        else:
            await channel.send('This is the highest we can count.')
    	
#----------RUNNING-CODE----------

client.run(os.getenv('TOKEN'))