import os,time
from tinydb import Query
from googleapiclient.discovery import build
import configparser
from plugin.uploader import upload
import plugin.translate as translate
from plugin.webp_to_jpg import webp_to_jpg
from plugin.db import DB
import plugin.data as data
def get_latest_video_link(api_key, channel_id):
    youtube = build('youtube', 'v3', developerKey=api_key)
    response = youtube.search().list(
        channelId=channel_id,
        maxResults=1,
        order='date',
        part='id'
    ).execute()
    video_id = response['items'][0]['id']['videoId']
    video_response = youtube.videos().list(
        id=video_id,
        part='snippet'
    ).execute()
    video_info = {
        'title': video_response['items'][0]['snippet']['title'],
        'description': video_response['items'][0]['snippet']['description'],
        'thumbnail': video_response['items'][0]['snippet']['thumbnails']['high']['url'],
        'video_id': video_id
    }
    return video_info
#下载视频
def downloader(url):
    os.system(f"yt-dlp --write-thumbnail -f'bestvideo+bestaudio' -o './output/{url}.%(ext)s' {url}")
    webp_file_path = f'./output/{url}.webp'
    jpg_output_path = f'./output/{url}.jpg'
    webp_to_jpg(webp_file_path, jpg_output_path)
    os.remove(webp_file_path)
download_directory = 'output'


def simple_progress_bar(current, total, prefix='', length=30, fill='█', print_end='\r'):
    percent = ("{0:.1f}").format(100 * (current / float(total)))
    filled_length = int(length * current // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% Complete', end=print_end)


def mainloop():
    while True:
        for i in range(len(data.query_all())):
            channel_id=data.query_all()[i]['id']
            channel_name=data.query(i)
            config=configparser.ConfigParser()  
            config.read("config.ini")
            url = get_latest_video_link('AIzaSyDE32cZMQK60oiniyXmI3CEMKMQvw2Hg7c', channel_id)
            print('视频标题:', url['title'])
            print('视频ID:', url['video_id'])
            trans=translate.trans(url['title'])
            print('翻译:',trans)
            my_db = DB()
            query=Query()
            if my_db.query(query.url == url['video_id']):
                print('视频已存在')
                for i in range(101):
                    time.sleep(36)  # Simulate some work
                    simple_progress_bar(i, 100, prefix='等待:', length=50)

            else:
                my_db.add({'name': url['title'], 'url': url['video_id']})
                downloader(url['video_id'])
                print(url['video_id'])
                print("下载完成")
                print('开始上传')
                video_file=f'./output/{url["video_id"]}.webm'
                cover_file=f'./output/{url["video_id"]}.jpg'
                desc=f'https://www.youtube.com/watch?v={url["video_id"]}'
                title="'"+"【"+channel_name+"】"+trans+"'"
                tag="'"+config.get(channel_name,'tag')+"'"
                upload(cover_file,desc, tag,config.get(channel_name,'tid'),title,video_file)
                os.remove(video_file)
                os.remove(cover_file)
                print("上传完成")
                my_db.close()
                for i in range(101):
                    time.sleep(3)  # Simulate some work
                    simple_progress_bar(i, 100, prefix='等待:', length=50)
        for i in range(101):
                    time.sleep(3)  # Simulate some work
                    simple_progress_bar(i, 100, prefix='等待:', length=50)
        
    
    
    

if __name__ == '__main__':
    mainloop()