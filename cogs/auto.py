import discord
import json
from discord.ext import commands

class auto(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #===AUTO WELCOME SETTING===

    @commands.command()
    @commands.has_permissions(administrator = True)
    @commands.bot_has_permissions(manage_channels = True)
    async def autowelcome(self, ctx, value = None):
        if value == None:
            await ctx.send('Pass values true/false to enable or disable auto-welcome on member join. This setting is **Disabled** by default')
        else:
            with open('./configs/autowelcome.json', 'r') as f:
                data = json.load(f)
            data[str(ctx.guild.id)] = value.lower()
            with open('./configs/autowelcome.json','w') as f:
                json.dump(data, f, indent = 4)

            await ctx.send(f'Auto-welcome: {value}')

    #===ON MEMBER JOIN===

    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open("./configs/autowelcome.json") as f:
            data = json.load(f)
            trueorfalse = data[str(member.guild.id)]
            if trueorfalse == 'true':
                channel = discord.utils.get(member.guild.text_channels, name='welcome')
                if channel is None:
                    channel = await member.guild.create_text_channel('welcome')
                await channel.send(f'{member} has joined {member.guild.name}.')
                await member.send(f'{member.mention} Enjoy your stay at {member.guild.name}!')
            if trueorfalse == 'false':
                return

        with open("./configs/autorole.json") as f:
            data = json.load(f)
            roles = data[str(member.guild.id)]
            if roles == None:
                return
            for datarole in roles:
                role = discord.utils.get(member.guild.roles, name = datarole)
                await member.add_roles(role)
        
    #===AUTO ROLE ADD===

    @commands.command()
    @commands.has_permissions(manage_roles = True)
    @commands.bot_has_permissions(manage_roles = True)
    async def autoroleadd(self, ctx, value = None):
        if value == None:
            await ctx.send('Please provide a role to add to auto-role listing')
        with open('./configs/autorole.json', 'r+') as f:
            data = json.load(f)
            role = data[str(ctx.guild.id)]
            if value in role:
                await ctx.message.delete()
                await ctx.send("Specified role is already set to be auto-roled")
            if discord.utils.get(ctx.guild.roles, name=value):
                role.append(value)
                with open('./configs/autorole.json','r+') as f:
                    data = json.load(f)
                    data[str(ctx.guild.id)] = role
                    f.seek(0)
                    f.write(json.dumps(data))
                    f.truncate()
                await ctx.send(":white_check_mark: role added")

    #===AUTO ROLE REMOVE===

    @commands.command(aliases=['autorolerm'])
    @commands.has_permissions(manage_roles = True)
    @commands.bot_has_permissions(manage_roles = True)
    async def autoroleremove(self, ctx, value = None):
        if value == None:
            await ctx.send('Please provide a role to remove from auto-role listing')
        with open('./configs/autorole.json', 'r+') as f:
            data = json.load(f)
            role = data[str(ctx.guild.id)]
            if value in role:
                role.remove(value)
                with open('./configs/autorole.json', 'r+') as f:
                    data = json.load(f)
                    data[str(ctx.guild.id)] = role
                    f.seek(0)
                    f.write(json.dumps(data))
                    f.truncate()
                await ctx.send(":white_check_mark: Role removed from auto-role")
            else:
                await ctx.send(":x: Specified role is not is not currently in auto-role listing")


    #===PERMISSION ERROR HANDLER===

    @autoroleadd.error
    async def autoroleadd_error(self,ctx, error): 
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send(":x:Bot is missing Manage Roles permission(s) to run this command.")
        elif isinstance(error,commands.MissingPermissions):
            await ctx.send(":x:You are missing Manage Roles permission(s) to run this command.")

    @autoroleremove.error
    async def autoroleremove_error(self,ctx, error): 
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send(":x:Bot is missing Manage Roles permission(s) to run this command.")
        elif isinstance(error,commands.MissingPermissions):
            await ctx.send(":x:You are missing Manage Roles permission(s) to run this command.")

    @autowelcome.error
    async def autowelcome_error(self,ctx, error): 
        if isinstance(error, commands.BotMissingPermissions):
            await ctx.send(":x:Bot is missing Manage Channels permission(s) to run this command.")
        elif isinstance(error,commands.MissingPermissions):
            await ctx.send(":x:You are missing Administrator permission(s) to run this command.")
            
def setup(bot):
    bot.add_cog(auto(bot))