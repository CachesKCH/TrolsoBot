from secret import token, secret_server_id
from discord.ext import commands, tasks
from itertools import cycle
import discord
import logging
import json
import random
import os
import asyncio

logging.basicConfig(level=logging.INFO)  # Inicializa el logger
with open("botconfig.json") as f:
    bot_config = json.load(f)  # Importa el archivo de configuracion a la variable bot_config

error_handler_on = False
p_var_server_id = secret_server_id  # Guarda el server ID secreto en una variable publica que puede ser reusada
admin_role = bot_config["admin_role"]  # Define el rol de moderacion segun informacion guardada en el archivo botconfig
client = commands.Bot(command_prefix="tr!", case_insensitive=True)  # Define el prefijo del bot
status = cycle(["Ahora con mas extraordinari", "Hello there", "Que listo que sos, goku", ":doot:", "Turbobatimamadisimo"
                ])


@client.event
async def on_ready():
    """Imprime a la terminal el momento en que el bot esta listo para recibir comandos"""
    change_status.start()
    print("El bot esta listo.")


# noinspection PyCallingNonCallable
@tasks.loop(seconds=30)
async def change_status():
    """Funcion que cambia el texto del bot con un timer. ATENCION: Recomiendo no bajar de 30 segundos"""
    await client.change_presence(activity=discord.Game(next(status)))


def role_check():

    """ >Checkea si un usuario tiene el rol de admin<
    Custom check que guarda la lista de roles de la persona que mando el comando, lo convierte en str y luego revisa
    si coincide con el rol de administrador para devolver un valor bool. este valor bool es usado como argumento en
    commands.check, si el valor es verdadero check decide que el codigo va a seguir ejecutandose, si es falso check
    para el codigo.
        el codigo es un poco hacky, no me juzguen tengo dos semanas de experiencia con python lol

        Ejemplo
        -------

        Se usa como decorador:
        @client.command()
        @role_check() <-----
        async def ban(ctx, member: discord.Member, *, reason=None):
            await member.ban(reason=reason)
    """

    async def predicate(ctx):
        roles = str(ctx.message.author.roles)
        return admin_role in roles
    return commands.check(predicate)


@client.command()
@role_check()
async def getemoji(ctx, emoji: discord.Emoji):
    """COMANDO DE DEBUG: Imprime la id de un emoji en la consola. USO: tr!getemoji :emoji: """
    print(emoji.id)


@client.command()
@role_check()
async def debug(ctx):
    """no hace nada, es mi comando de debug"""
    await ctx.send("I know you!  <:DOOT:665934856064073728>")


@client.command()
@role_check()
async def load(ctx, extension):
    """Comando que activa una extension especifica por nombre de archivo"""
    l_extension = f"cog_{extension}"
    await ctx.send(f"Activando extensión {l_extension[4:]}...")
    try:
        client.load_extension(f"cogs.{l_extension}")
        await ctx.send(f"Extensión {l_extension[4:]} activada exitosamente en {round(client.latency * 1000)} ms.")
    except discord.ext.commands.errors.ExtensionAlreadyLoaded:
        await ctx.send(f"Extensión {l_extension[4:]} ya esta activada")


@client.command()
@role_check()
async def unload(ctx, extension):
    """Comando que desactiva una extension especifica por nombre de archivo"""
    l_extension = f"cog_{extension}"
    await ctx.send(f"Desactivando extensión {l_extension[4:]}...")
    try:
        client.unload_extension(f"cogs.{l_extension}")
        await ctx.send(f"Extensión {l_extension[4:]} desactivada exitosamente en {round(client.latency * 1000)} ms.")
    except discord.ext.commands.errors.ExtensionNotLoaded:
        await ctx.send(f"Extensión {l_extension[4:]} ya esta desactivada")


@client.command()
@role_check()
async def reload(ctx, extension):
    """Comando que actualiza una extension especifica por nombre de archivo"""
    l_extension = f"cog_{extension}"
    await ctx.send(f"Desactivando extensión {l_extension[4:]}...")
    client.unload_extension(f"cogs.{l_extension}")
    await ctx.send(f"Reactivando extensión {l_extension[4:]}...")
    client.load_extension(f"cogs.{l_extension}")
    await ctx.send(f"Extensión {l_extension[4:]} activada exitosamente en {round(client.latency * 1000)} ms.")


@client.command()
@role_check()
async def modrole(ctx, *, nuevo_rol):
    """>Comando que cambia el rol de moderacion< (de una forma no muy pythonica por que soy un manco de la programacion)
    fw= file write,  fr= file read"""
    global admin_role
    global bot_config
    admin_role = nuevo_rol
    bot_config["admin_role"] = admin_role
    with open("botconfig.json", "w") as fw:
        json.dump(bot_config, fw, indent=2)
    with open("botconfig.json", "r") as fr:
        bot_config = json.load(fr)
        admin_role = bot_config["admin_role"]
    await ctx.send(f"Rol de moderacion cambiado exitosamente a {admin_role}")


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


for filename in os.listdir("./cogs"):  # For loop que carga las extensiones en la carpeta ./cogs
    if filename.startswith("cog_") and filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

if error_handler_on:  # desactiva el error handler para cosas de debug
    client.unload_extension(f"cogs.cog_error_handler")
    print("ATENCION: el Error Handler esta desactivado")
else:
    print("ATENCION: el Error Handler esta activado")

client.run(token)
