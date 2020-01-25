import discord
from discord import utils

t = 'TOKEN' # Token для бота

POST_ID = 000000000000000000  # Заменить на id будущего поста

DATA = {
	"1️⃣":658332820841955328, 
	"2️⃣":658332921823756289,
	"3️⃣":664005495341711388,
	"4️⃣":664005500324544513,
	"5️⃣":658477685944877073,
	"6️⃣":659489792156762134,
	"7️⃣":658333153576091662,
	"8️⃣":659490641885265955,
	"9️⃣":664005687424188438,
	"🔟":664005849500352532 ,
	"🇦":664005801199009822 ,
	"🇧":660770081789313024 ,
	"🇨":660770021055660036 ,
	"🇩":664005894471942187 ,
}

EXCROLES = (658331716250763284, 658463445783674893, 659854388671545374, 658635192306630658, 658334122028040223)

class Bot(discord.Client):
	async def on_raw_reaction_add(self, payload):
		message = await utils.get(utils.get(self.guilds, id=payload.guild_id).text_channels, id=payload.channel_id ).fetch_message(payload.message_id)
		mem = utils.get(message.guild.members, id=payload.user_id)

		if message.id == POST_ID:
			s = payload.emoji.name
			r = utils.get(message.guild.roles, id=DATA[s])
			if r != None and len([i for i in mem.roles if i.id not in EXCROLES]) < 5:
				await mem.add_roles( r )
				print("[Add Role] {0.name} for {1.display_name}".format(r, mem))
			else:
				print("[Error] Role hasn't been added")	

	async def on_raw_reaction_remove(self, payload):
		message = await utils.get(utils.get(self.guilds, id=payload.guild_id).text_channels, id=payload.channel_id ).fetch_message(payload.message_id)
		mem = utils.get(message.guild.members, id=payload.user_id)

		if message.id == POST_ID:
			s = payload.emoji.name
			r = utils.get(message.guild.roles, id=DATA[s])
			if r != None:
				await mem.remove_roles(r)
				print("[Rem Role] {0.name} for {1.display_name}".format(r, mem))
			else:
				print("[Error Role] can't remove role for {.display_name}".format(mem))		


	async def on_ready(self):
		print("[Log] READY")	

if __name__ == '__main__':
	c = Bot()
	c.run(t)
