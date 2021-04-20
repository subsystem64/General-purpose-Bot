from discord.ext import commands
import discord
from datetime import datetime


class Uptime(commands.Cog):
    """Commands relating to the bot itself."""

    def __init__(self, bot):
        self.bot = bot
        self.start_time = datetime.now()

    @commands.command()
    async def uptime(self, ctx):

        def format_seconds(time_seconds):
            """Formats some number of seconds into a string of format d days, x hours, y minutes, z seconds"""
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

def setup(bot):
  bot.add_cog(Uptime(bot))