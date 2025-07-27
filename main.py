import discord
import os
import random
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

@bot.slash_command(name="randomize", description="Randomize the channel you are in")
async def marceau(ctx: discord.ApplicationContext):
    voice_channel_list = ctx.guild.voice_channels
    members_list = []
    for voice_channels in voice_channel_list:
        for member in voice_channels.members:
            members_list.append(str(member))
            print(member)
    random.shuffle(members_list)
    print(members_list)
    nb_name = len(members_list)
    print(nb_name)
    nb_team1 = round(nb_name/2)
    print(nb_team1)
    team1 = members_list[:nb_team1]
    team2 = members_list[-(nb_name-nb_team1):]
    embed = discord.Embed(
        title="League of Legend Team Randomizer",
        description="Voici votre channel randomizer en 2 équipes",
        color=discord.Colour.blurple(), # Pycord provides a class with default colors you can choose from
    )
    #embed.add_field(name="A Normal Field", value="A really nice field with some information. **The description as well as the fields support markdown!**")

    embed.add_field(name="Team 1", value='\n'.join(team1), inline=False)
    embed.add_field(name="Team 2", value='\n'.join(team2), inline=False)
 
    embed.set_footer(text="Bonne partie") # footers can have icons too
    #embed.set_author(name="Pycord Team", icon_url="https://example.com/link-to-my-image.png")
    #embed.set_thumbnail(url="https://example.com/link-to-my-thumbnail.png")
    #embed.set_image(url="https://example.com/link-to-my-banner.png")
    await ctx.respond("Hello! Here's a cool embed.", embed=embed)

bot.run(os.getenv('TOKEN')) # run the bot with the token
