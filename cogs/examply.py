import discord
import os
from discord.ext import commands


class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        cog_name = os.path.basename(__file__)
        print(f"Extension {cog_name[:-3]} cargada exitosamente.")

    @commands.command()
    async def pingcog(self, ctx):
        await ctx.send("Pong!")


def setup(client):
    client.add_cog(Example(client))
