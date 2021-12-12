import discord
from discord import channel
from discord.ext import commands
from discord.flags import Intents


intents=discord.Intents.default()
intents.members=True

bot=commands.Bot(command_prefix='-',intents=intents)

@bot.event
async def on_ready():
    print(">>BOT以上線<<")

@bot.event
async def on_member_join(member):
    channel=bot.get_channel(919499537998049290)
    await channel.send(f'{member} 歡迎進來!')

@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(919499621007523840)
    await channel.send(f'{member} 遠走高飛了QAQ')

@bot.command()
async def ping(ctx): 
    await ctx.send(f'{round(bot.latency*1000)}(ms)')


bot.run('OTE5NDkzODIyODUxOTg5NTM0.YbWnWg.cHvwh9MuCV0qJ6HqWoLKzb5CDTU')