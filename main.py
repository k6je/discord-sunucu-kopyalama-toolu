mytitle = "Discord Sunucu Kopyalama Aracı - kaje.inc"
from os import system
system("title "+mytitle)
import psutil
from pypresence import Presence
import time
import sys
client_id = 'Your Account ID'
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from serverclone import Clone

client = discord.Client()
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
print(f"""{Fore.BLUE}
  _  __              _ ______ 
 | |/ /    /\       | |  ____|
 | ' /    /  \      | | |__   
 |  <    / /\ \ _   | |  __|  
 | . \  / ____ \ |__| | |____ 
 |_|\_\/_/    \_\____/|______|
                              
                                                                                                  
{Style.RESET_ALL}
{Fore.YELLOW}> Geliştirici: kaje#1000 {Style.RESET_ALL}

{Fore.YELLOW}> Instagram:{Style.RESET_ALL}
{Fore.YELLOW}> https://instagram.com/kaje.inc/{Style.RESET_ALL}
        """)


token = input(f'Lütfen token belirtin:\n >')
guild_s = input('Kopyalanmasını istediğiniz sunucunun ID''si:\n >')
guild = input('Kopyalamanın aktarılacağı sunucunun ID''si:\n >')
input_guild_id = guild_s  # <-- input guild id
output_guild_id = guild  # <-- output guild id
token = token  # <-- your Account token


print("  ")
print("  ")

@client.event
async def on_ready():
    extrem_map = {}
    print(f"Giriş Yapılan Hesap: {client.user}")
    print("Sunucu Kopyalanıyor")
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    print(f"""{Fore.GREEN}


██╗  ██╗ ██████╗ ██████╗ ██╗   ██╗ █████╗ ██╗      █████╗ ███╗   ██╗██████╗ ██╗
██║ ██╔╝██╔═══██╗██╔══██╗╚██╗ ██╔╝██╔══██╗██║     ██╔══██╗████╗  ██║██╔══██╗██║
█████╔╝ ██║   ██║██████╔╝ ╚████╔╝ ███████║██║     ███████║██╔██╗ ██║██║  ██║██║
██╔═██╗ ██║   ██║██╔═══╝   ╚██╔╝  ██╔══██║██║     ██╔══██║██║╚██╗██║██║  ██║██║
██║  ██╗╚██████╔╝██║        ██║   ██║  ██║███████╗██║  ██║██║ ╚████║██████╔╝██║
╚═╝  ╚═╝ ╚═════╝ ╚═╝        ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝
                                                                               


    {Style.RESET_ALL}""")
    await asyncio.sleep(5)
    client.close()


client.run(token, bot=False)
