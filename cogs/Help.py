# Author: Brendan Garcia
# Date: 12/21/20
# Description: The help cog for the CSE_220_Bot.  Describes the help command.

import discord
from discord.ext import commands


# defines the class for the Help cog to be constructed upon
class Help(commands.Cog):

    # Constructor
    def __init__(self, bot):
        self.bot = bot

    # defines the help command; direct messages the person who requested the help menu
    @commands.command(pass_context=True)
    async def help(self, ctx):
        author = ctx.message.author

        # defines the embed that is sent to the user
        embed = discord.Embed(color=discord.Color.orange())

        embed.set_author(name="Bot Prefix = !")
        embed.set_thumbnail(url="https://images-na.ssl-images-amazon.com/images/I/41II4YzkFxL.png")

        # basic stuff including Help and MainCog
        embed.add_field(name="help :smiley:", value="provides the help menu you are seeing right now.  ", inline=False)
        embed.add_field(name="embedTest :card_index:", value="Outputs an example of an embed block.  ", inline=False)
        embed.add_field(name="clear :soap:",
                        value="Takes one input (number of lines to clear) and removes the specified number of lines "
                              "from the current channel.  If no number is specified, 5 lines will be removed.  ",
                        inline=False)
        embed.add_field(name="load :floppy_disk:", value="Takes one input (the name of a new cog) and loads it.  ",
                        inline=False)
        embed.add_field(name="unload :headstone:",
                        value="Takes one input (the name of an existing cog) and unloads it.  ", inline=False)
        embed.add_field(name="reload :arrows_counterclockwise:",
                        value="Takes one input (the name of an existing cog) and unloads and loads it again.  ",
                        inline=False)
        embed.add_field(name="ping :ping_pong:", value="Provides bot ping in ms.  ", inline=False)

        # games
        embed.add_field(name="8ball :8ball:",
                        value="Takes one input (a yes or no question) and randomly selects a response like an 8 ball "
                              "toy would.  ", inline=False)

        # Wolfram
        embed.add_field(name="wolf :wolf:",
                        value="Takes in one input and returns requested information in an image format.  "
                              "This command's intended purpose is to display mathematical equations graphically, "
                              "but can technically be used to provide other information such as dates, people, "
                              "definitions, etc.  If an error is encountered, first check your spelling.  If this is "
                              "not the issue, it is likely your question is simply not valid for the wolfram image "
                              "format.  \n\nNote: This command displays ALL information.  To only see the first couple "
                              "results, try the !less command.",
                        inline=False)
        embed.add_field(name="less :dog:", value="Does the same as wolf, but only displays the first two results.  ",
                        inline=False)

        await author.send(embed=embed)  # send embed


# setup function to add the cog
def setup(bot):
    bot.add_cog(Help(bot))
