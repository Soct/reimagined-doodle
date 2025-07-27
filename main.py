import discord
import os
from dotenv import load_dotenv

load_dotenv()
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")

@bot.slash_command(name="help", description="Say hello to the bot")
async def help(ctx: discord.ApplicationContext):
    await ctx.respond("Hey2!")

@bot.slash_command(name="marceau", description="Say hello to the bot")
async def marceau(ctx: discord.ApplicationContext):
    voice_channel_list = ctx.guild.voice_channels
    for voice_channels in voice_channel_list:
        for member in voice_channels.members:
            print(member)

bot.run(os.getenv('TOKEN')) # run the bot with the token
