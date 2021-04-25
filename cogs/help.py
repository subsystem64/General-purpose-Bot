import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #===MAIN HELP MENU===

    @commands.group(invoke_without_command = True, aliases=['Help'])
    async def help(self, ctx):
        author =  ctx.message.author

        embed = discord.Embed(
        title="Help :question:", 
        description="Available commands for system86. Do **&help <command>** for more information on a command", 
        colour = discord.Colour.purple()
        )
        embed.set_thumbnail(url = ctx.guild.me.avatar_url)
        embed.add_field(name = 'Utilities (Misc.) :tools:', value = 'flipacoin, roll, ask, welcome, hi, getprefix ', inline=True)
        embed.add_field(name = 'Music :notes:', value = 'join, leave, play, pause, resume, volume, skip, nowplaying, queue, clearqueue, jumpqueue', inline=True)
        embed.add_field(name = 'Moderation', value = 'kick, ban, unban, purge, mute, unmute', inline=True)
        embed.add_field(name = 'Search APIs :mag:', value = 'youtube, wikisearch, wiki', inline=True)
        embed.add_field(name = 'Translate :globe_with_meridians:', value = 'translate, langlist, detectlang', inline=True)
        embed.add_field(name = 'Settings :gear:', value = 'setprefix, autowelcome, autoroleadd, autoroleremove, addbanword, removebanword', inline=True)
        embed.add_field(name = 'Debug :lady_beetle:', value = 'load, unload, reload, ping, botstats, shutdown, uptime', inline=True)

        await ctx.send(author.mention, embed = embed) 

    #===SUB HELP MENUS===

    #utility commands

    @help.command()
    async def flipacoin(self, ctx):
        embed = discord.Embed(
        title="flipacoin :coin:", 
        description="Flips a coin", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&flipacoin', inline=False)
        embed.add_field(name = '**Aliases**', value = 'coinflip', inline=True)
        embed.add_field(name = '**Required Permissions**', value = 'Send Messages', inline = False)
        await ctx.send(embed = embed)

    @help.command()
    async def roll(self, ctx):
        embed = discord.Embed(
        title="roll :game_die:", 
        description="Rolls a dice using #d# format", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&roll <dice_number>d<dice_size>', inline=False)
        embed.add_field(name = '**Aliases**', value = 'Roll', inline=True)
        embed.add_field(name = '**Required Permissions**', value = 'Send Messages', inline = False)
        await ctx.send(embed = embed)

    @help.command()
    async def ask(self, ctx):
        embed = discord.Embed(
        title="ask :question:", 
        description="Ask me a question!", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&ask <question>', inline=False)
        embed.add_field(name = '**Aliases**', value = 'Ask', inline=True)
        embed.add_field(name = '**Required Permissions**', value = 'Send Messages', inline = False)
        await ctx.send(embed = embed)

    @help.command()
    async def welcome(self, ctx):
        embed = discord.Embed(
        title="welcome", 
        description="Greeting", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&welcome', inline=False)
        embed.add_field(name = '**Aliases**', value = 'Welcome', inline=True)
        embed.add_field(name = '**Required Permissions**', value = 'Send Messages', inline = False)
        await ctx.send(embed = embed)

    @help.command()
    async def hi(self, ctx):
        embed = discord.Embed(
        title="hi", 
        description="Say hi to the bot", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&hi', inline=False)
        embed.add_field(name = '**Aliases**', value = 'Hi', inline=True)
        embed.add_field(name = '**Required Permissions**', value = 'Send Messages', inline = False)
        await ctx.send(embed = embed)

    @help.command()
    async def getprefix(self, ctx):
        embed = discord.Embed(
        title="getprefix", 
        description="Returns current bot prefix for the server", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&getprefix', inline=False)
        embed.add_field(name = '**Aliases**', value = 'currentprefix', inline=True)
        embed.add_field(name = '**Required Permissions**', value = 'Send Messages', inline = False)
        await ctx.send(embed = embed)

    #moderation commands

    @help.command()
    async def kick(self, ctx):
        embed = discord.Embed(
        title="kick", 
        description="Kicks a user from the server", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&kick <@user> <reason>', inline=False)
        embed.add_field(name = '**Aliases**', value = 'k', inline=True)
        embed.add_field(name = '**Required Permissions**', value = 'Send Messages, Kick Members', inline = False)
        await ctx.send(embed = embed)

    @help.command()
    async def ban(self, ctx):
        embed = discord.Embed(
        title="ban", 
        description="Bans a user from the server", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&ban <@user> <reason>', inline=False)
        embed.add_field(name = '**Required Permissions**', value = 'Send Messages, Ban Members', inline = False)
        await ctx.send(embed = embed)

    @help.command()
    async def unban(self, ctx):
        embed = discord.Embed(
        title="unban", 
        description="Unbans a user from the server", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&unban <user_ID/username> <reason>', inline=False)
        embed.add_field(name = '**Aliases**', value = 'ub', inline=True)
        embed.add_field(name = '**Required Permissions**', value = 'Send Messages, Ban Members', inline = False)
        await ctx.send(embed = embed)

    @help.command()
    async def mute(self, ctx):
        embed = discord.Embed(
        title="mute", 
        description="Mutes a user through Mute role", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&mute <user_ID/username>', inline=False)
        embed.add_field(name = '**Aliases**', value = 'm', inline=True)
        embed.add_field(name = '**Required Permissions**', value = 'Send Messages, Manage Roles', inline = False)

        await ctx.send(embed = embed)

    @help.command()
    async def unmute(self, ctx):
        embed = discord.Embed(
        title="unmute", 
        description="Unmutes a muted user", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&unmute <user_ID/username>', inline=False)
        embed.add_field(name = '**Aliases**', value = 'um', inline=True)
        embed.add_field(name = '**Required Permissions**', value = 'Send Messages, Manage Roles', inline = False)

        await ctx.send(embed = embed)

    @help.command()
    async def purge(self, ctx):
        embed = discord.Embed(
        title="purge", 
        description="Deletes the most recent specified amount of messages in the channel.", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&purge <amount>', inline=False)
        embed.add_field(name = '**Aliases**', value = 'clear, pg, clr', inline=True)
        embed.add_field(name = '**Required Permissions**', value = 'Send Messages, Manage Messages', inline = False)
        await ctx.send(embed = embed)

    #search api commands

    @help.command()
    async def youtube(self, ctx):
        embed = discord.Embed(
        title="youtube", 
        description="Performs a YouTube search query. Type **next** or **prev** to scroll through results, **exit** to exit search", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&youtube <search_query>', inline=False)
        embed.add_field(name = '**Aliases**', value = 'yt', inline=True)
        embed.add_field(name = '**Required Permissions**', value = 'Send Messages, Read Messages', inline = False)
        await ctx.send(embed = embed)

    @help.command()
    async def wikisearch(self, ctx):
        embed = discord.Embed(
        title="wikisearch :books:", 
        description="Returns a list of articles matching search request", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&wikisearch <search_query>', inline=False)
        embed.add_field(name = '**Aliases**', value = 'ws', inline=True)
        embed.add_field(name = '**Required Permissions**', value = 'Send Messages', inline = False)
        await ctx.send(embed = embed)

    @help.command()
    async def wiki(self, ctx):
        embed = discord.Embed(
        title="wiki :books:", 
        description="Shows preview of an article", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&wiki <article_title>', inline=False)
        embed.add_field(name = '**Aliases**', value = 'wk', inline=True)
        embed.add_field(name = '**Required Permissions**', value = 'Send Messages', inline = False)
        await ctx.send(embed = embed)

#settings commands

    @help.command()
    async def setprefix(self, ctx):
        embed = discord.Embed(
        title="setprefix", 
        description="Change the bot prefix for current server", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&setprefix <custom_prefix>', inline=False)
        embed.add_field(name = '**Aliases**', value = 'sp, prefix', inline=True)
        embed.add_field(name = '**Required Permissions**', value = 'Send Messages', inline = False)
        await ctx.send(embed = embed)

    @help.command()
    async def autowelcome(self, ctx):
        embed = discord.Embed(
        title="autowelcome :wave:", 
        description="Turns auto-welcome On/Off. By default it is set to **false**", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&autowelcome <boolean_value>', inline=False)
        embed.add_field(name = '**Required Permissions**', value = 'Send Messages, Manage Channels', inline = False)
        await ctx.send(embed = embed)

    @help.command()
    async def autoroleadd(self, ctx):
        embed = discord.Embed(
        title="autoroleadd", 
        description="Adds a role to be given on member join event", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&autoroleadd <role_name>', inline=False)
        embed.add_field(name = '**Required Permissions**', value = 'Manage Roles', inline = False)
        await ctx.send(embed = embed)

    @help.command()
    async def autoroleremove(self, ctx):
        embed = discord.Embed(
        title="autoroleremove", 
        description="Removes a role from auto-role listing", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&autoroleremove <role_name>', inline=False)
        embed.add_field(name = '**Aliases**', value = 'autorolerm', inline=True)
        embed.add_field(name = '**Required Permissions**', value = 'Manage Roles', inline = False)
        await ctx.send(embed = embed)

    @help.command()
    async def addbanword(self, ctx):
        embed = discord.Embed(
        title="addbanword", 
        description="Adds a word to ban list. Message containing the word will be auto-deleted.", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&addbanword <word>', inline=False)
        embed.add_field(name = '**Required Permissions**', value = 'Send Messages, Manage Messages', inline = False)
        await ctx.send(embed = embed)

    @help.command()
    async def removebanword(self, ctx):
        embed = discord.Embed(
        title="removebanword", 
        description="Removes a word from the ban list.", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&removebanword <word>', inline=False)
        embed.add_field(name = '**Aliases**', value = 'rmbanword', inline=True)
        embed.add_field(name = '**Required Permissions**', value = 'Send Messages, Manage Messages', inline = False)
        await ctx.send(embed = embed)

    #debug commands

    @help.command()
    async def load(self, ctx):
        embed = discord.Embed(
        title="load", 
        description="loads a cog", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&load <extension_name>', inline=False)
        embed.add_field(name = '**Required Permissions**', value = 'Send Messages', inline = False)
        await ctx.send(embed = embed)

    @help.command()
    async def unload(self, ctx):
        embed = discord.Embed(
        title="unload", 
        description="unloads a cog", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&unload <extension_name>', inline=False)
        embed.add_field(name = '**Required Permissions**', value = 'Send Messages', inline = False)
        await ctx.send(embed = embed)

    @help.command()
    async def reload(self, ctx):
        embed = discord.Embed(
        title="reload", 
        description="reloads a cog", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&reload <extension_name>', inline=False)
        embed.add_field(name = '**Required Permissions**', value = 'Send Messages', inline = False)
        await ctx.send(embed = embed)

    @help.command()
    async def botstats(self, ctx):
        embed = discord.Embed(
        title="botstats :bar_chart:", 
        description="Shows current server statistics", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&botstats', inline=False)
        embed.add_field(name = '**Required Permissions**', value = 'Send Messages', inline = False)
        await ctx.send(embed = embed)

    @help.command()
    async def ping(self, ctx):
        embed = discord.Embed(
        title="ping", 
        description="Returns latency and response time", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&ping', inline=False)
        embed.add_field(name = '**Required Permissions**', value = 'Send Messages', inline = False)
        await ctx.send(embed = embed)

    @help.command()
    async def shutdown(self, ctx):
        embed = discord.Embed(
        title="shutdown", 
        description="Logs off", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&shutdown', inline=False)
        embed.add_field(name = '**Required Permissions**', value = 'Send Messages', inline = False)
        await ctx.send(embed = embed)

    @help.command()
    async def uptime(self, ctx):
        embed = discord.Embed(
        title="uptime :hourglass:", 
        description="Returns bot uptime", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&uptime', inline=False)
        embed.add_field(name = '**Required Permissions**', value = 'Send Messages', inline = False)
        await ctx.send(embed = embed)

    #music commands

    @help.command()
    async def join(self, ctx):
        embed = discord.Embed(
        title="join", 
        description="Bot joins current user voice channel", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&join', inline=False)
        embed.add_field(name = '**Required Permissions**', value = 'Connect', inline = False)
        await ctx.send(embed = embed)

    @help.command()
    async def leave(self, ctx):
        embed = discord.Embed(
        title="leave", 
        description="Bot leaves current user voice channel", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&leave', inline=False)
        embed.add_field(name = '**Aliases**', value = 'disconnect', inline=True)
        embed.add_field(name = '**Required Permissions**', value = 'Connect', inline = False)
        await ctx.send(embed = embed)

    @help.command()
    async def play(self, ctx):
        embed = discord.Embed(
        title="play :arrow_forward:", 
        description="Plays a youtube video given url or first result from query", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&play <video_url/query>', inline=False)
        embed.add_field(name = '**Required Permissions**', value = 'Speak, Connect, Add Reactions', inline = False)
        await ctx.send(embed = embed)

    @help.command()
    async def pause(self, ctx):
        embed = discord.Embed(
        title="pause :pause_button:", 
        description="Pauses current track", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&pause', inline=False)
        embed.add_field(name = '**Aliases**', value = 'p', inline=True)
        embed.add_field(name = '**Required Permissions**', value = 'Speak, Connect, Add Reactions', inline = False)
        await ctx.send(embed = embed)

    @help.command()
    async def resume(self, ctx):
        embed = discord.Embed(
        title="resume :play_pause:", 
        description="Resumes paused track", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&resume', inline=False)
        embed.add_field(name = '**Required Permissions**', value = 'Speak, Connect, Add Reactions', inline = False)
        await ctx.send(embed = embed)
    
    @help.command()
    async def volume(self, ctx):
        embed = discord.Embed(
        title="volume :speaker:", 
        description="Change the volume of currently playing audio (values 0-250)", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&volume <value>', inline=False)
        embed.add_field(name = '**Aliases**', value = 'v', inline=True)
        embed.add_field(name = '**Required Permissions**', value = 'Speak, Connect, Add Reactions', inline = False)
        await ctx.send(embed = embed)
    
    @help.command()
    async def skip(self, ctx):
        embed = discord.Embed(
        title="skip :fast_forward:", 
        description="Skips or votes to skip the current track.", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&skip', inline=False)
        embed.add_field(name = '**Required Permissions**', value = 'Speak, Connect, Add Reactions', inline = False)
        await ctx.send(embed = embed)

    @help.command()
    async def nowplaying(self, ctx):
        embed = discord.Embed(
        title="nowplaying :musical_note:", 
        description="Displays current track information", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&nowplaying', inline=False)
        embed.add_field(name = '**Aliases**', value = 'np', inline=True)
        embed.add_field(name = '**Required Permissions**', value = 'Speak, Connect, Add Reactions', inline = False)
        await ctx.send(embed = embed)

    @help.command()
    async def queue(self, ctx):
        embed = discord.Embed(
        title="queue", 
        description="Returns current queue", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&queue', inline=False)
        embed.add_field(name = '**Aliases**', value = 'q,playlist', inline=True)
        embed.add_field(name = '**Required Permissions**', value = 'Speak, Connect, Add Reactions', inline = False)
        await ctx.send(embed = embed)

    @help.command()
    async def clearqueue(self, ctx):
        embed = discord.Embed(
        title="clearqueue", 
        description="Clears the play queue (Requires Administrator Privileges", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&clearqueue', inline=False)
        embed.add_field(name = '**Aliases**', value = 'q,playlist', inline=True)
        embed.add_field(name = '**Required Permissions**', value = 'Speak, Connect, Add Reactions', inline = False)
        await ctx.send(embed = embed)

    @help.command()
    async def jumpqueue(self, ctx):
        embed = discord.Embed(
        title="jumpqueue", 
        description="Moves song at an index to new index in queue", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&jumpqueue <index> <new_index>', inline=False)
        embed.add_field(name = '**Aliases**', value = 'jq', inline=True)
        embed.add_field(name = '**Required Permissions**', value = 'Speak, Connect, Add Reactions', inline = False)
        await ctx.send(embed = embed)

    #translate commands

    @help.command()
    async def translate(self, ctx):
        embed = discord.Embed(
        title="translate", 
        description="Translates a phrase to a specified language", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = 'tr [words] <from lang_code (optional)> <to lang_code>', inline=False)
        embed.add_field(name = '**Aliases**', value = 'tr', inline=True)
        embed.add_field(name = '**Required Permissions**', value = 'Send Messages', inline = False)
        await ctx.send(embed = embed)
    
    @help.command()
    async def langlist(self, ctx):
        embed = discord.Embed(
        title="langlist", 
        description="Returns a list of available languages and respective codes from Google Translate API", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&langlist', inline=False)
        embed.add_field(name = '**Required Permissions**', value = 'Send Messages', inline = False)
        await ctx.send(embed = embed)

    @help.command()
    async def detectlang(self, ctx):
        embed = discord.Embed(
        title="detectlang", 
        description="Returns detected language and certainty of detection", 
        colour = discord.Colour.gold()
        )
        embed.add_field(name = '**Syntax**', value = '&detectlang <phrase>', inline=False)
        embed.add_field(name = '**Required Permissions**', value = 'Send Messages', inline = False)
        await ctx.send(embed = embed)

    

def setup(bot):
  bot.add_cog(Help(bot))