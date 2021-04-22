import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')


class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Event - cog loaded
    # @commands.Cog.listener()
    # async def on_ready(self):
    #     print('Moderation loaded successfully')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """(id)"""
        await member.kick(reason=reason)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """(id)"""
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')

    # Unban user
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        """(id)"""
        banned_users = await ctx.guild.bans()  # get banned users as list
        member_name, member_discriminator = member.split('#')  # User#1234 -> User, 1234

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned{user.name}#{user.discriminator}')
                return

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        """(int) default = 5"""
        await ctx.channel.purge(limit=amount)

    # # jeśli ktoś zmienia nick na podany, bot zmienia go na poprzedni
    # @commands.Cog.listener()
    # async def on_member_update(self, before, after):
    #     nick = after.nick
    #     last = before.nick
    #     if nick:
    #         if nick.lower().count("tim") > 0
    #             if last:
    #                 await after.edit(nick=last)
    #             else:
    #                 await after.edit(nick="Nope")


    # # usuwa niecenzuralne słowa
    # for word in bad_words:
    #     if word in bad_words:
    #         print(f"A bad word {word} was said.")
    #         await message.channel.purge(limit=1)

def setup(bot):
    bot.add_cog(Moderation(bot))
