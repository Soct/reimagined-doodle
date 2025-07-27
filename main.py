import discord
import os
import random
from dotenv import load_dotenv
import re

load_dotenv()
bot = discord.Bot()

prefix = "doodle"

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")

@bot.slash_command(name="help", description="Say hello to the bot")
async def help(ctx: discord.ApplicationContext):
    await ctx.respond("Hey2!")

@bot.slash_command(name="clean", description="Clean all channels created by me")
async def delete_toot_channels(ctx):
    for channel in ctx.guild.channels:
        if channel.name.startswith(prefix):
            await channel.delete()
            print(f"Deleted channel: {channel.name}")
    await ctx.send("All channels deleted.")
    return

@bot.slash_command(name="randomize", description="Randomize the channel you are in")
async def marceau(ctx: discord.ApplicationContext):
    voice_channel_list = ctx.guild.voice_channels
    members_list = []
    for voice_channels in voice_channel_list:
        for member in voice_channels.members:
            members_list.append(str(member))

    if len(members_list) == 0:
        await ctx.respond("There is not player in the voice channel")
        return

    if len(members_list) == 1:
        await ctx.respond("At least two players are needed, there is only one")
        return

    # Shuffle the array
    random.shuffle(members_list)
    mid = len(members_list) // 2
    ## Extract nicknames of the player
    player_team_1 = members_list[:mid]
    player_team_2 = members_list[mid:]

    embed = discord.Embed(
        title="League of Legend Team Randomizer",
        description="Voici votre channel randomizer en 2 équipes",
        color=discord.Colour.blurple(), # Pycord provides a class with default colors you can choose from
    )
    #embed.add_field(name="A Normal Field", value="A really nice field with some information. **The description as well as the fields support markdown!**")

    embed.add_field(name="Team 1", value='\n'.join(map(extract_nickname, player_team_1)), inline=False)
    embed.add_field(name="Team 2", value='\n'.join(map(extract_nickname, player_team_2)), inline=False)
 
    embed.set_footer(text="Bonne partie") # footers can have icons too
    embed.set_author(name="Pycord Team", icon_url="https://example.com/link-to-my-image.png")
    embed.set_thumbnail(url="https://example.com/link-to-my-thumbnail.png")
    embed.set_image(url="https://example.com/link-to-my-banner.png")
    await ctx.respond("", embed=embed)

    await create_vc_and_move(ctx, prefix + " " + "team1", player_team_1)
    await create_vc_and_move(ctx, prefix + " " + "team2", player_team_2)

def extract_nickname(name):
    match = re.search(r'\((.*?)\)', name)
    return match.group(1) if match else None

def extract_username(name):
    match = re.match(r'^(\S+)\s+\(.*\)', name)
    return match.group(1) if match else None

async def create_vc_and_move(ctx, channel_name, members):
    guild = ctx.guild

    await guild.create_voice_channel(name=channel_name)

    for member in members:
        await move_user_by_username(ctx.guild, extract_username(member), channel_name)

async def delete_voice_channel(ctx, channel_name):
    guild = ctx.guild
    channel = discord.utils.get(guild.voice_channels, name=prefix + " " + channel_name)
    if channel:
        await channel.delete()
    else:
        print("Channel not found")

def get_member_by_nickname(guild, nickname):
    for member in guild.members:
        if member.nick == nickname:
            return member
    return None

async def find_by_nick(ctx, nickname):
    member = get_member_by_nickname(ctx.guild, nickname)
    if member:
        await ctx.send(f"Found user: {member.display_name} (ID: {member.id})")
    else:
        await ctx.send(f"No user found with nickname '{nickname}'.")

async def move_user_by_username(guild: discord.Guild, username: str, target_channel_name: str):
    member = discord.utils.find(lambda m: m.name == username, guild.members)

    if not member:
        print(f"User '{username}' not found in this server.")
        return

    if not member.voice or not member.voice.channel:
        print(f"User '{username}' is not connected to any voice channel.")
        return
    
    # Find the target voice channel
    target_channel = discord.utils.get(guild.voice_channels, name=target_channel_name)
    if not target_channel:
        return f"Voice channel '{target_channel_name}' not found."
    
    # Move the member
    await member.move_to(target_channel)
    return f"Moved {member.display_name} to {target_channel.name}."

bot.run(os.getenv('TOKEN')) # run the bot with the token
