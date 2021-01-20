# Author: Brendan Garcia
# Date: 12/21/20
# Description: The main cog for the CSE_220_Bot.
# Describes some basic commands for testing purposes and other
# minor functionalities unrelated to wolfram.

import discord
from discord.ext import commands


# defines the class for the MainCog to be constructed upon
class MainCog(commands.Cog):

    # Constructor
    def __init__(self, bot):
        self.bot = bot

    # leaving/joining events

    # sends message when person joins server
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"{member} has joined the server")
        channel = member.guild.system_channel
        await channel.send(f"{member} welcome to {member.guild.name}!")

    # sends message when person leaves, is kicked from, or is banned from a server
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"{member} has left the server")
        channel = member.guild.system_channel
        await channel.send(f"Bye, {member}, you will not be missed!")

    # prints when the bot is booted
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Game("with numbers | !help"))
        print(f"{self.bot.user} has been connected")

    # displays the ping of the bot in ms
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

    # example of how to use embeds
    @commands.command()
    async def embedTest(self, ctx):
        embed = discord.Embed(color=discord.Color.blue(), title="Test Title", description="Testing testing")
        embed.set_author(name="Author",
                         icon_url="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,"
                                  "f_auto/gigs/129979404/original/3ac0f520865d60efadc145def33b24355a2b1df9/turn-your"
                                  "-cat-into-a-sad-cat.jpg")
        embed.set_image(
            url="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,"
                "f_auto/gigs/129979404/original/3ac0f520865d60efadc145def33b24355a2b1df9/turn-your-cat-into-a-sad-cat"
                ".jpg")
        embed.set_thumbnail(
            url="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,"
                "f_auto/gigs/129979404/original/3ac0f520865d60efadc145def33b24355a2b1df9/turn-your-cat-into-a-sad-cat"
                ".jpg")
        embed.add_field(name="ping", value="Has the bot say pong and provide ping in ms", inline=False)
        embed.add_field(name="8ball", value="Does 8ball thing", inline=False)
        embed.set_footer(text="This is the footer")

        await ctx.send(embed=embed)

    # deletes the past <amount> messages in the channel the command was used in
    # default value of amount is 5
    @commands.command()
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)


# setup function to add the cog
def setup(bot):
    bot.add_cog(MainCog(bot))
