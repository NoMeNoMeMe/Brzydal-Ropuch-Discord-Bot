import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')


class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Event - cog loaded
    # @commands.Cog.listener()
    # async def on_ready(self):
    #     print('Fun loaded successfully')

    # Dodaje reakcję, gdy ktoś inny doda swoją reakcję
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        channel = await self.client.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = await self.client.fetch_user(payload.user_id)
        emoji = '<:brzydalropuch:706884719035285634>'

        await message.add_reaction(emoji)

    @commands.Cog.listener()
    async def on_message(self, message):
        id = client.get_guild(707151504368468020)

        if message.content.find("wolmo") != -1:
            await message.channel.send("JA LUBIE SZYPKO")
        elif message.content.find("wolno") != -1:
            await message.channel.send("JA LUBIE SZYPKO")
        elif message.content.find("Wolmo") != -1:
            await message.channel.send("JA LUBIE SZYPKO")
        elif message.content.find("Wolno") != -1:
            await message.channel.send("JA LUBIE SZYPKO")

        elif message.content.find("szypko") != -1:
            await message.channel.send("JA LUBIE WOLMO")
        elif message.content.find("szybko") != -1:
            await message.channel.send("JA LUBIE WOLMO")
        elif message.content.find("Szybko") != -1:
            await message.channel.send("JA LUBIE WOLMO")
        elif message.content.find("Szypko") != -1:
            await message.channel.send("JA LUBIE WOLMO")

    # usuwa emoji kiedy ktoś inny usunie swoje - chwilowo nie działa
    # @commands.Cog.listener()
    # async def on_raw_reaction_remove(self, payload):
    #     channel = await self.client.fetch_channel(payload.channel_id)
    #     message = await channel.fetch_message(payload.message_id)
    #     user = await self.client.fetch_user(payload.user_id)
    #     emoji = '<:brzydalropuch:706884719035285634>'
    #     user_id = 706592540463333506
    #     me = discord.Guild.me
    #
    #     await message.remove_reaction(emoji, me)


def setup(client):
    client.add_cog(Fun(client))
