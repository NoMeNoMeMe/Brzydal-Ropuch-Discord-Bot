import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')


class Users(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Event - cog loaded
    # @commands.Cog.listener()
    # async def on_ready(self):
    #     print('Users loaded successfully')

    # greet new user
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined a server.')
        for channel in member.guild.channels:
            if str(channel) == "ogólny":
                await channel.send(f'WITAJ KUCU {member}. NIECH ŻYJE ZBRODNICZY REŻIM!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left a server.')
        for channel in member.guild.channels:
            if str(channel) == "ogólny":
                await channel.send(f'POŻEGNAJMY RAZEM KUCA {member}.')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def info(self, ctx, *, member: discord.Member):
        """(id)"""
        fmt = 'Kuc {0} przybył do Bronksu {0.joined_at} i ma przypisane {1} role.'
        await ctx.send(fmt.format(member, len(member.roles)))

    @info.error
    async def info_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('Nie znalazłem takiego kuca...')

    # @commands.Cog.listener()
    # async def on_message(self, message):
    #     id = bot.get_guild(707151504368468020)
    #     channels = ["ogólny"]
    #     if message.channel in channels:
    #
    #        if message.content.find("/users") != -1:
    #            await message.channel.send(f"Liczba kucy: {id.member_count}")


def setup(bot):
    bot.add_cog(Users(bot))
