"""
API TOKEN ไปสมัครเอาเองที่เว็บ https://night-api.com/
"""


from nextcord.ui import button, View
from nextcord import Embed, ButtonStyle
import nextcord
from nextcord.ext import commands
import requests
from keep_Alive import keep_alive
import os

# ------------- CONFIG MAIN-------------- #

TOKEN = os.environ.get('TOKEN')
COLOR = 0xf8f8f8
PREFIX = "."
Images = "https://i.ibb.co/TDQqJhD/tumblr-p47bj0z1-At1uwii4ro8-540-3019061142.gif"
API_TOKEN = "TGUihFVnzD-05fCpYWJhFzCEhE4yTRv-cHTBeJn566"

# ------------- CONFIG MAIN-------------- #

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=PREFIX, help_command=None, intents=intents)

class ErrorHandlerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_command_error(self, ctx, error):
        if isinstance(error, commands.CommandError):
            await ctx.send(f"An error occurred: {str(error)}")

class WAIFU(View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(
        label='Waifu NSFW',
        style=nextcord.ButtonStyle.blurple
    )
    async def send(self, button: nextcord.Button, interaction: nextcord.Interaction):
        msg = await interaction.response.send_message('Please wait...', ephemeral=True)
        api = 'https://api.waifu.pics/nsfw/waifu'

        try:
            response = requests.get(api)
            response.raise_for_status() 

            url = response.json()['url']

            embed = Embed(
                title=f"**__WAIFU__**\n",
                description=f"Send by {interaction.guild.me.name}",
                color=COLOR
            )
            embed.add_field(name="API by", value="[Waifu](https://waifu.pics/)")
            embed.set_image(url)
            embed.set_footer(text="NSFW System", icon_url=interaction.guild.me.display_avatar.url)

            await interaction.user.send(embed=embed)

            await msg.edit(content='Sent, check DMs')
        except requests.RequestException as e:
            await msg.edit(content='Sorry, an error occurred while processing your request. Please try again later.')


class NSFW(View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @button(label="Neko Non-NSFW", style=ButtonStyle.primary)
    async def send_nekoimage(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await self.send_nsfw(interaction, "neko")

    @button(label="Hentai", style=ButtonStyle.primary)
    async def send_pussy(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await self.send_nsfw(interaction, "hentai")

    @button(label="kitsune", style=ButtonStyle.primary)
    async def send_creampie(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await self.send_nsfw(interaction, "hkitsune")

    @button(label="Neko", style=ButtonStyle.primary)
    async def send_neko_nsfw(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await self.send_nsfw(interaction, "hneko")

    @button(label="thigh", style=ButtonStyle.primary)
    async def send_hthigh(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await self.send_nsfw(interaction, "hthigh")

    @button(label="paizuri", style=ButtonStyle.primary)
    async def send_paizuri(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await self.send_nsfw(interaction, "paizuri")

    @button(label="irl-Pgif", style=ButtonStyle.primary)
    async def send_Pgif(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await self.send_nsfw(interaction, "pgif")

    @button(label="Boobs", style=ButtonStyle.primary)
    async def send_hboobs(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await self.send_nsfw(interaction, "hboobs")

    @button(label="Pussy", style=ButtonStyle.primary)
    async def send_hPussy(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await self.send_nsfw(interaction, "pussy")

    @button(label="irl-Tentacle", style=ButtonStyle.primary)
    async def send_Tentacle(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await self.send_nsfw(interaction, "tentacle") 

    @button(label="Thigh", style=ButtonStyle.primary)
    async def send_Thigh(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await self.send_nsfw(interaction, "thigh") 

    @button(label="Yaoi (Gay)", style=ButtonStyle.primary)
    async def send_Yaoi(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await self.send_nsfw(interaction, "yaoi") 

    @button(label="irl-Gonewild", style=ButtonStyle.primary)
    async def send_Gonewild(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await self.send_nsfw(interaction, "gonewild") 

    @button(label="irl-Boobs", style=ButtonStyle.primary)
    async def send_Boobs(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await self.send_nsfw(interaction, "boobs") 

    @button(label="irl-Ass", style=ButtonStyle.primary)
    async def send_Ass(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await self.send_nsfw(interaction, "ass") 

    @button(label="irl-Anal", style=ButtonStyle.primary)
    async def send_Anal(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await self.send_nsfw(interaction, "anal") 

    @nextcord.ui.button(
        label='NSFW RANDOM',
        style=nextcord.ButtonStyle.blurple
    )
    async def send(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        msg = await interaction.response.send_message('Please wait...', ephemeral=True)
        api = 'https://api.night-api.com/images/nsfw/'

        headers = {
            'authorization': API_TOKEN
        }

        try:
            response = requests.get(api, headers=headers)
            response_json = response.json()
            print("API Response:", response_json) 

            if response.status_code == 200 and 'content' in response_json and 'url' in response_json['content']:
                url = response_json['content']['url']

                embed = Embed(
                    title=f"**__RANDOM__**\n",
                    description=f"Send by {interaction.guild.me.name}",
                    color=COLOR
                )
                embed.add_field(name="API by", value="[Night Api](https://night-api.com/)")
                embed.set_image(url=url)
                embed.set_footer(text="NSFW System", icon_url=interaction.guild.me.display_avatar.url)

                await interaction.user.send(embed=embed)
                await msg.edit(content='Sent, check DMs')
            else:
                await msg.edit(content='Sorry, the NSFW API is currently down. Please try again later.')
        except requests.RequestException as e:
            await msg.edit(content='Sorry, an error occurred while processing your request. Please try again later.')

    async def send_nsfw(self, interaction: nextcord.Interaction, category: str):
        msg = await interaction.response.send_message('Please wait...', ephemeral=True)
        api = f'https://api.night-api.com/images/nsfw/{category}'

        headers = {
            'authorization': API_TOKEN
        }

        try:
            response = requests.get(api, headers=headers)
            response.raise_for_status()  

            url = response.json()['content']['url']

            embed = Embed(
                title=f"**__{category.upper()}__**\n",
                description=f"Send by {interaction.guild.me.name}",
                color=COLOR
            )
            embed.add_field(name="API by", value="[Night API](https://night-api.com/)")
            embed.set_image(url=url)
            embed.set_footer(text="NSFW System", icon_url=interaction.guild.me.display_avatar.url)

            await interaction.user.send(embed=embed)

            await msg.edit(content='Sent, check DMs')
        except requests.RequestException as e:
            await msg.edit(content='Sorry, an error occurred while processing your request. Please try again later')

@bot.slash_command(
    name="nsfw_menu",
    description="Setup NSFW system"
)
async def nsfw_setup(interaction: nextcord.Interaction):
    if not interaction.user.guild_permissions.administrator:
        return await interaction.response.send_message(content='[ERROR] No Permission For Use This Command.', ephemeral=True)
    
    embed1 = nextcord.Embed(
        title="**__NSFW MENU 1__**",
        description="```คลิกปุ่มเพื่อสุ่มรูปอนิเมะ 18+\nรูปภาพจะทำการส่งไปใน DMs นะ```",
        color=COLOR
    )
    embed1.set_image(url=Images)
    embed1.set_author(name=interaction.guild.name, icon_url=interaction.guild.icon.url)
    embed1.set_footer(text="all features are NSFW")
    
    embed2 = nextcord.Embed(
        title="**__NSFW MENU 2__**",
        color=COLOR
    )
    
    await interaction.channel.send(embed=embed1, view=NSFW())
    await interaction.channel.send(embed=embed2, view=WAIFU())
    await interaction.response.send_message(content='[SUCCESS] Done.', ephemeral=True)


@bot.event
async def on_ready():
    print(f"Started {bot.user.name}")
keep_alive()
bot.run(TOKEN)