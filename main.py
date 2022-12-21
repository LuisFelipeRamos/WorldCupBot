import tweepy
import os
from dotenv import load_dotenv
import schedule
import time
import datetime

# load environment variables
load_dotenv()

# put them in local variables
API_KEY = os.environ.get("API_KEY")
API_KEY_SECRET = os.environ.get("API_KEY_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")

def tweet_missing_days():

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # create API with authentication
    api = tweepy.API(auth)

    missing_days: int = (datetime.datetime(2026, 6, 8) - datetime.datetime.now()).days

    tweet: str = f"Faltam {missing_days} para a Copa do Mundo de 2026!"

    api.update_status(tweet)

def main():
    
    schedule.every().day.at("14:00:00").do(tweet_missing_days)

    while True:
        schedule.run_pending()
    return

if __name__ == "__main__":
    main()
