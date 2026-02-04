import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Define intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Initialize Bot
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

@bot.command(name='ping')
async def ping(ctx):
    """Check the bot's latency."""
    await ctx.send(f'🏓 Pong! {round(bot.latency * 1000)}ms')

@bot.command(name='echo')
async def echo(ctx, *, message: str):
    """Repeats what the user says."""
    await ctx.send(message)

@bot.command(name='userinfo')
async def userinfo(ctx, member: discord.Member = None):
    """Displays information about a user."""
    member = member or ctx.author
    embed = discord.Embed(title=f"User Info - {member}", color=discord.Color.blue())
    embed.set_thumbnail(url=member.display_avatar.url)
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.add_field(name="Joined Server", value=member.joined_at.strftime("%Y-%m-%d"), inline=True)
    embed.add_field(name="Account Created", value=member.created_at.strftime("%Y-%m-%d"), inline=True)
    embed.add_field(name="Top Role", value=member.top_role.mention, inline=True)
    await ctx.send(embed=embed)

@bot.command(name='clear')
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 5):
    """Deletes a specified number of messages."""
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f'🗑️ Deleted {amount} messages.', delete_after=3)

@bot.command(name='help')
async def help_command(ctx):
    """Custom help command."""
    embed = discord.Embed(title="Bot Commands", color=discord.Color.green())
    embed.add_field(name="!ping", value="Shows bot latency", inline=False)
    embed.add_field(name="!echo <text>", value="Repeats your message", inline=False)
    embed.add_field(name="!userinfo [@user]", value="Shows info about a user", inline=False)
    embed.add_field(name="!clear <num>", value="Deletes messages (Requires Manage Messages)", inline=False)
    await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ You don't have permission to use this command.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("⚠️ Missing arguments. Check !help for usage.")

if __name__ == '__main__':
    if not TOKEN:
        print("Error: DISCORD_TOKEN not found in environment variables.")
    else:
        bot.run(TOKEN)