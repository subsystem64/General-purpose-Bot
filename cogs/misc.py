import discord
import random
from discord.ext import commands
from random import randint


class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #===WELCOME-COMMAND===

    @commands.command(pass_context=True, aliases=['Welcome'])
    async def welcome(self, ctx):
        await ctx.send('Welcome!')

    #===HI-COMMAND===

    @commands.command(pass_context=True, aliases=['Hi'])
    async def hi(self, ctx):
        await ctx.send('Hi :]')

    #===ASK-QUESTION-COMMAND===
        
    @commands.command(pass_context=True, aliases=['Ask'])
    async def ask(self, ctx, question = None):
        variable = [
            "yes",
            "no",
            "mayybee"]
        if question == None:
            await ctx.send("What question are you asking?")
        else:
            await ctx.send("{}".format(random.choice(variable))) 
        
    @commands.command(pass_context=True, aliases=['coinflip','Coinflip','Flipacoin'])
    async def flipacoin(self, ctx):
        variable = [
            "head",
            "tail"]
        await ctx.send("{}".format(random.choice(variable))) 

    #===ROLL-DICE-COMMAND===

    @commands.command(pass_context=True, aliases=['Roll'])
    async def roll(self, ctx, roll : str = None):
        """Rolls a dice using #d# format.
        e.g .r 3d6"""
        
        resultTotal = 0
        resultString = ''
        try:
            try: 
                numDice = roll.split('d')[0]
                diceVal = roll.split('d')[1]
            except Exception as e:
                print(e)
                await ctx.send("Format has to be in #d# %s." % ctx.message.author.name)
                return

            if int(numDice) > 500:
                await ctx.send("I cant roll that many dice %s." % ctx.message.author.name)
                return

            #await delete_messages(ctx.message, ctx.message.author)
            
            await ctx.send("Rolling %s d%s for %s" % (numDice, diceVal, ctx.message.author.name))
            rolls, limit = map(int, roll.split('d'))

            for r in range(rolls):
                number = random.randint(1, limit)
                resultTotal = resultTotal + number
                
                if resultString == '':
                    resultString += str(number)
                else:
                    resultString += ', ' + str(number)
            
            if numDice == '1':
                await ctx.send(ctx.message.author.mention + "  :game_die:\n**Result:** " + resultString)
            else:
                await ctx.send(ctx.message.author.mention + "  :game_die:\n**Result:** " + resultString + "\n**Total:** " + str(resultTotal))

        except Exception as e:
            print(e)
            return

def setup(bot):
  bot.add_cog(Misc(bot))