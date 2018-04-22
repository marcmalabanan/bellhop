import discord
import re
from discord.ext import commands

TOKEN = 'NDM3Mjc1MDAzNjg4NTgzMTk4.DbzroQ.-Lje0_hhkdMTcrwg2G_bEir6vbs'
IMHERE = re.compile(r"(i[']+m|i[\"]+m|im) he[r]+e", re.IGNORECASE)

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    if IMHERE.search(message.content):
        await message.channel.send("{0.author.mention}, <:ctd_jade:435997993171419136> I'm here <:ctd_jade:435997993171419136>".format(message))

@bot.command()
async def imhere(ctx):
    await ctx.send("{0.author.mention}, <:ctd_jade:435997993171419136> I'm here <:ctd_jade:435997993171419136>".format(ctx))

@bot.command()
async def schedule(ctx):
    await ctx.send("{0.author.mention}, here is the current Back to Back podcast schedule: \n\n**Monday**: Black to Black with Amin / Black to Black overflow (Patreon exclusive) \n**Tuesday**: The Basketball Buds \n**Wednesday**: Zach Harper and Friends / SnarkHoops (Patreon exclusive) \n**Thursday**: Nerder She Wrote \n**Friday**: The Friday Mailbag \n\nOther Patron exclusive podcasts drop randomly!".format(ctx))

@bot.command()
async def wtf(ctx):
    await ctx.send("https://cdn.vox-cdn.com/uploads/chorus_asset/file/9825985/2017_12_06_20_45_42.gif")

@bot.command()
async def wow(ctx):
    await ctx.send("https://imgur.com/a/yPBWVcR")

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Bellhop", description="The list of commands for the Bellhop are:", color=0xeee657)

    embed.add_field(name="/imhere", value="Gives a special message from Jade.", inline=False)
    embed.add_field(name="/schedule", value="Gives the current Back to Back podcast schedule.", inline=False)
    embed.add_field(name="/wtf", value="Gives an appropriate 'wtf' gif.", inline=False)
    embed.add_field(name="/wow", value="Gives an appropriate 'wow' gif.", inline=False)
    embed.add_field(name="/help", value="Gives this message.", inline=False)

    await ctx.send(embed=embed)

bot.run(TOKEN)