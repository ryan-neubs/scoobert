#bot.py

import os
import random
import discord
import doomsday
from tiktactoe import *
from random import randint
from time import sleep
from discord.ext.commands.errors import BadArgument
from dotenv import load_dotenv

#1
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#2
bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='howdy')
async def howdy(ctx):
    embedVar = discord.Embed()
    embedVar.add_field(name='Scoobert', value='Hi There!')
    await ctx.send(embed=embedVar)


"""@bot.command(name='hatecrime')
async def hatecrime(ctx, amount=20, user: discord.User, message='Fuck You :)'):
    for i in range(int(amount)):
        await user.send(message)"""

@bot.command(name='dice')
async def dice(ctx, sides=6, amount=1):
    if sides < 4:
        await ctx.send(
        '''Please enter 4 or more sides (default = 6).
Command syntax: $dice [sides] [dice]''')
    elif amount < 1:
        await ctx.send(
            '''Please enter 1 or more dice (default 1).'''
        )
    else:
        await ctx.send('Rolling a %s sided die %d time(s)...' % (sides, amount))
        s = ""
        for i in range(amount):
            newNum = (random.randrange(1, sides + 1))
            s += str(newNum) + " "
        await ctx.send(s)
        
@dice.error
async def dice_error(ctx, error):
    await ctx.send("Please only use whole numbers.")

@bot.command(name='killcarlo')
async def killcarlo(ctx):
    await ctx.send("That mf gone", file=discord.File("scoobert//video0.mp4"))

@bot.command(name='dayofweek')
async def dayofweek(ctx, date):
    dow = doomsday.main(date)
    if dow == False:
        await ctx.send('Invalid date, check your date and try again. \nFormat: DD/MM/YYYY')
    response = '{' + date + ' is a ' + dow + '}'
    await ctx.send(response)

@bot.command(name='TicTacToe')
async def TicTacToe(ctx):
    rematch = True
    await ctx.send("Welcome to TicTacToe!")
    await ctx.send("Tiles are labeled like so:")
    await ctx.send("""----------------
    |[t1]|[t2]|[t3]|
    ----------------
    |[t4]|[t5]|[t6]|
    ----------------
    |[t7]|[t8]|[t9]|
    ----------------
    """)
    await ctx.send("Game will start in 10 seconds...")
    sleep(10)
    while rematch != False:
        await ctx.send("\nAssigning Symbols...")
        sleep(3)
        turn = randint(0,1)
        if turn == 0:
            game = TicTacToe('X')
            await ctx.send('X will go first.')
        else:
            game = TicTacToe('O')
            await ctx.send('O will go first.')
        # Fancy countdown thing to make sure player is ready, just cuz
        sleep(1)
        await ctx.send("\nGame begins in:")
        await ctx.send("5...")
        sleep(1)
        await ctx.send("4...")
        sleep(1)
        await ctx.send("3...")
        sleep(1)
        await ctx.send("2...")
        sleep(1)
        await ctx.send("1...")
        sleep(1)

        # Start of game
        while game.gameover() == False and game.checktie() == False:
            await ctx.send(game.table)
            await ctx.send("Turn:", game.turn)
            move = str(input("What is your move? (t1, t3, t6, etc):"))
            while True:
                if game.validmove(move):
                    game.mark(game.turn, move)
                    break
                else:
                    await ctx.send(game.table)
                    await ctx.send("Tile is taken or input was incorrect, try again.")
                    await ctx.send("Turn:", game.turn)
                    move = str(input("What is your move? (t1, t3, t6, etc):"))
        
        # Code to execute once gameover == True
        if game.checktie() == True and game.gameover() == False:
            await ctx.send(game.table)
            await ctx.send("Game has ended in a draw!")
        else:
            game.switchturn()
            await ctx.send(game.table)
            await ctx.send(game.turn, 'Wins!')
        restart = str(input("Play again? (Y/n):"))
        if restart == 'Y' or restart == 'y':
            rematch = True
        else:
            rematch = False
            await ctx.send("Goodbye!")


@bot.command(name='sendlove')
async def sendlove(ctx, user: discord.User, *, message="Here's a hug!"):
    embed = discord.Embed(description=user.mention + " " + message)
    embed.set_image(url="https://cdn.discordapp.com/attachments/875083768963145781/895153950385377320/hug.gif")
    await ctx.send(embed=embed)

@bot.command(name='rps')
async def rps(ctx):
    embed = discord.Embed()
    embed.add_field(name="Rock, Paper, Scissors", value="Select your move!")
    msg = await ctx.send(embed=embed)
    reactions = ['🪨','📰','✂']
    for emoji in reactions:
        await msg.add_reaction(emoji)

@bot.event
async def on_reaction_add(reaction, user): 
        if not user.bot and reaction.emoji == '🪨':
            print('Rock')
        if not user.bot and reaction.emoji == '📰':
            print('Paper')
        if not user.bot and reaction.emoji == '✂':
            print('Scissors')

@bot.event
async def on_message(message):
    channel = bot.get_channel(id=877018249567547414)
    if '69' in message.content:
        await channel.send("Nice.") 

@bot.command(name='shutdown')
@commands.is_owner()
async def stop(ctx):
    await ctx.send('Scoobert is now going offline...')
    await ctx.bot.logout()
    quit()


bot.run(TOKEN)
