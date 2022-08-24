#script to scrape r/listentothis for music and download the audio from those videos
#ideally should be ran once per day
#Web Scrape
import praw
from pytube import YouTube
from datetime import date
import os

def main():
# Read-only instance
  reddit_read_only = praw.Reddit(client_id="",
                               client_secret="",
                               user_agent="")
  subreddit = reddit_read_only.subreddit("listentothis")
  post_url= []
  for post in subreddit.hot(limit=21):
      post_url.append(post.url)
      #print(post.title)
  post_url.pop(0)   
  
  #download from youtube

  today = date.today()
  day = today.strftime("%d-%m-%Y")
  SAVE_PATH_1 = '' #should be in format C:\\Users\\etc
  SAVE_PATH = SAVE_PATH_1 + "\\" + day
  
  if not os.path.exists(SAVE_PATH):
    os.mkdir(SAVE_PATH)
  
  for i in (post_url):
    try:
      yt = YouTube(i)
      #audio_test=yt.streams.filter(only_audio=True)
      #print(audio_test)
    except:
      print('--- Connection Error ---')

    try:
      audio = yt.streams.get_by_itag(140)
    except:
      print('Video Unavailable', i)
    else:
      print('Downloading', yt.title, i)
      audio.download(SAVE_PATH)
    
if __name__ == "__main__":
    main()

