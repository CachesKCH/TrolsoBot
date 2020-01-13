from secret import token, secret_server_id
import random
import os
import asyncio
import discord
from discord.ext import commands

p_var_server_id = secret_server_id  # Guarda el server ID secreto en una variable publica que puede ser reusada
admin_role = "TrolsoBotUSR"  # Variable donde se guarda el rol de moderacion (mas adelante va a estar en una BDD)
client = commands.Bot(command_prefix="tr:", case_insensitive=True)  # Define el prefijo del bot


@client.event
async def on_ready():
    """Imprime a la terminal el momento en que el bot esta listo para recibir comandos"""
    print("El bot esta listo.")


@client.command()
@commands.has_role(admin_role)
async def load(ctx, extension):
    """Comando que activa una extension especifica por nombre de archivo"""
    await ctx.send(f"Activando extension {extension}...")
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"Extension {extension} activada exitosamente en {round(client.latency * 1000)} ms.")


@client.command()
@commands.has_role(admin_role)
async def unload(ctx, extension):
    """Comando que desactiva una extension especifica por nombre de archivo"""
    await ctx.send(f"Desactivando extension {extension}...")
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"Extension {extension} desactivada exitosamente en {round(client.latency * 1000)} ms.")


@client.command()
@commands.has_role(admin_role)
async def kick(ctx, member: discord.Member, *, reason=None):
    """Comando de kickear. recibe argumentos miembro y razon, se guardan en el audit log"""
    await member.kick(reason=reason)


@client.command()
@commands.has_role(admin_role)
async def ban(ctx, member: discord.Member, *, reason=None):
    """Comando de banear. recibe argumentos miembro y razon, se guardan en el audit log"""
    await member.kick(reason=reason)


@client.command()
@commands.has_role(admin_role)
async def clear(ctx, cantidad=0):
    """Comando usado para borrar una cantidad especifica de mensajes"""
    cantidad += 1  # Suma 1 a la cantidad ya que el bot cuenta el comando como (1) mensaje
    if cantidad == 1:  # Si el usuario no especifica (cantidad) el bot devuelve un error y lo borra luego de 5 secs
        await ctx.send("")
    else:
        await ctx.channel.purge(limit=cantidad)  # El bot elimina (cantidad) mensajes


@client.command()
async def sourcecode(ctx):
    """Devuelve el link de GitHub del bot"""
    await ctx.send("Hecho por Caches#8539 con discord.py, Codigo fuente en https://github.com/CachesKCH/TrolsoBot")


@client.command()
async def ping(ctx):
    """Comando simple de Ping para saber la latencia del bot al servidor"""
    await ctx.send(f"Pong! el bot respondio en {round(client.latency * 1000)} ms")


@client.command(aliases=["8ball"])
async def _8ball(ctx, *, pregunta):
    """Comando de 8ball"""
    respuestas = ["si bro", "no bro", "proveedores not found"]
    await ctx.send(f"Pregunta: {pregunta}\nRespuesta: {random.choice(respuestas)}")


@client.event
async def on_member_join(miembro):
    """El bot imprime a la terminal cada vez que un usuario se une"""
    print(f"{miembro} se ha unido al servidor.")


@client.event
async def on_member_remove(miembro):
    """El bot imprime a la terminal cada vez que un usuario se va"""
    print(f"{miembro} ha salido del servidor.")

# For loop que carga las extensiones en la carpeta ./cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(token)
