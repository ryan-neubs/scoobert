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

from discord.ext import commands

# Bot Startup/Connection

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Commands

@bot.command(name='howdy')
async def howdy(ctx):
    embedVar = discord.Embed()
    embedVar.add_field(name='Scoobert', value='Hi There!')
    await ctx.send(embed=embedVar)

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
            move = 1
        if not user.bot and reaction.emoji == '📰':
            move = 2
        if not user.bot and reaction.emoji == '✂':
            move = 3


@bot.command(name='shutdown')
@commands.is_owner()
async def stop(ctx):
    await ctx.send('Scoobert is now going offline...')
    await ctx.bot.logout()
    quit()



# Purged commands

###@bot.command(name='hatecrime')
###async def hatecrime(ctx, amount=20, user: discord.User, message='Fuck You :)'):
###    for i in range(int(amount)):
###        await user.send(message)

bot.run(TOKEN)