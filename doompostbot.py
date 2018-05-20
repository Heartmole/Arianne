import random
import botUtils

class DoompostBot:

	# Constructor
	def __init__(self):
		# Leer tweets
		self.tweets = botUtils.readCsv('tweets.csv')
		botUtils.stringToDate(self.tweets, 3)
		# Leer frases de YouTube
		self.youtube = botUtils.readCsv('youtube.csv')
		botUtils.stringToDate(self.youtube, 3)
		# Leer imágenes
		self.images = []
		# Inicializar el randomizer
		random.seed()

	# Random tweet
	def randomTweet(self):
		try:
			index = random.randint(0, len(self.tweets) - 1)
			tweet = self.tweets[index]
			date = botUtils.dateToString(tweet[3]) if (len(tweet) > 3) else ""
			return "**\"%s\"**\n\n%s%s" % (tweet[1], tweet[0], date)
		except ValueError:
			pass # No hay tweets para sacar...

	# Random image
	def randomImage(self):
		return "Not implemented"

	# Random phrase from YouTube
	def randomYouTube(self):
		try:
			index = random.randint(0, len(self.youtube) - 1)
			youtube = self.youtube[index]
			date = botUtils.dateToString(youtube[3]) if (len(youtube) > 3) else ""
			return "**\"%s\"**\n\n%s%s" % (youtube[1], youtube[0], date)
		except ValueError:
			pass # No hay frases de YouTube para sacar...

	# Leer mensajes y realizar las acciones respectivass
	def readMessages(self):
		while (True):
			try:
				message = input()
				if (message == "!tweet"):
					print(self.randomTweet())
				if (message == "!image"):
					print(self.randomImage())
				if (message == "!youtube"):
					print(self.randomYouTube())
			except KeyboardInterrupt:
				print('\nKeyboardInterrupt')
				break
