# -*- coding: utf-8 -*-

import discord
from discord.ext import commands, tasks
import json
import secrets
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
bot = commands.Bot(command_prefix="!", case_insensitive=False)
statuses = open('statusy.txt', 'r', encoding='utf-8')
all_statuses = statuses.readlines()
statuses.close()


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f'Loaded {filename[:-3]}')


@bot.event
async def on_ready():
    change_status.start()
    print('Brzydal Ropuch przejmuje zbrodniczy reżim')


@tasks.loop(seconds=60)
async def change_status():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(secrets.choice(all_statuses)))


@bot.command()
@commands.has_permissions(administrator=True)
async def cogs(ctx):
    """Shows available cogs"""
    cgs = 'Available cogs:\n'
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            cgs = cgs + f'{file[:-3]}\n'
    await ctx.send(cgs)
    print(cgs)


@bot.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    """(cog_name)"""
    bot.load_extension(f'cogs.{extension}')
    print(f'{extension} loaded successfully')


@bot.command()
@commands.has_permissions(administrator=True)
async def reload(ctx, extension):
    """(cog_name)"""
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    print(f'{extension} reloaded successfully')


@bot.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    """(cog_name)"""
    bot.unload_extension(f'cogs.{extension}')
    print(f'{extension} unloaded successfully')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Nie znalazłem takiej komendy, lepiej zapytaj Kurową')


@bot.command()
@commands.has_permissions(administrator=True)
async def ping(ctx):
    await ctx.send(f'Mam {round(bot.latency * 1000)}ms opóźnienia...')
    print(f'Latency: {round(bot.latency * 1000)}ms')

bot.run(TOKEN)
