import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix="m.")
token = os.getenv("DISCORD_BOT_TOKEN")
admins = os.getenv("ADMIN_IDS").split(",")
admins = [int(i) for i in admins]

@bot.event
async def on_ready() :
    await bot.change_presence(activity = discord.Game("with kids"))
    print("I am online")

@bot.command()
async def ping(ctx) :
    await ctx.send(f"🏓 Pong with {str(round(bot.latency * 1000))}ms")

@bot.command()
async def whoami(ctx) :
    await ctx.send(f"You are {ctx.message.author.name}")

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    async def cog_check(self, ctx):
        return ctx.message.author.id in admins

    @commands.command()
    async def clear(self, ctx, amount=3):
        await ctx.channel.purge(limit=amount)

    @commands.command()
    async def admin(self, ctx):
        await ctx.send("You are the better admin")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        if ctx.cog.qualified_name == "Admin":
            await ctx.send("( ͡⚆ ͜ʖ ͡⚆)╭∩╮")


bot.add_cog(Admin(bot))
bot.run(token)
