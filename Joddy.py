# Work with Python 3.6
import discord
from discord.utils import get
import asyncio

TOKEN = 'NTE2MDY0MTMwMTAxMjgwNzcw.DtuN8g.532aiMm5GjCKgOcfhMJQBrY47R4'

client = discord.Client()

role_list = ['Archer', 'Assassin', 'Priest', 'Runeblade']

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!archer'):
        role = get(message.server.roles, name='Archer')
        await client.add_roles(message.author, role)
        await client.delete_message(message)
        msg = '{0.author.mention} has been assigned Archer role'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!assassin'):
        role = get(message.server.roles, name='Assassin')
        await client.add_roles(message.author, role)
        await client.delete_message(message)
        msg = '{0.author.mention} has been assigned Assassin role'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!priest'):
        role = get(message.server.roles, name='Priest')
        await client.add_roles(message.author, role)
        await client.delete_message(message)
        msg = '{0.author.mention} has been assigned Priest role'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!runeblade'):
        role = get(message.server.roles, name='Runeblade')
        await client.add_roles(message.author, role)
        await client.delete_message(message)
        msg = '{0.author.mention} has been assigned Runeblade role'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!berserker'):
        role = get(message.server.roles, name='Berserker')
        await client.add_roles(message.author, role)
        await client.delete_message(message)
        msg = '{0.author.mention} has been assigned Berserker role'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!heavygunner'):
        role = get(message.server.roles, name='Heavy Gunner')
        await client.add_roles(message.author, role)
        await client.delete_message(message)
        msg = '{0.author.mention} has been assigned Heavy Gunner role'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!knight'):
        role = get(message.server.roles, name='Knight')
        await client.add_roles(message.author, role)
        await client.delete_message(message)
        msg = '{0.author.mention} has been assigned Knight role'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!wizard'):
        role = get(message.server.roles, name='Wizard')
        await client.add_roles(message.author, role)
        await client.delete_message(message)
        msg = '{0.author.mention} has been assigned Wizard role'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!thief'):
        role = get(message.server.roles, name='Thief')
        await client.add_roles(message.author, role)
        await client.delete_message(message)
        msg = '{0.author.mention} has been assigned Thief role'.format(message)
        await client.send_message(message.channel, msg)


    if message.content.startswith("!unassign"):
        roles_cleared = True

        for r in role_list:
            # Check every role
            role = discord.utils.get(message.server.roles, name=r)
            if role in message.author.roles:
                # If they have the role, get rid of it
                try:
                    await client.remove_roles(message.author, role)
                    await asyncio.sleep(1)
                except discord.Forbidden:
                    await client.send_message(message.author, "I don't have perms to remove roles.")
                    roles_cleared = False
                    break

        if roles_cleared:
            msg = '{0.author.mention} has had class roles removed.'.format(message)
            await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)