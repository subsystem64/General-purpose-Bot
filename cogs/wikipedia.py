import discord
import wikipedia
from discord.ext import commands
from random import randint

current_language = "en"

class Wikipedia(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #===WIKI-SEARCH-COMMAND===

    @commands.command(pass_context=True, aliases=['Wikisearch','ws','WikiSearch', 'Ws'])
    async def wikisearch(self, ctx, *, request = None):

        if request == None:
            author =  ctx.message.author
    
            embed = discord.Embed(
            colour = discord.Colour.red()
            )
            embed.set_author(name = 'Wikipedia Search')
            embed.add_field(name = '&wikisearch', value = 'Returns a list of articles matching search request (&wikisearch <search_query>', inline=False)
            await ctx.send(ctx.message.author.mention, embed = embed)

        else:

            #Load current lang for picture
            global current_language

            #Get user input
            #msg = ctx.message.content.split(" ")
            #request = msg[2:]
            #request = " ".join(request)
            #error = None
            try:

                wikicontent = wikipedia.search(request, results=20, suggestion=False) #Wikipedia search request
                print(wikicontent)
                print(" ".join(wikicontent))

                #If there are no results
                if not wikicontent:
                    wikicontent ="No results returned for '{}'.".format(request)
                    embed = discord.Embed(title="Wikipedia search results:", color=0xe74c3c, description=wikicontent)
                    embed.set_thumbnail(url="https://www.wikipedia.org/static/images/project-logos/{}wiki.png".format(current_language))
                    await ctx.send(embed=embed)

                #If there are do:
                else:
                    embed = discord.Embed(title="Wikipedia search results:", color=0, description="\n".join(wikicontent))
                    embed.set_thumbnail(url="https://www.wikipedia.org/static/images/project-logos/{}wiki.png".format(current_language))
                    await ctx.send(embed=embed)


            #Handle random errors
            except Exception as error:
                error = str(error)
                await ctx.send("An error occurred. Please try again.")
                print(error)

    #===WIKI-COMMAND===

    @commands.command(pass_context=True, aliases=['Wiki','wk'])
    async def wiki(self, ctx, *, request = None):
        if request == None:
            author =  ctx.message.author
    
            embed = discord.Embed(
            colour = discord.Colour.red()
            )
            embed.set_author(name = 'Wikipedia')
            embed.add_field(name = '&wiki', value = 'Shows preview of an article (&wiki <search_query>', inline=False)
            await ctx.send(ctx.message.author.mention, embed = embed)
        else:
            global current_lang

            #Checks if the request is valid
            try:
                pagecontent = wikipedia.page(request)
                pagetext = wikipedia.summary(request, sentences=5)


                #Try to get random image from the article to display.
                #If there are no pictures, it wil set it to the default wkikipedia picture
                try:
                    thumbnail = pagecontent.images[randint(0, len(pagecontent.images))]

                except:
                    thumbnail = "https://www.wikipedia.org/static/images/project-logos/{}wiki.png".format(current_language)


                embed = discord.Embed(title=request, color=0, description=pagetext + "\n\n[Read further]({})".format(pagecontent.url))
                embed.set_thumbnail(url=thumbnail)
                await ctx.send(embed=embed)


            except wikipedia.DisambiguationError:

                NotSpecificRequestErrorMessage = "Search request inspecific"
                embed = discord.Embed(title="Bad request: ", color=0xe74c3c, description=NotSpecificRequestErrorMessage)
                embed.set_thumbnail(url="https://www.wikipedia.org/static/images/project-logos/{}wiki.png".format(current_language))
                await ctx.send(embed=embed)

            except wikipedia.PageError:

                NoResultErrorMessage = "Invalic article name"
                embed = discord.Embed(title="Not found: ", color=0xe74c3c, description=NoResultErrorMessage)
                embed.set_thumbnail(url="https://www.wikipedia.org/static/images/project-logos/{}wiki.png".format(current_language))
                await ctx.send(embed=embed)

            except:
                RandomErrorMessage = "An error occured"
                embed = discord.Embed(title="Error", color=0xe74c3c, description=RandomErrorMessage)
                embed.set_thumbnail(url="https://www.wikipedia.org/static/images/project-logos/{}wiki.png".format(current_language))
                await ctx.send(embed=embed)
                #await ctx(error)

def setup(bot):
  bot.add_cog(Wikipedia(bot))