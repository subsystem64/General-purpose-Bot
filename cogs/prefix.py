import json
from discord.ext import commands

class SetPrefix(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    #===SET CUSTOME PREFIX===

    @commands.command(aliases=['Setprefix','sp','prefix'])
    async def setprefix(self, ctx, prefix = None):
        if prefix == None:
            await ctx.send('Change the bot prefix for current server (&setprefix <custom_prefix>).')
        else:
            with open('./configs/prefixes.json', 'r') as f:
                prefixes = json.load(f)
            prefixes[str(ctx.guild.id)] = prefix
            with open('./configs/prefixes.json','w') as f:
                json.dump(prefixes, f, indent = 4)

            await ctx.send(f'The prefix is now: {prefix}')

    #===CURRENT PREFIX===

    @commands.command(aliases=['currentprefix','Getprefix'])
    async def getprefix(self, ctx):
        with open("./configs/prefixes.json", "r") as f:
            data = json.loads(f.read())
            guildID = str(ctx.guild.id)
            prefix = data[guildID]
            await ctx.send(f"The current server prefix is: {prefix}")
            
  


def setup(bot):
  bot.add_cog(SetPrefix(bot))


