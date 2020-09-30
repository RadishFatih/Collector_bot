import discord
from discord.ext import commands
import aiohttp
import aiofiles

class Attachments(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        att = len(message.attachments)
        if att > 0:
            for x in range(att):
                try:
                    async with aiohttp.ClientSession() as session:
                        url = message.attachments[x].url
                        async with session.get(url) as resp:
                            if resp.status == 200:
                                f = await aiofiles.open(f'files/{message.attachments[x].filename}', mode='wb')
                                await f.write(await resp.read())
                                await f.close()
                except:
                    channel = message.channel
                    await channel.send('Unexpected error')

def setup(bot):
    bot.add_cog(Attachments(bot))
