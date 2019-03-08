import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", status=discord.Status.idle, activity=discord.Game(name="given dzban XD.."))

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='Algorytma', type=3))
    print('gotowy')
@bot.command()
async def user(ctx, member:discord.User = None):
    if member == None:
        member = ctx.message.author
        pronoun = 'Twoj'
    else:
        pronoun = 'Their'
    name = f"{member.name}#{member.discriminator}"     
    status = member.status   
    await ctx.channel.send(f'Jestes {name}. {pronoun} status to {status}.')



    
bot.run('NTUzNjM2MTgwMjMxNDU0NzM0.D2Q-Og.KDByfKzgFdikNnXMQ-E-Nyb2Kcw')
