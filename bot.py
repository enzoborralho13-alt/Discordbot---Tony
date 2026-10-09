
import discord
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# ID do canal onde o bot vai dar Meow
CANAL_ID = 1553129498818379857

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

    if not meow_loop.is_running():
        meow_loop.start()

@tasks.loop(minutes = 5)
async def meow_loop():
    canal = bot.get_channel(CANAL_ID)

    if canal is not None:
        await canal.send("Meow 🐱")

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! Eu sou um bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)

bot.run("Token")
