# Author: Brendan Garcia
# Date: 12/21/20
# Description: The games cog for the CSE_220_Bot.
# Describes any extra fun functionalities I come up with.

import random
from discord.ext import commands

# defines the class for the Games cog to be constructed upon
class Games(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # randomly selects a response to a question like an 8 ball toy would
    @commands.command(aliases=["8Ball", "8ball", "_8Ball"])
    async def _8ball(self, ctx, *, question):
        # possible responses
        responses = ["As I see it, yes. ",
                     "Ask again later. ",
                     "Better not tell you now. ",
                     "Cannot predict now. ",
                     "Concentrate and ask again. ",
                     "Don’t count on it. ",
                     "It is certain. ",
                     "It is decidedly so. ",
                     "Most likely.  ",
                     "My reply is no. ",
                     "My sources say no. ",
                     "Outlook not so good. ",
                     "Outlook good. ",
                     "Reply hazy, try again. ",
                     "Signs point to yes. ",
                     "Very doubtful. ",
                     "Without a doubt. ",
                     "Yes. ",
                     "Yes – definitely. ",
                     "You may rely on it. "]

        # chooses a random response
        await ctx.send(f"Question: {question} \nAnswer: {random.choice(responses)}")

        # add some more simple games


def setup(bot):
    bot.add_cog(Games(bot))
