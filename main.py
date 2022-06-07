import configparser
import discord
from discord.ext import commands
import logging
from functions import *


# Read config
config = configparser.ConfigParser()
config.read('config.ini')

# Bot Needs Arguments
intents = discord.Intents(messages = True, guilds = True, reactions=True, members=True, presences=True)
Bot = commands.Bot(command_prefix="!", intents = intents)
token = config['discord']['token']
game = Game()
#Logging settings
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level=logging.INFO
# )

@Bot.event
async def on_ready():
    print("Ben Hazirim")

@Bot.event#Karsilama
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name ="general")
    await channel.send(f"@{member} aramiza katildi . Hosgeldi!")
    print(f"{member} aramiza katildi . Hosgeldi!")
@Bot.event#Cikma mesaji
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name ="general")
    await channel.send(f"@{member}Aramizdan ayrildi :(")
    print(f"{member} Aramizdan ayrildi :(")


@Bot.command(aliases=["game","oyun"])#Oyun
async def adilaxmedov(ctx, *args):
    if "roll" in args:
        await ctx.send(game.roll_dice())
    else:
        await ctx.send("Hatali Komut")

@Bot.command()#chat mesaj silme
@commands.has_role('admin')
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit = amount)
    print(f"{amount} Mesaj Basarili Sekilde Silindi") 

@Bot.command(aliases=['copy'])#Kanal Kopyalama
async def clone_channel(ctx, amount = 1):
    for i in range(amount):
        await ctx.channel.clone()

@Bot.command()#Kickleme
@commands.has_role('admin')
async def kick(ctx, member:discord.Member, *args, reason = "Yok"):
    await member.kick(reason=reason)

@Bot.command()#banlama
@commands.has_role('admin')
async def ban(ctx, member:discord.Member, *args, reason = "Yok"):
    await member.ban(reason=reason)

Bot.run(token)
