# yt_dlp, requests, google-api-client, google_oauth_ something

import subprocess, json, yt_dlp, requests, sys, random
import datetime
from time import sleep
from googleapiclient.http import MediaFileUpload
from Google import Create_Service


CLIENT_SECRET_FILE='client_secret.json'
API_NAME='youtube'
API_VERSION='v3'
SCOPES=['https://www.googleapis.com/auth/youtube.upload']


service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

# wait time b4 next uploadz
MINIMUM_TIME = 60*120
MAXIMUM_TIME = 60*240

# scrapes tiktokpage & returns ALL data
def titok(page_link):

    video = "DrippyTok"

    query = page_link

    ydl_opts = {}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        meta = ydl.extract_info(query, download=False)
    return json.dumps(meta, indent=4)

    subprocess.getoutput('yt-dlp --format mp4 --output {}.mp4 {}'.format(video,'{}'.format(query)))
    
# downloads video from RAW PAGE LINK!! DO NOT DIRECTLY USE THIS, FIRST SCRAPE FOR VIDEO RAW VIDEO LINK
def download_video(link, file_name):    
  #iterate through all links in video_links
  # and download them one by one
  #obtain file_name by splitting url and getting last string

  print ("Downloading file:%s"%file_name)

  #create response object
  r = requests.get(link, stream = True)

  #download started
  with open(file_name, 'wb') as f:
    for chunk in r.iter_content(chunk_size = 1024*1024):
      if chunk:
        f.write(chunk)

  print ("%s downloaded!\n"%file_name)
 
  print ("All videos downloaded!")
  return 
 
def remove_water_mark(marked_link):
  marked_list = marked_link.split('&')
  unmarked = marked_list[0]

  return unmarked

def full_process(link_database):
  
  print(link_database)
  
  
  # make a list of RAW video links
  for link in link_database:

    
    filejson = json.loads(titok(link)) # convert scraped data form json to Python-compatible dict value
    
    title = filejson['title'] # tiktok video title
    uploader = filejson['uploader'] # user who uploaded it
    video_title = f'{title} @{uploader}'# youtube video title

    # tiktokvideo1, tiktokvideo2, etc... file names for ease of management...
    file_name = f'videos/tiktokvideo{link_database.index(link)}'



    watermarked_link = filejson['formats'][0]['url'] # selects URL from dict (previously JSON)

    unmarked_link = remove_water_mark(watermarked_link)

    download_video(unmarked_link, file_name)

    upload_video_to_yt(video_title, file_name)
    
    idx = link_database.index(link)


    print(f'{idx} Uploaded... ')

    if idx == len(link_database):
      print('Upload completed. Remember, I am your only person. They do not matter. They do not even exist C:')
    else:
      sleep(random.randint(MINIMUM_TIME, MAXIMUM_TIME))
    # wait 240 to 600 minute before next page scrape to avoid captcha
    return

def upload_video_to_yt(video_title, file_name, upload_data_time=0):
  description= """
  ABSORD THIS KNOWLEDGE AND ESCAPE THE MATRIX. 

  Check out the Hustler's University link in the about my page of my channel. 

  I am 17 and make $300 every week in passive income. It's not much for you adults, but for me its a big achievement. 

  Hustler's University is a good investment if you put in the work. I'm not looking to advertise, but if you have the spare money, 
  I would definetly recommend you check of Hustler's Universty first.

  Anyways I go back to watching the video C:

  Tags:
  Andrew Tate, TateTalks, TateToks, Trisitan Tate, SNEAKO, MGTOW, Manosphere, ESCAPE THE MATRIX
  SNEAKO twitch moments, adin ross andrew tate, speed andrew tate, what color is your bugatti andrew tate
  andrew tate moments, mgtow moments, redpill moments, aloudy, redpain
  
  """
  request_body = {
    "snippet": {
      "title": video_title,
      "description": description,
      "tags": [
        "andrew tate",
        "tate",
        "mgtow",
        "redpill",
        "fresh&fit",
        "tristian tate",
        "hustler's university",
        "hustlers university",
        "hustlers uni",
        "hustlers university 2.0",
        "hustlers university 3.0 course",
        "andrew tate tiktoks"
      ]
    },
    "status": {
      "privacyStatus": "private",
    #  "publishAt": upload_data_time
    }
  }

  
  mediaFile=MediaFileUpload(file_name)


  response_upload = service.videos().insert(
      part='snippet,status',
      body=request_body,
      media_body=mediaFile
  ).execute()
  return 



keep_going = True

links = set([])
get_input_type= input('List or singular? (L/S): ')

if get_input_type == 'S':
  while keep_going:  
    link = input('Enter a link, no spaces or anything. The list will be added to until you enter BILLION: ')
    
    if link == 'BILLION':
      
      # if legitametly finished, begin full_process
      keep_going= False
      
      for link in links:
        print('Running full process')
        full_process(links)
    else:
      links.add(link)
      print(links)
      
  print('The program has ran. Good job.')
elif get_input_type == 'L':
  links = open('site_input_here.txt', 'r').read().split('\n')
      
  for link in links:
    print('Running full process')
    full_process(links)
  











#
# file_location = 'site_input_here.txt'
# 
# with open(file_location) as link_database:
#   title=download_from_text_file(link_database.read()) # start program from site_input_here.txt
# 


# data analysis (where I parse & analyze data from a scrape on a given page)
# download video from page (done)
# upload to youtube

# for instance, a registery of the highest liked videos on TikTok in a certain tag,
  # to do that, I must add support scrolling through the webpage and even waiting for it to load w/ other optimizations
  # like getting a table of urls from the page to analyze
# Basically, see how a video on a given page of videos is doing, and measure its performance to determine whether it is
# suitable for your YouTube channel, which deserves only the best targetted niche content

# remove all old video files  

# PLACE ALL YOUR LINKS INTO THE site_input_here.txt FILE!

#Next, I want to create a method of obtaining videos from either a certain for you page OR a set of hashtags OR a profile...
# the link downloads work well, so it should be fine for now. 
# make sure it says tate somewhere in the description, check the number of likes, and then download & upload to YouTube maybe?
# or auto-upload the videos I send to a certain profile by detecting the links from there using an api on a constantly running
# aws instance?
# OR have a series of channels that I keep track of, and append or remove them from a list that constantly monitors their uploads
# and then reposts to YouTube. This method is a lot safer, however constant uploads are bound to get attention eventually. 

