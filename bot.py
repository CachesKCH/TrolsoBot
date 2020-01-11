from secret import token, secret_server_id
import random
import discord
from discord.ext import commands

p_var_server_id = secret_server_id  # Guarda el server ID secreto en una variable publica que puede ser reusada
client = commands.Bot(command_prefix=".")  # Define el prefix con el cual los comandos van a ser llamados


@client.event
async def on_ready():
    print("Bot is ready.")


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! el bot respondio en {round(client.latency * 1000)} ms")


@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
    responses = ["si bro", "no bro"]
    await ctx.send(f"Pregunta: {question}\nRespuesta: {random.choice(responses)}")


@client.event
async def on_member_join(member):
    print(f"{member} se ha unido al servidor.")


@client.event
async def on_member_remove(member):
    print(f"{member} ha salido del servidor.")
client.run(token)
