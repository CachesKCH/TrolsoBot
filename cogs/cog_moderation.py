from discord.ext import commands
import discord
import os
import json
with open("E:/Python/Proyectos/TrolsoBot/botconfig.json") as f:
    bot_config = json.load(f)  # Importa el archivo de configuracion a la variable bot_config
    admin_role = bot_config["admin_role"]  # Asigna el rol de moderacion


class Moderacion(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        """Imprime un mensaje a la consola cuando la extension termina de cargar"""
        cog_name = os.path.basename(__file__)
        print(f"Extension {cog_name[:-3]} cargada exitosamente.")

    @commands.command()
    async def pingcog(self, ctx):
        await ctx.send("Pong!")

    @commands.command()
    @commands.has_role(admin_role)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Comando de kickear. recibe argumentos miembro y razon, se guardan en el audit log"""
        await member.kick(reason=reason)

    @commands.command()
    @commands.has_role(admin_role)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Comando de banear. recibe argumentos miembro y razon, se guardan en el audit log"""
        await member.ban(reason=reason)

    @commands.command()
    @commands.has_role(admin_role)
    async def clear(self, ctx, cantidad=0):
        """Comando usado para borrar una cantidad especifica de mensajes"""
        cantidad += 1  # Suma 1 a la cantidad ya que el bot cuenta el comando como (1) mensaje
        if cantidad == 1:  # Si el usuario no especifica (cantidad) el bot devuelve un error y lo borra luego de 5 secs
            await ctx.send("")
        else:
            await ctx.channel.purge(limit=cantidad)  # El bot elimina (cantidad) mensajes


def setup(client):
    client.add_cog(Moderacion(client))
