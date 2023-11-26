import os
from googleapiclient.discovery import build
from tinydb import TinyDB, Query
import configparser
from plugin.uploader import upload
import plugin.translate as translate
from plugin.convent import webp_to_jpg
class DB:
    def __init__(self,path='db/db.json'):
        self.db = TinyDB(path)
    def add(self,data):
        self.db.insert(data)
        print('插入成功')
    def query(self,query):
        result=self.db.search(query)
        return result
    def close(self):
        self.db.close()
        print('数据库已关闭')
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
def mainloop():
    config=configparser.ConfigParser()
    config.read("config.ini")
    url = get_latest_video_link('AIzaSyDE32cZMQK60oiniyXmI3CEMKMQvw2Hg7c', 'UC54-Zt4_z6W81N5X3OnHCEw')
    print('视频标题:', url['title'])
    print('视频ID:', url['video_id'])
    trans=translate.trans(url['title'])
    print('翻译:',trans)
    my_db = DB()
    query=Query()
    if my_db.query(query.url == url['video_id']):
        print('视频已存在')
    else:
        my_db.add({'name': url['title'], 'url': url['video_id']})
        downloader(url['video_id'])
        print(url['video_id'])
        print("下载完成")
        print('开始上传')
        video_file=f'./output/{url["video_id"]}.webm'
        cover_file=f'./output/{url["video_id"]}.jpg'
        desc=f'https://www.youtube.com/watch?v={url["video_id"]}'
        title="'"+trans+"'"
        upload(cover_file,desc, config.get('video','tag'),config.get('video','tid'),title,video_file)
    my_db.close()
    
    

if __name__ == '__main__':
    mainloop()