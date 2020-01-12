import traceback
import sys
from discord.ext import commands
import os
import discord


class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """Imprime un mensaje a la consola cuando la extension termina de cargar"""
        cog_name = os.path.basename(__file__)
        print(f"Extension {cog_name[:-3]} cargada exitosamente.")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """El evento que el programa genera cuando hay un error interno.
        ctx   : Context
        error : Exception"""

        # Esto previene a cualquier programa con handlers locales a ser procesados en este handler.
        if hasattr(ctx.command, 'on_error'):
            return

        ignored = (commands.CommandNotFound, commands.UserInputError)

        # Nos deja checkear por excepciones originales levantadas y mandadas a CommandInvokeError.
        # Si nada es encontrado, mantenemos la excepcion pasada a on_Command_error.
        error = getattr(error, 'original', error)

        # Cualquier cosa en la variable (ignored) va a ser ignorada y devolvera nada, haciendo nada.
        if isinstance(error, ignored):
            return

        elif isinstance(error, commands.DisabledCommand):
            return await ctx.send(f'{ctx.command} ha sido deshabilitado.')

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                return await ctx.author.send(f'{ctx.command} no se puede usar en Mensajes Privados.')
            except:
                pass


def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))
