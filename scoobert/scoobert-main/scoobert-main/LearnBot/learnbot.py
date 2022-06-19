#learnbot.py

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '.')

@bot.event
async def on_ready():
    print('Bot is ready')

@bot.event
async def on_connect():
    print('Bot has connected to Discord')

@bot.event
async def on_disconnect():
    print('Bot has disconnected from Discord')

@bot.event
async def on_member_join(ctx, member):
    print(f'{member} has joined the server!')
    await ctx.send(f"Hello, {member}, welcome to the server!")

@bot.event 
async def on_member_remove(ctx, member):
    print(f'{member} has left the server.')
    await ctx.send(f"Goodbye, {member}, we're sad to see you go.")

@bot.event
async def on_message(message):
    file = open(r'C:\Users\Ryan\Documents\scoobert\scoobert-main\scoobert-main\LearnBot\ChatLog.txt', 'a')
    log = f'|>{message.author}<|>{message.created_at}<|>{message.content}<|\n' 
    file.write(log)
    file.close()
        
@bot.event
async def on_message_edit(before, after):
    file = open(r'C:\Users\Ryan\Documents\scoobert\scoobert-main\scoobert-main\LearnBot\ChatLog.txt', 'a')
    log = f'|>{before.author}<|>{before.edited_at}<|\n|>Before: {before.content}<|\n|>After: {after.content}<|\n' 
    file.write(log)
    file.close()

@bot.event
async def on_message_edit(message):
    file = open(r'C:\Users\Ryan\Documents\scoobert\scoobert-main\scoobert-main\LearnBot\ChatLog.txt', 'a')
    log = f'|>{message.author}<|>{message.created_at}<|> *DELETED MESSAGE* {message.content}<|\n' 
    file.write(log)
    file.close()
    

bot.run('NzAxMTU3MTA0Mzc1MDM3OTky.XptZcA.OFddVpptcSovbKH1bWjkhK6Bneo')