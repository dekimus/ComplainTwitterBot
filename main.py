from InternetSpeedTwitterBot import InternetSpeedTwitterBot
import time

PDOWN = 30
PUP = 30

bot = InternetSpeedTwitterBot(PUP,PDOWN)
twuser = "TU_USUARIO_TWITTER_AQUI"
twpass = "TU_PASS_AQUI"
bot.get_internet_speed()
bot.tweet_at_provider(twuser, twpass)





