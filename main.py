from art import *
from googletrans import Translator
import python_weather
import datetime
import random
import requests
import discord

class Main:
	def __init__(self):
		print('[LOG] Module EasyBotGame initalized successfully and successfully updated!')
		print('TEST краш!!!')
	def Random(self, min, max):
		self.min = min
		self.max = max
		return random.randint(self.min, self.max)
	async def TextToArt(self, ctx, text=''):
		self.text = text
		self.ctx = ctx
		await ctx.send(f'```{text2art(text)}```')
	async def AddRole(self, ctx, bot, rolename='', user=None):
		self.ctx = ctx
		self.rolename = rolename
		self.user = user
		self.bot = bot
		role = discord.utils.get(self.user.guild.roles, name=self.rolename)
		await user.add_roles(role)
		print(f'[LOG] Successfully added role {self.rolename} to {user.name}')
	async def DelRole(self, ctx, bot, rolename='', user=None):
		self.ctx = ctx
		self.rolename = rolename
		self.user = user
		self.bot = bot
		role = discord.utils.get(self.user.guild.roles, name=self.rolename)
		await user.remove_roles(role)
		print(f'[LOG] Successfully removed role {self.rolename} to {user.name}')
	async def ChangeNick(self, ctx, user, newnick):
		self.ctx = ctx
		self.user = user
		self.newnick = newnick
		self.currnick = ctx.author.nick
		await self.user.edit(nick=self.newnick)
		print(f'[LOG] Successfully changed nick from {self.currnick} to {self.newnick}')
	def Embed(self, text='', description=''):
		self.text = text
		self.description = description
		return discord.Embed(
        title = self.text,
        description = self.description,
    )
	class GetTime:
		def Hours(self):
			return datetime.datetime.now().strftime('%H')
		def Minutes(self):
			return datetime.datetime.now().strftime('%M')
		def Seconds(self):
			return datetime.datetime.now().strftime('%S')
		def Year(self):
			return datetime.datetime.now().strftime('%y')
		def Month(self):
			return datetime.datetime.now().strftime('%m')
		def Day(self):
			return datetime.datetime.now().strftime('%d')
	class Users:
		def GetCount(self, ctx):
			return ctx.guild.member_count
	def BotServers(self, bot):
		return bot.guilds
	class Weather:
		async def GetTemperature(self, city):
			client = python_weather.Client(format=python_weather.IMPERIAL)
			self.city = city
			temp = await client.find(self.city)
			return round((temp.current.temperature - 32) * 5/9)
			await client.close()