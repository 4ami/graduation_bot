from twitter_linker import TwitterLinker
from bot import Tweet
import schedule
import time

twitter = TwitterLinker()
twitter.__load__()

i = 0

def main():
    tweet = Tweet()
    tweet = tweet.generate()
    twitter.send(tweet= f"Abdullah testing {i}")

schedule.every().second.do(main)
while True:
    schedule.run_pending()
    time.sleep(5)
    i+=1
    print('Sending tweet ... ')