import discord
from discord.ext import commands

Bot = commands.Bot(command_prefix= "!", intents= discord.Intents.all())

@Bot.command()
async def destek(ctx):        #Destek komutu yazılan kanala Bir bildirim oluşturur. genelde Sesli Kanalda Bekleyen insanların işi daha hızlı çözülmesi için atılan bildirimdir.
    print(f"\033[94m[Sistem Mesajı Algılandı] Destek Talebi Oluşturuldu\033[91m [TERMİNAL LOG]")
    await ctx.send(f"**Destek Kısa Süre İcinde Sizlerle olucaktır. Bu Kanala Girip bekleyiniz.** <#İD> ") # son kısma destek ses kanal id sini yazın.
    await ctx.send(f"<@&İD>") #Yönetim Rol id sini yazın

@Bot.command()
async def say(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(message)

@Bot.event
async def on_ready():
    print("\033[94m[Sistem Mesajı Algılandı] Sistem Başlatıldı\033[91m [TERMİNAL LOG]")

@Bot.event
async def on_message(message: discord.Message):
    print(f"\033[94m[Sistem Chat Mesajı Algıladı] mesaj:\033[92m {message.content} \033[94mYazan Kişi:\033[92m {message.author}")

@Bot.event
async def on_member_join(member: discord.Member):
    print(f"\033[94m[Sistem Mesajı Algılandı] Giriş Yapıldı, yapan kişi:\033[93m {member.name}\033[91m [TERMİNAL LOG]")

@Bot.event
async def on_member_remove(member: discord.Member):
    print(f"\033[94m[Sistem Mesajı Algılandı] Çıkış Yapıldı, yapan kişi:\033[93m {member.name}\033[91m [TERMİNAL LOG]")

@Bot.command()
async def üyeat(ctx, member: discord.Member, reason):
    print(reason)
    await member.kick()
    await ctx.send("Üye Sunucudan Atıldı.")

@Bot.command()
async def üyebanla(ctx, member: discord.Member, reason):
    print(reason)
    await member.ban()
    await ctx.send("Üye Sunucudan Atıldı.")


#Komut listesi
#!üyeat @üye sebep
#!üyebanla @üye sebep
#!say Mesaj (Bota Mesaj Yazdırmayı Sağlar)
#Sunucuya Giren veya Cıkan kişileri Terminal e yazdırır.


#Botun tokeni Alttaki "token" içine Yazılıcak!  Dikkat edin "" leri Silmeyin Parantez içinde olmalı
Bot.run("token")