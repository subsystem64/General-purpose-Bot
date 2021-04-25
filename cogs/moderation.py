import discord
import json
import re
import string
from discord.ext import commands


separators = string.punctuation+string.digits+string.whitespace
excluded = string.ascii_letters


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #===KICK===

    @commands.command(aliases=["k"])
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member = None,*, reason=None):
        if member == None:
            await ctx.send("Please mention a user to kick")
        if reason == None:
            reason = f"{ctx.author.name}#{ctx.author.discriminator} did not specify a reason"
        x = len(reason)
        if x > 460: # 460 is the character limit of the reason in discord
            await ctx.send('Reason must be less or equal to 460 characters') 
        await member.kick(reason=reason)  
        await ctx.send(f'{member.mention} is kicked from {member.guild.name}.')

    #===BAN===

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member = None, *, reason=None):
        if member == None:
            await ctx.send("Please mention a user to ban")
        if reason == None:
            reason = f"{ctx.author.name}#{ctx.author.discriminator} did not specify a reason"
        x = len(reason)   
        if x > 460: # 460 is the character limit of the reason in discord
            await ctx.send('Reason must be less or equal to 460 characters')
        await ctx.send(f'{member.mention} is banned from {member.guild.name}.')
        await member.ban(reason=reason)

    #===UNBAN===

    @commands.command(aliases=['ub'])
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def unban(self, ctx, member: discord.User = None, *, reason=None): # discord.User allows you to use discord ID/discordname#discriminator (674670744776474644 or Mystery R#6892)
        if reason == None:
            reason = f"{ctx.author.name}#{ctx.author.discriminator} did not specify a reason"
        if member == None:
            await ctx.send("Please give a User ID or Username to unban")
        x = len(reason)   
        if x > 460: # 460 is the character limit of the reason in discord
            await ctx.send('Reason must be less or equal to 460 characters')
        else:
            await ctx.guild.unban(member, reason=reason) # add the response from bot after members are unbanned yourself after this line
            await ctx.send(f'{member} is unbanned from the server.')

    #===PURGE=== 

    @commands.command(aliases=['clear','pg','clr'])
    @commands.has_permissions(manage_messages = True)
    @commands.bot_has_permissions(manage_messages = True)
    async def purge(self, ctx, limit = 3):
        await ctx.channel.purge(limit=limit)

    #===MUTE===

    @commands.command(aliases=['m'])
    @commands.has_permissions(kick_members = True)
    @commands.bot_has_permissions(manage_roles = True)
    async def mute(self, ctx, member:discord.Member):
        try:
            muted_role = discord.utils.get(member.server.roles, name='Muted')
        except:
            await ctx.send("No **Muted** role is found for this server. The role name is case sensitive.")
        await member.add_roles(muted_role)
        await ctx.send(member.mention + "has been muted.")

    #===UNMUTE===

    @commands.command(aliases=['um'])
    @commands.has_permissions(kick_members = True)
    @commands.bot_has_permissions(manage_roles = True)
    async def unmute(self, ctx, member:discord.Member):
        try:
            muted_role = discord.utils.get(member.server.roles, name='Muted')
        except:
            await ctx.send("No **Muted** role is found for this server. The role name is case sensitive.")
        try:
            await member.remove_roles(muted_role)
        except:
            await ctx.send(member.mention + "does not have the Muted role.")

        await ctx.send(member.mention + "has been unmuted.")

    #===MODERATION ERROR HANDLER===

    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(":x:You are missing Manage Messages permission(s) to run this command.")
    
    @kick.error
    async def kick_error(self,ctx, error): 
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(":x:No member was found with the given argument")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(":x:Bot is missing Kick Members permission(s) to run this command.")
        elif isinstance(error,commands.MissingPermissions):
            await ctx.send(":x:You are missing Kick Members permission(s) to run this command.")

    @mute.error
    async def mute_error(self,ctx, error): 
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(":x:No member was found with the given argument")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(":x:Bot is missing Kick Members permission(s) to run this command.")
        elif isinstance(error,commands.MissingPermissions):
            await ctx.send(":x:You are missing Kick Members permission(s) to run this command.")

    @mute.error
    async def unmute_error(self,ctx, error): 
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(":x:No member was found with the given argument")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(":x:Bot is missing Kick Members permission(s) to run this command.")
        elif isinstance(error,commands.MissingPermissions):
            await ctx.send(":x:You are missing Kick Members permission(s) to run this command.")

    @ban.error
    async def ban_error(self,ctx, error): 
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(":x:No member was found with the given argument")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(":x:Bot is missing Ban Members permission(s) to run this command.")
        elif isinstance(error,commands.MissingPermissions):
            await ctx.send(":x:You are missing Ban Members permission(s) to run this command.")
    @unban.error
    async def unban_error(self,ctx, error): 
        if isinstance(error, commands.MemberNotFound):
            await ctx.send(":x:No member was found with the given argument")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(":x:Bot is missing Ban Members permission(s) to run this command.")
        elif isinstance(error,commands.MissingPermissions):
            await ctx.send(":x:You are missing Ban Members permission(s) to run this command.")


    #===ADD BAN WORD===

    @commands.command()
    @commands.has_permissions(administrator = True)
    @commands.bot_has_permissions(manage_messages = True)
    async def addbanword(self, ctx, word):
        with open('./configs/bannedwords.json', 'r+') as f:
            data = json.load(f)
            worddata = data[str(ctx.guild.id)]
            if word.lower() in worddata:
                await ctx.message.delete()
                await ctx.send("Specified word is already banned in this server")
            else:
                worddata.append(word.lower())
                with open('./configs/bannedwords.json','r+') as f:
                    data = json.load(f)
                    data[str(ctx.guild.id)] = worddata
                    f.seek(0)
                    f.write(json.dumps(data))
                    f.truncate()
                await ctx.message.delete()
                await ctx.send(":white_check_mark: Word added to ban list")

    #===REMOVE BAN WORD===

    @commands.command(aliases=['rmbanword'])
    @commands.has_permissions(administrator = True)
    @commands.bot_has_permissions(manage_messages = True)
    async def removebanword(self, ctx, word):
        with open('./configs/bannedwords.json', 'r+') as f:
            data = json.load(f)
            worddata = data[str(ctx.guild.id)]
            if word.lower() in worddata:
                worddata.remove(word.lower())
                with open('./configs/bannedwords.json', 'r+') as f:
                    data = json.load(f)
                    data[str(ctx.guild.id)] = worddata
                    f.seek(0)
                    f.write(json.dumps(data))
                    f.truncate()
                await ctx.message.delete()
                await ctx.send(":white_check_mark: Word removed from ban list")
            else:
                await ctx.send(":x: Specified word is not banned in this server")

    #===BAN WORD PERMISSION ERROR HANDLER===

    @addbanword.error
    async def addbanword_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(":x:You are missing Administrator permission(s) to run this command.")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(":x:Bot is missing Manage Messages permission(s) to run this command.")

    @removebanword.error
    async def removebanword_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(":x:You are missing Administrator permission(s) to run this command.")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(":x:Bot is missing Manage Messages permission(s) to run this command.")

    #===WORD FILTER ON MESSAGE===

    @commands.Cog.listener()
    async def on_message(self, message):
        with open("./configs/bannedwords.json") as f:
            data = json.load(f)
        messageAuthor = message.author
        worddata = data[str(message.guild.id)]
        if worddata != None and (isinstance(message.channel, discord.channel.DMChannel) == False):
            for word in worddata:
                formatted_word = f"[{separators}]*".join(list(word))
                regex_true = re.compile(fr"[^a-zA-Z0-9]*({formatted_word})[^a-zA-Z0-9]*", re.IGNORECASE)
                regex_false = re.compile(fr"([{excluded}]+{word})|({word}[{excluded}]+)", re.IGNORECASE)
                if regex_true.search(message.content) is not None\
                    and regex_false.search(message.content) is None:
                    try:
                            await message.author.send(f"{messageAuthor.mention} Your message was removed as it contained a word banned from {message.guild.name}")
                    except:
                            await message.channel.send(f"{messageAuthor.mention} Your message was removed as it contained a word banned from the server")
                    await message.delete()
                else:
                    return           
                        

def setup(bot):
  bot.add_cog(Moderation(bot))