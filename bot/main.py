import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix="m.")
token = os.getenv("DISCORD_BOT_TOKEN")
admins = ["244876633528336384"]

@client.event
async def on_ready() :
    await client.change_presence(activity = discord.Game("with kids"))
    print("I am online")

@client.command()
async def ping(ctx) :
    await ctx.send(f"🏓 Pong with {str(round(client.latency * 1000))}ms")

@client.command()
async def whoami(ctx) :
    await ctx.send(f"You are {ctx.message.author.name}")

@client.command()
async def clear(ctx, amount=3) :
    if (ctx.message.author.id in admins):
        await ctx.channel.purge(limit=amount)


client.run(token)
