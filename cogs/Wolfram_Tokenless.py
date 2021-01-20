# Author: Brendan Garcia
# Date: 12/21/20
# Description: The wolfram cog for the CSE_220_Bot.
# Describes the three different ways that I used the wolfram API.

from discord.ext import commands
import wolframalpha
import requests

# app id
TOKENW = 'Insert Token Here'

# creates the wolfram client
client = wolframalpha.Client(TOKENW)


# defines the class for the Wolfram cog to be constructed upon
class Wolfram(commands.Cog):

    # Constructor
    def __init__(self, bot):
        self.bot = bot

    # Takes in one input and returns requested information in an image format. This command's intended purpose is to
    # display mathematical equations graphically, but can technically be used to provide other information.
    # Note: This command displays ALL information.  To only see the first couple results, try the !less command.
    @commands.command()
    async def wolf(self, ctx, *, question):

        # wait message
        await ctx.send(f"Querying for \"{question}\"")

        try:

            # defines the parameters that will dictate the output of the get command
            params = {"input": question, "appid": TOKENW, "output": "json", "format": "image"}

            # define response as the result of the get command query based on the above parameters
            response = requests.get(f"http://api.wolframalpha.com/v2/query?", params=params)

            output = []  # defines a list of outputs that will be displayed to the user

            # for loop through response and extract the title of each pod and the image content of each subpod
            for i in response.json()["queryresult"]["pods"]:
                output.append(i["title"])  # add titles to list
                for j in i["subpods"]:
                    output.append(j["img"]["src"])  # add image urls to list

            # send messages in channel (ctx) with all acquired information
            for i in output:
                await ctx.send(i)

        # If the output does not contain any pods, a KeyError is encountered.  This means, there is no output,
        # thus the input is determined to be invalid.
        except KeyError:
            await ctx.send(f"Question: {question} \nAn error was encountered! Use \"!help\" for more details")

    # Does the same as wolf, but only displays the first two results.
    @commands.command()
    async def less(self, ctx, *, question):

        # wait message
        await ctx.send(f"Querying for \"{question}\"")

        try:

            # defines the parameters that will dictate the output of the get command
            params = {"input": question, "appid": TOKENW, "output": "json", "format": "image",
                      "podindex": "1,2"}

            # define response as the result of the get command query based on the above parameters
            response = requests.get(f"http://api.wolframalpha.com/v2/query?", params=params)

            output = []  # defines a list of outputs that will be displayed to the user

            # for loop through response and extract the title of each pod and the image content of each subpod
            for i in response.json()["queryresult"]["pods"]:
                output.append(i["title"])  # add titles to list
                for j in i["subpods"]:
                    output.append(j["img"]["src"])  # add image urls to list

            # send messages in channel (ctx) with all acquired information
            for i in output:
                await ctx.send(i)

        # If the output does not contain any pods, a KeyError is encountered.  This means, there is no output,
        # thus the input is determined to be invalid.
        except KeyError:
            await ctx.send(f"Question: {question} \nAn error was encountered! Use \"!help\" for more details")


# setup function to add the cog
def setup(bot):
    bot.add_cog(Wolfram(bot))
