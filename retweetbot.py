# A twitter bot which retweets the latest tweet from a random
# twitter user that is in the top 30 on Twitter with followers.

import sys
import simple_twit 
import tweepy
import random

def reversal(string):
    length = len(string)
    i = len(string)
    rev = ""
    while(i>=0):
        rev=rev+string[i:i+1]
        i-=1
    return rev
def main():
    # This call to simple_twit.create_api will create the api object that
    # Tweepy needs in order to make authenticated requests to Twitter's API.
    api = simple_twit.create_api()
    simple_twit.version()
    top30 = ['@BarackObama','@katyperry','@justinbieber','@rihanna','@taylorswift13','@Cristiano','@ladygaga','@TheEllenShow','@YouTube','@ArianaGrande',
             '@realDonaldTrump','@jtimberlake','@KimKardashian','@selenagomez','@twitter','@britneyspears','@cnnbrk','@shakira','@jimmyfallon', '@narendramodi',
             '@BillGates','@neymarjr','@MileyCyrus','@nytimes','@JLo','@KingJames','@BrunoMars','@CNN','@Oprah','@BBCBreaking']
    me = api.get_user("joshmathew_iae")
    print(me.screen_name)
    public_tweets = api.home_timeline()

    cont = True
    while (cont):
        try: 
            index = random.randrange(0,30)
            randuser = api.user_timeline(top30[index])
            randtweet = randuser[0].text
            ident = randuser[0].id
            print(randtweet)
            print("\n\nReversed:")
            revd = reversal(randuser[0].text)
            print(revd)
            message = top30[index]+' '+revd
            api.update_status(message,ident)
            print(top30[index])
            cont = False
        except:
                        #check for errors
            print("\nERROR occured, trying again...\n")

if __name__ == "__main__":
    main()

    
    
    
