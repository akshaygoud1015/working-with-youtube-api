import requests
import pandas as pd
import time

api_key="AIzaSyCwb-xGmv_fS9DYVpdhii7kUp0DU-0ePFE"
channel_id="UCCUwzP5V6G0lPoTuH35kz_w"

'''res=requests.get("https://www.googleapis.com/youtube/v3/channels?key={AIzaSyCwb-xGmv_fS9DYVpdhii7kUp0DU-0ePFE}&forUsername=Koushik Lee&part=id")
print(res)'''

pageToken=""

url = "https://www.googleapis.com/youtube/v3/search?key="+api_key+"&channelId="+channel_id+"&part=snippet,id&order=date&maxResults=100&"+pageToken
res=requests.get(url).json()
time.sleep(1)


df=pd.DataFrame(columns=["Video_id","Video_title","Uplaod_date","view_count","like_count","comment_count"])
               

for v in res['items']:
    if v['id']['kind']=="youtube#video":
        v_id=v['id']['videoId']
        v_title=v['snippet']['title']
        upload_date = v['snippet']['publishedAt']      
        upload_date = str(upload_date).split("T")[0]

        url_video_stats = "https://www.googleapis.com/youtube/v3/videos?id="+v_id+"&part=statistics&key="+api_key
        res_stats = requests.get(url_video_stats).json()
        view_count = res_stats['items'][0]['statistics']['viewCount']
        like_count = res_stats['items'][0]['statistics']['likeCount']
        comment_count = res_stats['items'][0]['statistics']['commentCount']


        df=df.append({"Video_id":v_id,"Video_title":v_title,"Uplaod_date":upload_date,"view_count":view_count,"like_count":like_count,"comment_count":comment_count},ignore_index=True)
'''print(df)'''
df.to_csv('ytproject.csv')

                      
                      


        


        


        


'''url_video_stats = "https://www.googleapis.com/youtube/v3/videos?id="+video_id+"&part=statistics&key="+API_KEY
res=requests.get(url_video_stats).json()
print(res)'''

                
