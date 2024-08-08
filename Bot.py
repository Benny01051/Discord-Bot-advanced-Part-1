
import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "welcome":  # Replace 'welcome' with the name of your welcome channel
            welcome_message = f"Welcome to the server, {member.mention}!"
            

                
            await channel.send(welcome_message)
            break

bot.run("YOUR BOT TOKEN")
