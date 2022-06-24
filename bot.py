from discord import Client, Intents, Embed, Role, Colour, guild
from discord.emoji import Emoji
from discord.utils import get
from discord_slash import SlashCommand, SlashContext
from discord_slash.context import ComponentContext
from discord_slash.utils.manage_components import create_button, create_actionrow, wait_for_component
from discord_slash.model import ButtonStyle
from dotenv import dotenv_values
from commands import agedeclaration
from utilities import get_rgb_from_hex

config = dotenv_values('.env')

# Define guilds to register the commands to
guild_id=int(config['BOT_GUILD_ID'])

# Setup the main bot
client = Client(intents=Intents.default())

# Get the slashcommand object reference
slash = SlashCommand(client, sync_commands=True)

@client.event
async def on_component(ctx: ComponentContext):
    # Reference the guild and get the defined role
    guild = client.get_guild(guild_id)
    role = get(guild.roles, id = int(ctx.custom_id))
    
    # Try to add the role to the user
    if role is not None:

        user_role = get(ctx.author.roles, id = int(ctx.custom_id))

        if user_role is not None:
            embed = Embed(
                title="Role removed",
                description="Successfully removed 18+ role",
                color=Colour.red())

            await ctx.author.remove_roles(role)
        else:
            embed = Embed(
                title="Role set",
                description="Successfully added 18+ role",
                color=Colour.from_rgb(*get_rgb_from_hex('309279')))
            await ctx.author.add_roles(role)

        await ctx.send(embed=embed, hidden=True)
    else:
        await ctx.send("Invalid role specified", hidden=True)

agedeclaration.register(slash, guild_id)


# Run the client with the given key
client.run(config['BOT_API_KEY'])