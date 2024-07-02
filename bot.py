import discord
from discord import app_commands
from discord.ext import commands
from discord import Embed
import os
import dotenv

dotenv.load_dotenv()

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='!', intents=intents)

statsdict = {}
cstack = []


commands_list = [
    {"name": "/commands", "description": "Lists all commands"},
    {"name": "/ping", "description": "Replies with Pong!"},
    {"name": "/set", "description": "Set the number of workouts completed for a user"},
    {"name": "/jim", "description": "Add a workout to total"},
    {"name": "/stats", "description": "Shows total workouts per user"},
    {"name": "/commandstack", "description": "See most recent commands used"},
    # Add more commands as needed``
]

def add_command(command, user):
    cstack.append((user, command))
    if len(cstack) > 10:
        cstack.pop(0)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    try:
        s = await bot.tree.sync()
        print(f'Synced {s} commands')
    except Exception as e:
        print(e)
        print(f'Error syncing commands: {e}')
    print(f'Logged in as {bot.user.name} - {bot.user.id}')


@bot.tree.command(name='ping', description='Replies with Pong!')
async def ping(interaction: discord.Interaction):
    embed = discord.Embed(title='Pong!', description=f'{round(bot.latency * 1000)} ms')
    embed.color = discord.Color.green()
    embed.set_thumbnail(url=bot.user.avatar)
    user = interaction.user.global_name
    add_command('ping', user)
    await interaction.response.send_message(embed=embed, ephemeral=True)
    

@bot.tree.command(name='commands', description='List all commands')
async def commands(interaction: discord.Interaction):
    embed = discord.Embed(title='Commands', description='List of all commands')
    embed.color = discord.Color.greyple()
    embed.set_thumbnail(url=bot.user.avatar)
    user = interaction.user.global_name
    add_command('commands', user)
    for command in commands_list:
        embed.add_field(name=('```' + command['name'] + '```'), value=command['description'], inline=False)
    await interaction.response.send_message(embed=embed, ephemeral=True)


@bot.tree.command(name='set', description='Set the number of workouts completed')
async def set(interaction: discord.Interaction,  member: discord.Member, number: int):
    user = interaction.user.global_name
    userset = member.global_name
    if userset == None:
        await interaction.response.send_message('User not found or is a bot. Please try again.', ephemeral=True)
    else:
        statsdict[userset] = number
        add_command('set', user)
        if number == 1:
            await interaction.response.send_message(f'You have set {userset} to {number} workout')
        else:
            await interaction.response.send_message(f'You have set {userset} to {number} workouts')


@bot.tree.command(name='jim', description='Add a workout to total')
async def jim(interaction: discord.Interaction):
    embed=discord.Embed(title='Workout added!', description='')
    embed.color = discord.Color.teal()
    user = interaction.user.global_name
    add_command('jim', user)
    if user not in statsdict:
        statsdict[user] = 1
        await interaction.response.send_message(embed=embed.add_field(name=f'{user} has completed* `1` workout!', value='').set_thumbnail(url=interaction.user.avatar))
    
    else:
        statsdict[user] += 1
        await interaction.response.send_message(embed=embed.add_field(name=f'{user} has completed* `{statsdict[user]}` workouts!', value='').set_thumbnail(url=interaction.user.avatar))


@bot.tree.command(name='stats', description='Total workouts per user')
async def stats(interaction: discord.Interaction):
    embed = discord.Embed(title='Stats', description='')
    embed.color = discord.Color.green()
    user = interaction.user.global_name
    add_command('stats', user)
    least = 5000000
    leastuser = ''
    for user in statsdict:
        if statsdict[user] < least:
            least = statsdict[user]
            leastuser = user
    if least == 5000000:
        embed.add_field(name='No workouts have been completed', value='', inline=False)
    else:
        if least == 1:
            embed.add_field(name=(leastuser + ' has the least workouts with `' + str(least) + '` workout'), value="", inline=False)
        else:
            embed.add_field(name=(leastuser + ' has the least workouts with `' + str(least) + '` workouts'), value="", inline=False)
    for user in statsdict:
        embed.add_field(name=f'{user}:\t`{statsdict[user]}`', value='', inline=False)
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name='commandstack', description='see most recent commands used')
async def commandstack(interaction: discord.Interaction):
    embed = discord.Embed(title='Command Stack', description='List of most recent commands used')
    embed.color = discord.Color.greyple()
    if cstack == None or cstack.__len__() == 0:
        embed.add_field(name='No commands used yet', value='', inline=False)
    else:
        for tuple in reversed(cstack):
            embed.add_field(name=(tuple[0] + ' used command: ```/' + tuple[1] + '```'), value='', inline=False)
    await interaction.response.send_message(embed=embed, ephemeral=True)


bot.run(os.getenv('TOKEN'))