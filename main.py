#Invite Link for MadLibs bot
#https://discord.com/api/oauth2/authorize?client_id=939546855036039229&permissions=8&scope=bot


import discord
from discord.ext import commands
import os
import random

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="madlibs"))


pickup_lines = [
    'I wanna c ddle, but I can’t without u',
    'are u a fart? cuz you just blew me away 😩',
    'if covid doesnt take you out i will',
    "Are you the ∑(1/n^2) from 1 to ∞? Because my heart converges absolutely to you",
    'Is ur name earl gray cuz u look like a hot-tea',
    '👉 👈 is that an airplane? Or did my heart just take off',
    '🥴 if you were a booger id pick u',
    'are you a banana? because you are very appealing',
    'Did you sabotage O2 because you take my breath away ',
    'if you were a burger at mcdonalds ud be mcgorgeous', 'my love for you is like explosive diarrhea, i just cant hold it in',
    'do you happen to have a band-aid? i just scraped my knee falling for u',
    'Imma complain to Spotify for u not being named this weeks hottest single',
    'I wanna take u to the movies but they don’t let u bring ur own snacks',
    'I’d never play hide and seek w u bc someone like u is impossible to find',
    'You know what you would look great in? My arms',
    'I always thought happiness started w an h but it turns out mine starts w u',
    'I believe in following my dreams so can I have ur insta',
    'Ur hands looks heavy can I hold it for u ',
    'I must be in a museum cuz ur a piece of art',
    'Kiss me if I’m wrong but dinosaurs still exists right?',
    'I’m not drunk I’m just intoxicated by you',
    'Do u have a name or can I call u mine'
]


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.help'):
        channel = message.channel
        await channel.send('Type .amogus or .ls to begin madlibbing. Type .pickup to get a random pickup line.')

    if message.content.startswith('.amogus'):
        channel = message.channel

        def check(m):
            return True

        await channel.send('Enter an adjective:')
        x1 = await client.wait_for('message', check=check)

        await channel.send('Enter a color:')
        x2 = await client.wait_for('message', check=check)

        await channel.send('Enter a location:')
        x3 = await client.wait_for('message', check=check)

        await channel.send('Enter an adjective:')
        x4 = await client.wait_for('message', check=check)

        await channel.send('Enter a clothing Item:')
        x5 = await client.wait_for('message', check=check)

        await channel.send('Enter a verb:')
        x6 = await client.wait_for('message', check=check)

        await channel.send('Enter a verb ending with -ed:')
        x7 = await client.wait_for('message', check=check)

        await channel.send('Enter an adjective:')
        x8 = await client.wait_for('message', check=check)

        await channel.send('Enter an adjective:')
        x9 = await client.wait_for('message', check=check)

        await channel.send('Enter a verb:')
        x10 = await client.wait_for('message', check=check)

        await channel.send('Enter my color: ')
        x11 = await client.wait_for('message', check=check)

        await channel.send('Enter an adjective:')
        x12 = await client.wait_for('message', check=check)

        await channel.send('Enter a verb ending with -ed:')
        x13 = await client.wait_for('message', check=check)

        await channel.send('It was a {.content} day on Polus'.format(x1))
        await channel.send('I saw {.content}'.format(x2) + ' heading towards {.content}'.format(x3))
        await channel.send('they looked {.content}'.format(x4)+', wearing {.content}'.format(x5))
        await channel.send('So I decided to {.content}'.format(x6))
        await channel.send('When we got to {.content}'.format(x3)+', they {.content}'.format(x7))
        await channel.send('This made me incredibly {.content},'.format(x8))
        await channel.send('so I called an emergency meeting.')
        await channel.send('I tried to tell everyone they were {.content}'.format(x9))
        await channel.send('and that they {.content}'.format(x7)+', but {.content}'.format(x2))
        await channel.send('responded with one sentence:')
        await channel.send('"{.content} was sus."'.format(x11))
        await channel.send('and then it was time to {.content}'.format(x10)+'.')
        await channel.send('they all voted for {.content}'.format(x11)+' and {.content} looked '.format(x2)+'{.content}'.format(x12))
        await channel.send('They {.content}. And I dieded. :('.format(x13))


    if message.content.startswith('.ls'):
      channel = message.channel

      def check(m):
        return True

      await channel.send('Enter an adjective:')
      ADJ1 = await client.wait_for('message', check=check)

      await channel.send('Enter an adjective:')
      ADJ2 = await client.wait_for('message', check=check)

      await channel.send('Enter a body part:')
      BODYPART1 = await client.wait_for('message', check=check)

      await channel.send('Enter a noun:')
      NOUN1 = await client.wait_for('message', check=check)

      await channel.send('Enter a verb:')
      VERB1 = await client.wait_for('message', check=check)

      await channel.send('Enter a verb:')
      VERB2 = await client.wait_for('message', check=check)

      await channel.send('Enter a verb:')
      VERB3 = await client.wait_for('message', check=check)

      await channel.send('Enter a noun:')
      NOUN2 = await client.wait_for('message', check=check)

      await channel.send('Enter an exclamation:')
      EXCLAMATION1 = await client.wait_for('message', check=check)

      await channel.send('Enter a noun:')
      NOUN3 = await client.wait_for('message', check=check)

      await channel.send('Enter a verb: ')
      VERB4 = await client.wait_for('message', check=check)

      await channel.send('Enter an verb:')
      VERB5 = await client.wait_for('message', check=check)

      await channel.send('Enter an exclamation:')
      EXCLAMATION2 = await client.wait_for('message', check=check)

      await channel.send('Enter a noun:')
      NOUN6 = await client.wait_for('message', check=check)

      await channel.send('Enter a verb:')
      VERB6 = await client.wait_for('message', check=check)

      await channel.send('Enter a verb:')
      VERB7 = await client.wait_for('message', check=check)

      await channel.send('Enter a verb:')
      VERB8 = await client.wait_for('message', check=check)

      await channel.send('Enter a noun:')
      NOUN7 = await client.wait_for('message', check=check)

      await channel.send('Enter a noun:')
      NOUN8 = await client.wait_for('message', check=check)

      await channel.send('Enter a verb:')
      VERB9 = await client.wait_for('message', check=check)

      await channel.send('Enter an adverb:')
      ADVERB1 = await client.wait_for('message', check=check)

      await channel.send('Enter an adjective:')
      ADJ3 = await client.wait_for('message', check=check)

      await channel.send('Enter a verb:')
      VERB10 = await client.wait_for('message', check=check)

      await channel.send('Enter a verb:')
      VERB11 = await client.wait_for('message', check=check)
      
      await channel.send('When I first saw you you looked {.content}'.format(ADJ1)+' and {.content}. I couldn’t'.format(ADJ2))
      await channel.send('believe my {.content}.'.format(BODYPART1)+' You smelled like {.content} and you'.format(NOUN1))
      await channel.send('{.content}'.format(VERB1)+' over to me. I wanted to {.content}'.format(VERB2)+' with you. I {.content} you'.format(VERB3))
      await channel.send('if I could take you out to {.content}'.format(NOUN2)+' and you said {.content}. I'.format(EXCLAMATION1))
      await channel.send('gave you a {.content}'.format(NOUN3)+' and you {.content}.'.format(VERB4)+' I {.content} you out and you'.format(VERB5))
      await channel.send('said {.content}'.format(EXCLAMATION2)+' so we went to {.content}'.format(NOUN6)+' for our first')
      await channel.send('{.content}'.format(VERB6)+'. I loved {.content}'.format(VERB7)+' with you. When you {.content}'.format(VERB8)+' me I felt')
      await channel.send('{.content}'.format(NOUN7)+'. I saw {.content}'.format(NOUN8)+' when you {.content} at me'.format(VERB9))
      await channel.send('and I knew we were meant to be. After this {.content} date'.format(ADVERB1))
      await channel.send('I was so {.content}'.format(ADJ3)+' to {.content}'.format(VERB10)+' you home. I {.content}'.format(VERB11)+' you.')
    
    
    if message.content.startswith('.pickup'):
      await message.channel.send(random.choice(pickup_lines))

client.run(os.getenv('TOKEN'))
