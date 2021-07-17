import discord
import os
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = int(os.getenv('GUILD_ID'))

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    the_boys = discord.utils.get(bot.guilds, id=GUILD_ID)

    print('Connected')


@bot.command(name='tookmeds')
async def tookmeds(context):

    if str(context.author) == 'Sawooop#1134':
        await context.send('Good job, keep taking ur meds jit!')
    else:
        await context.send('Give jackson his meds back!')
        print(context.author)


'''@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$jit'):
        await message.channel.send('jit jit slaart!')'''

bot.run(TOKEN)
