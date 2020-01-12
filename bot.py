from secret import token, secret_server_id
import random
import asyncio
import discord
from discord.ext import commands

p_var_server_id = secret_server_id  # Guarda el server ID secreto en una variable publica que puede ser reusada
# Define el prefix con el cual los comandos van a ser llamados
client = commands.Bot(command_prefix="tr:", case_insensitive=True)


# Imprime a la terminal el momento en que el bot esta listo para recibir comandos
@client.event
async def on_ready():
    print("El bot esta listo.")


# Comando usado para borrar una cantidad especifica de mensajes
@client.command()
@commands.has_role("TrolsoBotUSR")
async def clear(ctx, cantidad=0):
    cantidad += 1  # Suma 1 a la cantidad ya que el bot cuenta el comando como (1) mensaje
    if cantidad == 1:  # Si el usuario no especifica (cantidad) el bot devuelve un error y lo borra luego de 5 secs
        await ctx.send("")
    else:
        await ctx.channel.purge(limit=cantidad)  # El bot elimina (cantidad) mensajes


# Comando simple de Ping para saber la latencia del bot al servidor
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! el bot respondio en {round(client.latency * 1000)} ms")


# Comando de 8ball
@client.command(aliases=["8ball"])
async def _8ball(ctx, *, pregunta):
    respuestas = ["si bro", "no bro"]
    await ctx.send(f"Pregunta: {pregunta}\nRespuesta: {random.choice(respuestas)}")


# El bot imprime a la terminal cada vez que un usuario se une
@client.event
async def on_member_join(miembro):
    print(f"{miembro} se ha unido al servidor.")


# El bot imprime a la terminal cada vez que un usuario se va
@client.event
async def on_member_remove(miembro):
    print(f"{miembro} ha salido del servidor.")

client.run(token)
