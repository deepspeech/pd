import unittest
import tweepy
import requests
import json
import twitter_info

# Developer: Nunez, Priscila
# Assignment: HW7
# Instructors: Niharika and Chong Li
# Professor: Van Lent
# Collaborators: (Myself)Priscilla N., Kyle E., Maheen K., Michele G., and Aaron C. 
# Date: 10.24.17


## NunezP Retrieved my secret values to authenticate to Twitter. Replaced each of these 
## with variables rather than filling in the empty strings if you choose to do the secure way 
## for EC points 
consumer_key = twitter_info.consumer_key
consumer_secret = twitter_info.consumer_secret
access_token = twitter_info.access_token
access_token_secret = twitter_info.access_token_secret

## NunezP authentication to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


#NunezP Grab Api data from Twitter 
# Set up library to grab stuff from twitter with your authentication, and 
# return it in a JSON-formatted way

api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
#NunezP first ask user what they are looking for
# x = input("type in a search query ")
# public_tweets = api.search(x) 
# #print(public_tweets["statuses"][0]["text"])

# for tweet in public_tweets["statuses"][0:5]:
# 	print(tweet["text"])
# 	print ("\n \n \n \n") #prints spaces 

##NunezP I can choose to use range to do a while loop or for loop
## for x in range(3):
## print ('hi') - testing how many times it runs

## NunezP setting a file name with variable - because this exists we know the contents are from the file and storing in json dictionary. 
## If we can't open the file then if any produce an error it will go to the except block of code.
## Guess what - not going to open because it's a json file
CACHE_FNAME = "206W17_HW7_Twitter.json"
try:
	cache_file = open(CACHE_FNAME,'r')
	cache_contents = cache_file.read()
	cache_file.close()
	CACHE_DICTION = json.loads(cache_contents)
except:
	CACHE_DICTION = {}

def getSearchWithCaching(q):
	#url = serviceurl + urllib.parse.urlencode({'address': loc}) #This example is used for location

	if q in CACHE_DICTION:
		print("Data was in the cache")
		return CACHE_DICTION[q]
	else:
		print("Making a request for new data...")
		data = api.search(q) 
		try: # This should ALWAYS work 
			CACHE_DICTION[q] =  data
			dumped_json_cache = json.dumps(CACHE_DICTION)
			fw = open(CACHE_FNAME,"w")
			fw.write(dumped_json_cache)
			fw.close() # Close the open file
			return CACHE_DICTION[q]
		except: #This should ALWAYS work 
			print("Wasn't in cache and wasn't valid search either")
			return None
count = 0
for num in range(3): #Big nested loop example 
#while count < 3 is another option but verify with Prof Van Lent if < 3 is ok.

#while True: # This is an infinite loop example
    search = input('Enter search query: ') #This is an example for lines 58 to 95
    #if len(address) < 1: break #if len (address) < 1: (without the break)
    data = getSearchWithCaching(search)
    public_tweets = data["statuses"] #["address_components"] if was using for location
    for tweet in public_tweets[0:5]:
        #if 'country' in d["types"]: (If this was based on location use while loop)
        print("TEXT: \t" , tweet["text"])
        print("CREATED AT: \t" , tweet["created_at"])

        print ("\n \n \n \n") #prints spaces #end of Big nested loop example
        #count += 1 