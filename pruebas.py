import traceback
import sys
from discord.ext import commands
import os
import discord

# # Comando para cambiar el rol usado para checkear si tienes permisos de admin o moderador
# @client.command()
# @commands.has_role(admin_role)
# async def changerole(ctx, *, new_role):
#     global admin_role
#     admin_role = str(new_role)

# For this error example we check to see where it came from...
elif isinstance(error, commands.BadArgument):
if ctx.command.qualified_name == 'tag list':  # Check if the command being invoked is 'tag list'
    return await ctx.send('I could not find that member. Please try again.')

# All other Errors not returned come here... And we can just print the default TraceBack.
print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

"""Below is an example of a Local Error Handler for our command do_repeat"""


@commands.command(name='repeat', aliases=['mimic', 'copy'])
async def do_repeat(self, ctx, *, inp: str):
    """A simple command which repeats your input!
    inp  : The input to be repeated"""

    await ctx.send(inp)


@do_repeat.error
async def do_repeat_handler(self, ctx, error):
    """A local Error Handler for our command do_repeat.
    This will only listen for errors in do_repeat.
    The global on_command_error will still be invoked after."""

    # CHeckea si el argumento inp no esta.
    if isinstance(error, commands.MissingRequiredArgument):
        if error.param.name == 'inp':
            await ctx.send("You forgot to give me input to repeat!")