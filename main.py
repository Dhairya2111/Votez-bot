import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Setup Intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

@bot.command(name='unmute')
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, member: discord.Member, *, reason=None):
    """Unmutes a member by removing the Muted role or timing them out."""
    
    # 1. Handle Modern Discord Timeout (Communication Disabled)
    if member.is_timed_out():
        try:
            await member.edit(timed_out_until=None, reason=reason)
            await ctx.send(f'✅ Successfully removed timeout from {member.mention}.')
        except discord.Forbidden:
            await ctx.send("❌ I do not have permission to remove timeouts.")
        return

    # 2. Handle Legacy Role-based Muting
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    
    if not muted_role:
        await ctx.send("❌ No 'Muted' role found in this server.")
        return

    if muted_role in member.roles:
        try:
            await member.remove_roles(muted_role, reason=reason)
            await ctx.send(f'✅ Successfully unmuted {member.mention}.')
        except discord.Forbidden:
            await ctx.send("❌ I do not have permission to remove roles from this user.")
    else:
        await ctx.send(f"❓ {member.display_name} is not muted.")

@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ You need 'Manage Roles' permissions to use this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("❌ Could not find that member.")
    else:
        await ctx.send(f"⚠️ An error occurred: {str(error)}")

if __name__ == '__main__':
    if not TOKEN:
        print("Error: DISCORD_TOKEN not found in environment variables.")
    else:
        bot.run(TOKEN)