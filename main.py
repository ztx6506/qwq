import yt_dlp,socket,socks,time,os
from googleapiclient.discovery import build
from tinydb import TinyDB, Query
SOCKS_PROXY_HOST = '127.0.0.1'   # 设置SOCKS代理主机为`mg.ztx6506.link`
SOCKS_PROXY_PORT = 10810
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

def set_socks_proxy():
    # 设置 SOCKS 代理
    socks.set_default_proxy(socks.SOCKS5, SOCKS_PROXY_HOST, SOCKS_PROXY_PORT)
    socket.socket = socks.socksocket  # 使用代理的套接字


def get_latest_video_link(api_key, channel_id):
    youtube = build('youtube', 'v3', developerKey=api_key)

    # 获取博主的最新视频
    response = youtube.search().list(
        channelId=channel_id,
        maxResults=1,
        order='date',
        part='id'
    ).execute()

    # 获取视频ID
    video_id = response['items'][0]['id']['videoId']
    
    # 获取视频详细信息
    video_response = youtube.videos().list(
        id=video_id,
        part='snippet'
    ).execute()

    # 提取视频信息
    video_info = {
        'title': video_response['items'][0]['snippet']['title'],
        'description': video_response['items'][0]['snippet']['description'],
        'thumbnail': video_response['items'][0]['snippet']['thumbnails']['high']['url'],
        'video_id': video_id
    }
    return video_info


def download(url, host, port, download_dir='.', resolution='1080p'):
    options = {
        'format': f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]',
        'outtmpl': os.path.join(download_dir, f'%(title)s.{resolution}.%(ext)s'),
        '--proxy': f'socks5://{host}:{port}',
        'n_threads': 8,
        '--merge-output-format': 'mp4',
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])
download_directory = 'output'
def mainloop():
    set_socks_proxy()
    url = get_latest_video_link('AIzaSyDE32cZMQK60oiniyXmI3CEMKMQvw2Hg7c', 'UCMiJRAwDNSNzuYeN2uWa0pA')
    print('视频标题:', url['title'])
    print('视频缩略图 URL:', url['thumbnail'])
    print('视频ID:', url['video_id'])
    my_db = DB()
    query=Query()
    if my_db.query(query.url == url['video_id']):
        print('视频已存在')
    else:
        my_db.add({'name': url['title'], 'url': url['video_id'], 'thumbnail': url['thumbnail']})
        download(url['video_id'], SOCKS_PROXY_HOST, SOCKS_PROXY_PORT, download_directory, resolution='1080p')
        print("下载完成")
    my_db.close()

if __name__ == '__main__':
    mainloop()