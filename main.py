import discord
import random
import asyncio
import praw
import giphy_client
from discord.ext import commands, tasks
from discord.ext.commands import Context
from giphy_client.rest import ApiException
from random import choices



Token = 'MTAxMDkyMzUwMTE2ODg5ODA2OA.GSQotT.CLZU6DCR_IKiob0eUS9ERegUHkRc_aC_bPnDHw'

#bot starting process

client = commands.Bot(command_prefix = '!', intents = discord.Intents.all())

@client.event
async def on_ready():
    print('We have logged.')

    await client.change_presence(activity=discord.Game(name=f"on {len(client.guilds)} servers | !commands"))

#custom commands

@client.command()
async def hello(ctx):
    await ctx.reply("Hello!")

@client.command()
async def yash(ctx):
    await ctx.reply('khargosh ke saath busy hai wo....')

@client.command()
async def random(ctx):
    await ctx.reply ({random.randrange(1000000)})

@client.command()
async def beg(ctx):
    await ctx.send('pls work')

@client.command()
async def mihika(ctx):
    await ctx.reply('loves sarthak')

@client.command()
async def manku(ctx):
    await ctx.reply('mayank-uddin sheikh mulla')

@client.command()
async def ping(ctx):
    await ctx.send(f"pong! {round(client.latency*1000)} ms")

@client.command()
async def who(ctx):
    await ctx.reply('mujhe modi ji ne parliament se nikal diya isiliye berozgaari ki wajah se yaha baitha hu aur mere jaise anya berozgaaro ki madad kar rha hu')

@client.command()
async def meme(ctx):
  subreddit = reddit.subreddit("SaimanSays")
  all_subs = []


  top = subreddit.top(limit = 50)

  for submission in top:
    all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    em = discord.Embed(title = name)

    em.set_image(url = url)

    await ctx.send(embed= em)

#embed for about

@client.command(aliases=['user','info'])
@commands.has_permissions(kick_members=True)
async def about(ctx, member: discord.Member):
    embed = discord.Embed(title = member.name , description = member.mention , color = discord.Colour.red())
    embed.add_field(name = "ID", value = member.id , inline = True)
    embed.set_thumbnail(url = member.avatar.url)
    embed.set_footer(icon_url = ctx.author.avatar, text = f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

#custom help command

client.remove_command("help")

@client.group(invoke_without_command=True)
async def commands(ctx):
    em = discord.Embed(title = "Commands", description = "Use !command for all commands.", color = ctx.author.color)

    await ctx.send (embed = em)

#commands for giphy client

@client.command()
async def lul(ctx):

  api_key='niWm87YTpIgXJdJGFoVhGs3WEpSlLKTu'
  api_instance = giphy_client.DefaultApi()
  q="hello"

  try:

    api_response = api_instance.gifs_search_get(api_key, q, limit=5, rating = 'r')
    lst = list(api_response.data)
    giff = lst

    emb = discord.Embed(title=q)
    emb.set_image(url = f'https://media.giphy.com/media/{giff.id}/giphy.gif')

    await ctx.channel.send(embed=emb)

  except ApiException as e:
    print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)


#reddit memes starts from here

reddit = praw.Reddit(client_id = "sBgRk6j_UaaRPwUYX4tffw",
                    client_secret = "wMw3TsrYz_6mWtgXFfkT1m2H67P-ug",
                    username = "Groovy",
                    password = "ripGroovy09",
                    user_agent = "Grooovy")





client.run (Token)

