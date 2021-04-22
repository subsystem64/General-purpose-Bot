import discord
import urllib.parse, urllib.request, re
import asyncio
from discord.ext import commands

class YouTube(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    #===YOUTUBE SEARCH===

    @commands.command(aliases=['Youtube','yt','YouTube', 'Yt'])
    async def youtube(self, ctx, *, search = None):
        
        if search == None:
 
            embed = discord.Embed(
            colour = discord.Colour.red()
            )
            embed.set_author(name = 'YouTube Search')
            embed.add_field(name = '&youtube', value = 'Starts a YouTube search query (&youtube <search_query>). type **next** or **prev** to scroll through results, **exit** to exit search', inline=False)
            await ctx.send(ctx.message.author.mention, embed = embed)
        else:
            query_string = urllib.parse.urlencode({'search_query': search})
            html_content = urllib.request.urlopen('http://www.youtube.com/results?' + query_string)
            search_content= html_content.read().decode()
            search_results = re.findall(r'\/watch\?v=\w+', search_content)
            prev_msg = await ctx.send('https://www.youtube.com' + search_results[0])
            await ctx.send('type **next** or **prev** to scroll through results, **exit** to exit search')
            count = 0
            while True:
                def check(msg):
                    return msg.content in ('next', 'Next', 'exit','Exit','Prev','prev')

                try:
                    msg = await self.bot.wait_for('message', check=check, timeout = 90.0)
                    if msg.content == 'next':
                        count += 1
                        await msg.delete(delay = 0)
                        await prev_msg.edit(content = 'https://www.youtube.com' + search_results[count])
                    elif msg.content == 'Next':
                        count += 1
                        await msg.delete(delay = 0)
                        await prev_msg.edit(content = 'https://www.youtube.com' + search_results[count])
                    elif msg.content == 'Prev':
                        if count > 0:
                            count -= 1
                            await msg.delete(delay = 0)
                            await prev_msg.edit(content = 'https://www.youtube.com' + search_results[count])
                        else:
                            await ctx.send("No previous search results.")
                    elif msg.content == 'prev':
                        if count > 0:
                            count -= 1
                            await msg.delete(delay = 0)
                            await prev_msg.edit(content = 'https://www.youtube.com' + search_results[count])
                        else:
                            await ctx.send("No previous search results.")
                    elif msg.content == 'exit':
                        await msg.add_reaction("✅")
                        break
                    elif msg.content == 'Exit':
                        await msg.add_reaction("✅")
                        break
                except asyncio.TimeoutError:
                    await ctx.send(':x: **Timed Out**')
                    break
            await ctx.send('**Search Quitted**')
            
def setup(bot):
  bot.add_cog(YouTube(bot))