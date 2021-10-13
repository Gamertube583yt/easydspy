from art import *
from googletrans import Translator
import python_weather
import datetime
import random
import requests
import discord
import json


class Main:
	def __init__(self, log = False):
		self.log = log
		if self.log is not False:
			print('[LOG] Module EasyBotGame initalized successfully and successfully updated!')
			print('[LOG] File main.py successfully updated!')
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
		if self.log is not False:
			print(f'[LOG] Successfully added role {self.rolename} to {user.name}')
	async def DelRole(self, ctx, bot, rolename='', user=None):
		self.ctx = ctx
		self.rolename = rolename
		self.user = user
		self.bot = bot
		role = discord.utils.get(self.user.guild.roles, name=self.rolename)
		await user.remove_roles(role)
		if self.log is not False:
			print(f'[LOG] Successfully removed role {self.rolename} to {user.name}')
	async def ChangeNick(self, ctx, user, newnick):
		self.ctx = ctx
		self.user = user
		self.newnick = newnick
		self.currnick = ctx.author.nick
		await self.user.edit(nick=self.newnick)
		if self.log is not False:
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
	class UserDatabase:
		def CreateUser(self, id, data):
			self.id = id
			self.data = data
			with open(f'users/{self.id}.json', 'w') as f:
				json.dump(self.data, f)
		def SetValue(self, id, data, newvalue):
			self.id = id
			self.data = data
			self.newvalue = newvalue
			print(self.newvalue)
			f = open('users/' + str(self.id)+ '.json', 'r+')
			data = json.load(f)
			f.seek(0)
			r = f.read()
			f.truncate(0)
			f.seek(0)
			f.write(r.replace(data[self.data], self.newvalue))
		def GetValue(self, id, value):
			self.id = id
			self.value = value
			f = open('users/' + str(self.id)+ '.json')
			data = json.load(f)
			d = data[value]
			return d
	class RPactions:
		async def StartListener(self, ctx, list):
			list = list
			cmc = ctx.content.lower()
			lets = []
			for i in cmc.split(' '):
				lets.append(cmc.split(' '))
			lets = lets[0]
			while True:
				for i in range(len(lets)):
					if lets[i] in list:
						await ctx.channel.send(list[lets[i]].replace('{u1}', ctx.author.mention).replace('{u2}', ctx.content.split(" ")[1]))
						return
					return