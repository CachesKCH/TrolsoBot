from secret import token, secret_server_id
import random
import discord
from discord.ext import commands

p_var_server_id = secret_server_id  # Guarda el server ID secreto en una variable publica que puede ser reusada
client = commands.Bot(command_prefix="tr:")  # Define el prefix con el cual los comandos van a ser llamados


@client.event
async def on_ready():
    print("El bot esta listo.")


@client.command()
async def clear(ctx, cantidad=0):
    cantidad += 1
    await ctx.channel.purge(limit=cantidad)


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! el bot respondio en {round(client.latency * 1000)} ms")


@client.command(aliases=["8ball"])
async def _8ball(ctx, *, pregunta):
    respuestas = ["si bro", "no bro"]
    await ctx.send(f"Pregunta: {pregunta}\nRespuesta: {random.choice(respuestas)}")


@client.event
async def on_member_join(miembro):
    print(f"{miembro} se ha unido al servidor.")


@client.event
async def on_member_remove(miembro):
    print(f"{miembro} ha salido del servidor.")

client.run(token)
