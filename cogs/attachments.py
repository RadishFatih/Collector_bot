import discord
import json
from discord.ext import commands
import aiohttp
import aiofiles


class Attachments(commands.Cog):
    def __init__(self, bot: discord):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        print(message.channel.id)
        att = len(message.attachments)
        if att > 0:
            for x in range(att):
                try:
                    #async with aiohttp.ClientSession() as session:
                    #    url = message.attachments[x].url
                    #    async with session.get(url) as resp:
                    #        if resp.status == 200:
                    #            f = await aiofiles.open(
                    #                f"files/{message.attachments[x].filename}",
                    #                mode="wb",
                    #            )
                    #            await f.write(await resp.read())
                    #            await f.close()
                    if str(message.channel) == "na-puste-pytania":
                        await message.add_reaction(emoji="🅰️")
                        await message.add_reaction(emoji="🅱️")

                except:
                    channel = message.channel
                    await channel.send("Unexpected error")

        # If message only consist of bot mention, bot will reply with current prefix

        if str(message.content)[3:-1] == str(self.bot.user.id) and str(
            message.author
        ) != str(self.bot.user):
            with open("./config/prefixes.json", "r") as f:
                prefixes = json.load(f)

            channel = message.channel
            await channel.send(f"Current prefix: {prefixes[str(message.guild.id)]}")


def setup(bot):
    bot.add_cog(Attachments(bot))
