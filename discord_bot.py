import gpt_api
import webscraping as web
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import requests
from datetime import datetime


load_dotenv()

discord_token = os.getenv("DISCORD_BOT_TOKEN")
id_canal = 1160297880481968290
intents = discord.Intents.all()
client = discord.Client(intents=intents)
logado = False

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
	print(f"Logado como {bot.user}")

	canal = bot.get_channel(id_canal)

	await canal.send("Fui inicializado. Toda interação comigo irá gerar um log informando o que foi feito, por quem foi feito e quem foi feito")


@bot.command()
async def gpt(ctx, *, comando):
	global logado
	if logado:
		log = {
		"usuario": ctx.author.name,
		"comando": "GPT",
		"data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
		}
		req = requests.post("http://127.0.0.1:80/logs", json=log)
		if req.status_code != 201:
			await ctx.send('Falha em enviar o Log para o servidor')
		print("comando GPT",comando)
		resposta = gpt_api.conversa(comando)
		await ctx.send(resposta)
	else:
		await ctx.send("Você precisa fazer login. Utilize /login username senha")

@bot.command()
async def puc(ctx):
	global logado
	if logado:
		log = {
		"usuario": ctx.author.name,
		"comando": "PUC",
		"data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
		}
		req = requests.post("http://127.0.0.1:80/logs", json=log)

		if req.status_code != 201:
				await ctx.send('Falha em enviar o Log para o servidor')

		await ctx.send(web.puc_cursos())
	else:
		await ctx.send("Você precisa fazer login. Utilize /login username senha")

@bot.command()
async def manga(ctx, *, comando):
	global logado
	if logado:
		log = {
			"usuario": ctx.author.name,
			"comando": "Manga " + comando,
			"data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
		}
		req = requests.post("http://127.0.0.1:80/logs", json=log)

		if req.status_code != 201:
				await ctx.send('Falha em enviar o Log para o servidor')

		await ctx.send(web.num_caps(comando))
	else:
		await ctx.send("Você precisa fazer login. Utilize /login username senha")

@bot.command()
async def ajuda(ctx):
   
  log = {
        "usuario": ctx.author.name,
        "comando": "Ajuda",
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
  req = requests.post("http://127.0.0.1:80/logs", json=log)

  if req.status_code != 201:
      await ctx.send('Falha em enviar o Log para o servidor')

  await ctx.send(
    '''
    Lembre-se de fazer login utilizando /login <nome> <senha>

    Utilize o comando /ajuda para saber todos os comandos disponíveis \n
    Utilize o comando /gpt <mensagem> para se comunicar com o chat GPT \n
    Utilize o comando /puc para ver todos os cursos de graduação oferecidos pela PUC Rio \n
    Utilize o comando /manga <nome_manga> para ver quantos capítulos já foram lançados de determinado mangá (baseado no site mangalivre)\n
    '''
  )
    
@bot.command()
async def login(ctx, username, password):
	global logado
    
	response = requests.post("http://127.0.0.1:80/login", json={'username': username, 'password': password})
	
	if response.status_code == 200:
		logado = True
		await ctx.send('Logado')
	else:
		logado = False
		await ctx.send('Falha no login. Verifique suas credenciais.')

def run_bot():
  bot.run(discord_token)
  