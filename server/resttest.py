# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '778543465860915200-2e6vYoCTyhmqQdBcRV5r1LQvK8SLpez'
ACCESS_SECRET = 'RB5lFlpwWRo4Ieu3eVNEUYzrG7Wr3T2yOvTYDgcUQQump'
CONSUMER_KEY = 'Wq5WnCX5fiNyuPPmgEXHPj9G4'
CONSUMER_SECRET = 'YQhF1tAVH5Jn5AlaiE7NprgoLXJdMET0nlfrlEdplAJoY1bxsA'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter REST API
twitter = Twitter(auth=oauth)
            
# Search for latest tweets about "#nlproc"
#iterator = twitter.statuses.user_timeline(screen_name="twitterapi")
iterator = twitter.search.tweets(q="")
#iterator = twitter.users.tweets(q="actors")

iterator1 = iterator["statuses"]


# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 
tweet_count = 1000
for tweet in iterator1:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    #print json.dumps(tweet)  
    #print "\n\n", tweet["text"]

    if 'extended_entities' in tweet:
                ee = tweet['extended_entities']
                
                if ee['media']:
                    media=ee['media'][0]
                    print "EE: type:", media['type']
                

    
    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)
       
    if tweet_count <= 0:
        break 
