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
async def help(ctx: discord.ApplicationContext):
    await ctx.respond("Hey2!")

@bot.slash_command(name="tchoupinax", description="Say hello to the bot")
async def help(ctx: discord.ApplicationContext):
    await ctx.defer()

    channel = discord.utils.get(ctx.guild.voice_channels, name="Vocal")

    if not channel:
        await ctx.respond("Channel 'Vocal' not found.")
        return

    members_array = []
    for member in ctx.guild.members:
        members_array.append(member.display_name)

    await ctx.respond(f"Members in #Vocal2: {', '.join(members_array)}")

bot.run(os.getenv('TOKEN')) # run the bot with the token