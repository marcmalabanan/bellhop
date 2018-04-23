import discord
import random
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
    await bot.process_commands(message)

    if message.author != bot.user:
        if IMHERE.search(message.content):
            await message.channel.send("{0.author.mention}, <:ctd_jade:435997993171419136> I'm here <:ctd_jade:435997993171419136>".format(message))

@bot.command()
async def schedule(ctx):
    await ctx.send("{0.author.mention}, here is the current Back to Back podcast schedule: \n\n**Monday**: Black to Black with Amin / Black to Black overflow (Patreon exclusive) \n**Tuesday**: The Basketball Buds \n**Wednesday**: Zach Harper and Friends / SnarkHoops (Patreon exclusive) \n**Thursday**: Nerder She Wrote \n**Friday**: The Friday Mailbag \n\nOther Patron exclusive podcasts drop randomly!".format(ctx))

@bot.command()
async def social(ctx):
    await ctx.send("{0.author.mention}, follow Count The Dings on social media: \n\n**Twitter**: http://www.twitter.com/countthedings \n**Facebook**: http://www.facebook.com/countthedings \n**YouTube**: http://bit.ly/2IqxSBC \n**Instagram**: http://www.instagram.com/countthedings".format(ctx))

@bot.command()
async def wow(ctx):
    IMAGES = ["https://imgur.com/45uoRlu", "https://imgur.com/a/yPBWVcR"]
    await ctx.send(IMAGES[random.randint(0,len(IMAGES) - 1)])

@bot.command()
async def wtf(ctx):
    await ctx.send("https://cdn.vox-cdn.com/uploads/chorus_asset/file/9825985/2017_12_06_20_45_42.gif")

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Bellhop", description="The list of commands for the Bellhop are:", color=0xeee657)

    embed.add_field(name="/help", value="Gives this message.", inline=False)
    embed.add_field(name="/schedule", value="Gives the current Back To Back podcast schedule.", inline=False)
    embed.add_field(name="/social", value="Gives the social media links for Count The Dings.", inline=False)
    embed.add_field(name="/wow", value="Gives an appropriate 'wow' gif.", inline=False)
    embed.add_field(name="/wtf", value="Gives an appropriate 'wtf' gif.", inline=False)

    await ctx.send(embed=embed)

bot.run(TOKEN)