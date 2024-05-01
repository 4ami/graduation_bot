import tweepy
from dotenv import load_dotenv
import os

class TwitterLinker:
    _api_key = None
    _secret = None
    _bearer = None
    _access_token = None
    _access_token_secret = None
    __authed = False
    _client = None
    _client_secret = None
    api = None
    def __init__(self) -> None:
        load_dotenv()
        
    
    def __load__(self)  -> bool:
        self._api_key = os.getenv("API_KEY")
        self._secret = os.getenv("API_SECRET_KEY")
        self._bearer = os.getenv("BEARER_TOKEN")
        self._access_token = os.getenv("ACCESS_TOKEN")
        self._access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
        self._client = os.getenv("CLIENT_ID")
        self._client_secret = os.getenv("CLIENT_SECRET")

        _auth = tweepy.Client(
            bearer_token= self._bearer,
            consumer_key= self._api_key,
            consumer_secret= self._secret,
            access_token= self._access_token,
            access_token_secret= self._access_token_secret
        )
        
        if _auth is None:
            return False
        
        self.api = _auth
        self.__authed = True
        
        return True
    
    def send(self, tweet:str,) -> bool:
        assert self.__authed, "Assertion Error: you must invoke __load__() before call send()"
        assert tweet is not str or len(tweet) == 0, "Assertion Error: tweet must be provided!"
        
        try:
            self.api.create_tweet(text= tweet)
            print("Sent!")
            return True
        except Exception as e :
            print(e)
            return False             
             