import discord
from discord import Webhook, AsyncWebhookAdapter
from discord.ext import commands
import aiohttp
import random as r
import datetime


twitter_footer_icon_url = 'https://abs.twimg.com/icons/apple-touch-icon-192x192.png'


async def webhook_tweet(user: discord.User, message: str, attachmentURL=None):
    async with aiohttp.ClientSession() as session:
        url = ''  # WEBHOOK URL HERE
        c = discord.Color.from_rgb(29, 161, 242)
        embed = discord.Embed(description=message, color=c, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text='Twitter', icon_url='')
        embed.add_field(name='Retweets', value=str(r.randint(100, 2500)))
        embed.add_field(name='Likes', value=str(r.randint(100, 2500)))
        embed.set_author(name=f"{user.display_name} (@{user.name}{user.discriminator})", icon_url=str(user.avatar_url))
        if attachmentURL is not None:
            embed.set_image(url=attachmentURL)
        webhook = Webhook.from_url(url, adapter=AsyncWebhookAdapter(session))
        await webhook.send(embed=embed)


class Twitter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['tweet'])
    async def sendtweet(self, ctx, *, message):
        """A function that sends a Discord embed-style tweet on behalf of the invoker using webhooks."""
        if ctx.channel.name == 'twitter':
            if len(message) > 280:
                await ctx.author.send("Error: Tweet too big for Twitter. Get your message below 280 characters and try again.")
            else:
                try:
                    attachment = ctx.message.attachments[0].url
                except IndexError:
                    attachment = None
                await webhook_tweet(ctx.author, message, attachment)
            await ctx.message.delete()