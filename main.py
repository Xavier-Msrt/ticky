
import os
import discord
from utils import random_string
from discord.member import Member
from discord.guild import Guild
from discord.ext import commands
from dotenv import load_dotenv

class TicketButton(discord.ui.View):
    @discord.ui.button(label='🎟️ Click here to open a ticket', style=discord.ButtonStyle.primary, custom_id="open_ticket")
    async def open_ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.guild is None or not isinstance(interaction.user, Member):
            return
        
        guild: Guild = interaction.guild
        user: Member = interaction.user

        # sort ticket in one category
        category = discord.utils.get(guild.categories, name='Tickets')
        if category is None:
            category = await guild.create_category('Tickets')

        # creat an ticket channel
        while True:
            channel_name = f"{interaction.user.name}-{random_string(5)}"
            if not discord.utils.get(guild.text_channels, name=channel_name):
                break


        ticket_channel = await guild.create_text_channel(
            name=channel_name,
            category=category,
            reason=f"Ticket created by {interaction.user}"
        )

        # give channel permission
        await ticket_channel.set_permissions(guild.default_role, view_channel=False)
        await ticket_channel.set_permissions(user, view_channel=True, send_messages=True)

        await interaction.response.send_message(f"Your ticket has been created: {ticket_channel.mention}", ephemeral=True)


def all_command(bot):

    @bot.command(help='Create a ticket creator button')
    @commands.guild_only()
    @commands.has_role('ticket-manager')
    async def create(ctx: commands.Context):

        embed = discord.Embed(
            title="Create a ticket",
            description="If you need help for anything you can click to the button",
            color=discord.Color.dark_orange(),
        )
        await ctx.send(
            embed=embed,
            view=TicketButton()
        )


def all_events():
    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send(f"🚫 You must have the `{error.missing_role}` role to use this command.")
        elif isinstance(error, commands.CheckFailure):
            await ctx.send("🚫 You cannot use this command here.")
        else:
            raise error

if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    if token is None:
        print('Please provide a token in the .env file (DISCORD_TOKEN)')
        exit()


    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True

    bot = commands.Bot(command_prefix='!', intents=intents)
    all_events()
    all_command(bot)
    bot.run(token)