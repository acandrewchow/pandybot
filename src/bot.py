# bot.py
from asyncio import streams
import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
import pandas_datareader as  web

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

# remove default Help command
bot.remove_command('help')

# move a member
@bot.command()
async def move(ctx, member: discord.Member, channel: discord.VoiceChannel):
    await member.move_to(channel)
    await ctx.send(f'{member} has been moved')

# roll dice
@bot.command(name='roll_dice', help='Simulates rolling dice e.g - !roll_dice 1 6')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

# create text channel
@bot.command(name='create-channel-text', help='Creates a new text channel')
@commands.has_role('admin')
async def create_channel(ctx, channel_name='General'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new text channel: {channel_name}')
        await guild.create_text_channel(channel_name)

# Help Command
@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title='Bot Commands',
        description='List of Commands:',
        color=discord.Colour.blue()
    )
    embed.set_thumbnail(url='https://avatars.githubusercontent.com/u/40132839?s=400&u=da6471b1e9f2051b7ceca901711880f175453901&v=4')
    embed.add_field(
        name='!help',
        value='List of all commands',
        inline=False
    )
    await ctx.send(embed=embed)




@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')





bot.run(TOKEN)