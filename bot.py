from secret import token, secret_server_id
import discord

p_var_server_id = secret_server_id

client = discord.Client()


@client.event
async def on_message(message):
    print(message.content)
    server_id = client.get_guild(439556519311441920)
    channels = ["comandos", "general"]

    if str(message.channel) in channels:
        if message.content.find("!ligma") != -1:
            await message.channel.send("fav")
        elif message.content == "!users":
            await message.channel.send(f"""# de Miembros {server_id.member_count}""")

client.run(token)
