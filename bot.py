import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

sonuc = ("SİYAH", "KIRMIZI", "YEŞİL")

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def nasilimm(ctx):
    await ctx.send("FaÇaSıN kArDeŞiM bEnİm DiKkAt Et KeSmE bİzİ hA")
    
@bot.command()
async def bye(ctx):
    await ctx.send("baysssss :3 :3 :3")
       
@bot.command()
async def rulet(ctx, karar: str):
    secilen_renk = random.choice(sonuc)
    
    if secilen_renk == karar:
        await ctx.send("Tebrikler Tahmininiz Doğru :)")
    else:
        await ctx.send(f"Maalesef Kaybettiniz :(, Cevap {secilen_renk} Olmalıydı")

        
        
bot.run("")
