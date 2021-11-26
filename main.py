import tweepy, random, os
from dotenv import load_dotenv
load_dotenv()

auth = tweepy.OAuthHandler(os.getenv("consumer_key"), os.getenv("consumer_secret"))
auth.set_access_token(os.getenv("access_key"), os.getenv("access_secret"))

api = tweepy.API(auth)

def tweetYes():
	tweets = ["Still dead", "Rotting in hell", "Having her grave pissed on, cause shes dead", "as dead as you can be", "will never see any daylight again", "as dead as pokemon go", "Dead dead dead", "Urine speaks louder than words, so piss on her grave when you get the chance", "Holding hands with Ronald Reagan in the deepest Level of hell", "Dead or Alive? No she's dead"]
	api.update_status(random.choice(tweets))

tweetYes()

