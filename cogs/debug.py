import discord
from discord.ext import commands
from datetime import datetime, timedelta
from platform import python_version
from time import time
from psutil import Process, virtual_memory
from discord import __version__ as discord_version


class debug(commands.Cog):
    """Commands relating to the bot itself."""

    def __init__(self, bot):
        self.bot = bot
        self.start_time = datetime.now()

    @commands.command()
    async def uptime(self, ctx):
        
        def format_seconds(time_seconds):
            #Formats some number of seconds into a string of format d days, x hours, y minutes, z seconds
            seconds = time_seconds
            hours = 0
            minutes = 0
            days = 0
            while seconds >= 60:
                if seconds >= 60 * 60 * 24:
                    seconds -= 60 * 60 * 24
                    days += 1
                elif seconds >= 60 * 60:
                    seconds -= 60 * 60
                    hours += 1
                elif seconds >= 60:
                    seconds -= 60
                    minutes += 1

            return f"{days}d {hours}h {minutes}m {seconds}s"

        """Tells how long the bot has been running."""
        uptime_seconds = round(
            (datetime.now() - self.start_time).total_seconds())
        await ctx.send(f"Current Uptime: {format_seconds(uptime_seconds)}"
                       )

    #===PING===

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(title = "Pong!", colour = discord.Colour.red(), timestamp=datetime.utcnow())
        embed.add_field(name = ":hourglass: API Latency:", value = f"{self.bot.latency*1000:,.0f} ms", inline = False)

        new_embed = discord.Embed(title = "Pong!", colour = discord.Colour.red(), timestamp=datetime.utcnow())
        new_embed.add_field(name = ":hourglass: API Latency:", value = f"{self.bot.latency*1000:,.0f} ms", inline = False)

        start = time()
        message = await ctx.send(embed=embed)
        end = time()
        new_embed.add_field(name = ":stopwatch: Response Time:", value = f"{(end-start)*1000:,.0f} ms", inline = False)
        await message.edit(embed = new_embed)

    #===BOT STATISTICS===

    @commands.command()
    @commands.is_owner()
    async def botstats(self, ctx):

        embed = discord.Embed(title = "Statistics", colour = discord.Colour.red(), thumbnail=self.bot.user.avatar_url, timestamp=datetime.utcnow())

        proc = Process()
        with proc.oneshot():
            uptime = timedelta(seconds=time()-proc.create_time())
            cpu_time = timedelta(seconds=(cpu := proc.cpu_times()).system + cpu.user)
            mem_total = virtual_memory().total / (1024**2)
            mem_of_total = proc.memory_percent()
            mem_usage = mem_total * (mem_of_total / 100)

        embed.add_field(name = "Python version", value = python_version(), inline = True),
        embed.add_field(name = "discord.py version", value = discord_version, inline = True),
        embed.add_field(name = "Uptime", value = uptime, inline = True),
        embed.add_field(name = "CPU time", value = cpu_time, inline = True),
        embed.add_field(name = "Memory usage", value = f"{mem_usage:,.3f} / {mem_total:,.0f} MiB ({mem_of_total:.0f}%)", inline = True),
        #embed.add_field(name = "Users", value = f"{ctx.guild.member_count:,}", inline =True)

        await ctx.send(embed=embed)
    
    #===SHUT DOWN===

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        await ctx.send("Shutting down...")
        await ctx.bot.logout()

    #===PERMISSION ERROR HANDLER===

    @botstats.error
    async def botstats_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send(":x: Insufficient permissions. You do not own this bot")
    
    @shutdown.error
    async def shutdown_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send(":x: Insufficient permissions. You do not own this bot")
    
def setup(bot):
    bot.add_cog(debug(bot))