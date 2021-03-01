import tweepy

ACCESS_TOKEN =
ACCESS_SECRET =
CONSUMER_KEY =
CONSUMER_SECRET =


def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)
    return api

api = connect_to_twitter_OAuth()

user = input("User:")
word_list=[]
persontweets = api.user_timeline(screen_name= user, count=10, include_rts = False)
for tweet in persontweets:
    word_list.append(tweet.text)
words=[]
for tweet in word_list:
    splited = tweet.split()
    words = words + splited
woah = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ "
final =[]
for word in words:
    idk =""
    for character in word:
        if character in woah:
            idk += character
    final.append(idk)
for list in final:
  if list=="":
    final.remove(list)

def smth(new):
  new.sort(key=len)
  return new
yeap =(smth(final))

for i in range(5):
  print(yeap[i])

for k in range((len(final) - 5), len(final)):
  print(yeap[k])


