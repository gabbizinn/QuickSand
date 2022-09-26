import os.path
from datetime import date
import random

#*Things left to do*
  #SOME IDEAS
  #1) Editing a post
  #2) Disliking/Liking
  #4) Make it where caps dont matter (check caps file)
  #5) view>tweet>input>SHOULD PRINT OUT ALL OF A USER"S TWEETS
  #6) share>which tweet input>should add tweet back to refresh(if cannot implement, remove it completely. Let us know so we may pla accordingly.)
  #7) save>INPUT>(input should search for that tweet and append it AND the OP's info in the save file)
  #8 get view saved tweet to work


#Opening Statement
print("        Welcome to Twotter!")
print("      |A Total Waste Of Time|")
print(" Please Create an Account or Log in!")
print("____________________________\n")

print("| Log in | | Create Account |")
inp = input("> ")

#COUNTER
#are likes going to be like reddit where you go negitive or like youtube with two diffrent counters?
likes = 0
dislikes = 0 

#ARGS
fname = "tweetarchive.txt"

#LOG IN
def login():
  #LOG IN // DONE
  if inp == ("Log in"):
    while True:
      user_login = input("Username: ")
      password_login = input("Password: ")
      if os.path.exists(f"{user_login}.txt") == True:
        with open(f"{user_login}.txt") as x:
          findpassword = x.readlines()  
          if password_login in findpassword:
            print("Login Successful")
            break
          else:
            print("Bad Password")
      elif FileNotFoundError:
        print("Account doesn't exist!")
        
#LIKE TWEETS  
def like_tweet(likes):
  print("What tweet are you liking?")
  inp = input("> ") #put emojis
  with open("tweetarchive.txt", "r") as findtweet:
    blank = findtweet.readlines()
    if blank != inp:
      likes += 1
      print(likes)
  #NOT DONE IGNORE ON PSUEDOCODE FOR NOW
      
#DISLIKE TWEETS
def dis_like_tweet(dislikes):
  print("What tweet are you disliking?")
  inp = input("❤. ") #put emojis
  with open("tweetarchive.txt", "r") as dis_like_tweet:
    dis_like = dis_like_tweet.readlines()
    if dis_like != inp:
      dislikes -= 1
      
#CREATE ACCOUNT // DONE     
def create_account():  
  if inp == ("Create Account"):
    while True:
      username = input("Username: ")  
      password = input("Password: ")
      
      if len(password) < 5:
        print("Password must be at least 5 characters.")
      try:
        if len(password) >= 5:
          open (f"{username}.txt", "x")
          with open (f"{username}.txt", "w") as f:
            f.write (f"{username}\n{password}")
            print("Successful first log in!")
            break
      except:
        FileExistsError
        print("Username Taken, waste your time even further by being more creative with a new one.")
        
#CREATE TWEETS
def create(likes):
  users_input = input("Enter Tweet: ")
  print("Which account would like to tweet from?")
  tweetdash = input("@")
  print("Tweet Posted, refresh to see if your tweet made it to the timeline!")
  today = date.today()
  with open("tweetarchive.txt", "a") as tweet:
    tweet.write(f"\n{users_input} | @{tweetdash} {likes}❤ {dislikes}👎 {today}")
  
#REFRESH TWEETS
def refresh_tweets(fname):
  lines=open(fname).read().splitlines()
  
  return random.sample(lines, 5)
  # i = 0 
  # #if i < 5:
  #   for line in lines:
  #     i +=1
  #     print(random.choice(line))
      
#OPEN TWEET FILE 
def findtweetsave():
    with open("tweetarchive.txt", "r") as x:
        looking = x.readlines()
    return looking
  
find = findtweetsave()

#SAVE TWEETS
def save_tweet():
  print("Please write the tweet you would like to save.")
  savetweet = input("> ")
  for x in find:
      if savetweet in x:
  # with open("tweetarchive.txt", "r") as findtweet:
  #   blank = findtweet.readlines()
  #   if blank != savetweet:
        print("Tweet saved")
        with open("saved.txt", "a") as save:
          save.write(f"\n{savetweet}")#ask about saving tweet info britt
          break
          
#VIEW SAVED TWEETS
def view_saved():
  with open ("saved.txt") as read:
    saved = read.read()
    return saved
  
#VIEW TWEETS  
def view_tweet():
  users_input = input("Who's tweet would you like to see?: ")
  with open("tweetarchive.txt", "r") as view_tweet:
    view_tweet.readline()
  return users_input

  
def main(inp):
#LOG IN
  if inp == "Log in":
    login()
    while True:
      #move input to its own line and give more spacing
      users_choice = input("[create], [view], [refresh], [share], [save]> ")
      if users_choice == "create":
        create(likes)
      elif users_choice == "view":
        print("Would you like to view a [tweet] or view [saved] tweet?")
        inp = input("> ")
        if inp == "saved":
          view_saved()
        elif inp == "tweet":
          view_tweet()
      elif users_choice == "refresh":
        refresh_tweets(fname)
        print(*refresh_tweets('tweetarchive.txt'),sep = "\n")
        print("|Like👍| |Dislike 👎| |Pass|")
        f = input("> ")
        if f == "Like":
          like_tweet(likes)
        elif f == "Dislike":
          dis_like_tweet(dislikes)
        else:
          pass
          
      elif users_choice == "share":
        ...
      elif users_choice == "save":
        save_tweet()

#CREATE ACCOUNT    
  if inp == "Create Account": 
    create_account()
    while True:
      users_choice = input("[create], [view], [refresh], [share], [save]> ")
      if users_choice == "create":
        create(likes)
      elif users_choice == "view":
        print("Would you like to view a [tweet] or view [saved] tweet?")
        inp = input("> ")
        if inp == "saved":
          view_saved()
          print(view_saved)
        elif inp == "tweet":
          view_tweet()
      elif users_choice == "refresh":
        refresh_tweets(fname)
        print(*refresh_tweets('tweetarchive.txt'),sep = "\n")
        print("|Like👍| |Dislike 👎| |Pass|")
        f = input("> ")
        if f == "Like":
          like_tweet(likes)
        elif f == "Dislike":
          dis_like_tweet(dislikes)
        else:
          break
      elif users_choice == "share":
        ...
      elif users_choice == "save":
        save_tweet()

if __name__ == '__main__':
  main(inp)
          
