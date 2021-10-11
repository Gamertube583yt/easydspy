from art import *
import random
import discord

class Main:
	def __init__(self):
		print('[LOG] Module EasyBotGame initalized successfully!')
	async def Spam(self, ctx, text='', count=0):
		self.text = text
		self.ctx = ctx
		self.count = count
		for i in range(count):
			await ctx.send(text)
		print('-'*10 + f'\n[LOG] Spam with:\nTEXT: {self.text}\nCOUNT: {self.count}\nCTX: {self.ctx}\nsuccessfully ended!\n' + '-'*10)
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