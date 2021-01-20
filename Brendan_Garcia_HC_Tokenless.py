# Author: Brendan Garcia
# Date: 12/21/20
# Description: The main file for the CSE_220_Bot.
# Describes the basis for the bot to be constructed using cog commands.

import discord
import os
from discord.ext import commands

# discord token
TOKEND = "Insert Token Here"

# initializes intents, allowing for events to be detected properly
intents = discord.Intents.default()
intents.members = True

# initializes the discord bot as well as sets the command prefix
bot = commands.Bot(command_prefix='!', intents=intents)

# remove default help command
bot.remove_command("help")


# cogs

# command used to load the specified cog
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"{extension} has been loaded")


# command used to unload the specified cog
@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"{extension} has been unloaded")


# command used to unload the specified cog
@bot.command()
async def reload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"{extension} has been reloaded")


# accesses all the cogs in "CSE_220_Bot/cogs" and loads them with their respective name (removing the ".py")
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(TOKEND)
