import discord
from discord.ext import commands
from pyternos import Client
import os

# Load credentials from environment variables
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
ATERNOS_USERNAME = os.getenv("ATERNOS_USERNAME")
ATERNOS_PASSWORD = os.getenv("ATERNOS_PASSWORD")
SPECIFIC_SERVER_NAME = os.getenv("ATERNOS_SERVER_NAME")

# Initialize Discord Bot
bot = commands.Bot(command_prefix="!")

# Initialize Aternos Client
aternos = Client(ATERNOS_USERNAME, ATERNOS_PASSWORD)

# Find the specific server
server = None
for s in aternos.list_servers():
    if s.server_id == SPECIFIC_SERVER_NAME:
        server = s
        break

@bot.command()
async def start(ctx):
    """Starts the Aternos server when requested."""
    if server and server.status == "online":
        await ctx.send(f"Server **{SPECIFIC_SERVER_NAME}** is already running!")
    else:
        server.start()
        await ctx.send(f"Starting Aternos server **{SPECIFIC_SERVER_NAME}**...")

bot.run(DISCORD_TOKEN)
