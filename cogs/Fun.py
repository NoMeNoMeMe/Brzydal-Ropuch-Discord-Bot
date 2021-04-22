import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
# client = discord.Client()


class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Event - cog loaded
    # @commands.Cog.listener()
    # async def on_ready(self):
    #     print('Fun loaded successfully')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        channel = await self.bot.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = await self.bot.fetch_user(payload.user_id)
        emoji = '<:brzydalropuch:706884719035285634>'

        await message.add_reaction(emoji)

    @commands.Cog.listener()
    async def on_message(self, message):
        id = bot.get_guild(707151504368468020)

        if message.author.bot:
            return
        else:
            if message.content.lower().find("wolmo") != -1:
                await message.channel.send("JA LUBIE SZYPKO")
            elif message.content.lower().find("wolno") != -1:
                await message.channel.send("JA LUBIE SZYPKO")
            elif message.content.lower().find("szypko") != -1:
                await message.channel.send("JA LUBIE WOLMO")
            elif message.content.lower().find("szybko") != -1:
                await message.channel.send("JA LUBIE WOLMO")

    # @commands.Cog.listener()
    # async def on_raw_reaction_remove(self, payload):
    #     channel = await self.bot.fetch_channel(payload.channel_id)
    #     message = await channel.fetch_message(payload.message_id)
    #     user = await self.bot.fetch_user(payload.user_id)
    #     emoji = '<:brzydalropuch:706884719035285634>'
    #     user_id = 706592540463333506
    #     me = discord.Guild.me
    #
    #     await message.remove_reaction(emoji, me)


def setup(bot):
    bot.add_cog(Fun(bot))
