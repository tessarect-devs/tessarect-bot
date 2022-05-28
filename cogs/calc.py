import aiohttp
import discord
import requests
from discord.ext import commands


class Calc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Calc cog loaded successfully")

    @commands.command(description="Calculates the given expression")
    async def calc(self, ctx, *, expression):
        if len(expression) > 30:
            await ctx.send("**Too big equation**")
        else:
            st = expression.replace("+", "%2B")
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"https://api.mathjs.org/v4/?expr={st}"
                ) as response:
                    ex = await response.text()
                    if len(ex) > 2000:
                        await ctx.send("Too big result")
                    else:

                        embed = discord.Embed(
                            timestamp=ctx.message.created_at,
                            description="Here is the result ",
                            color=discord.Color.gold()
                        )
                        embed.add_field(
                            name=f"Expression", value=f"```css\n{expression}```", inline=False
                        )                      
                        embed.add_field(
                            name=f"Result", value=f"```css\n{ex}```", inline=False
                        )
                        
                        embed.set_author(
                            name="Calculator"
                            
                        )
                        embed.set_thumbnail(url="https://www.involve.me/assets/images/blog/how-to-create-a-simple-price-calculator-and-capture-more-leads/calculator-L.png",)
                        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Calc(client))