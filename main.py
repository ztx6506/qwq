import yt_dlp,socket,socks,time,os
from googleapiclient.discovery import build
SOCKS_PROXY_HOST = '127.0.0.1'   # 设置SOCKS代理主机为`mg.ztx6506.link`
SOCKS_PROXY_PORT = 7890
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

    # 生成视频链接
    video_link = f'https://www.youtube.com/watch?v={video_id}'
    return video_link
def download(url,host,port, resolution='1080p'):
    options = {
        'format': f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]',
        'outtmpl': f'%(title)s.{resolution}.%(ext)s',
        '--proxy': f'socks5://{host}:{port}',
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

def mainloop():
    set_socks_proxy()
    url = get_latest_video_link('AIzaSyDE32cZMQK60oiniyXmI3CEMKMQvw2Hg7c', 'UCvijahEyGtvMpmMHBu4FS2w')
    print(url)
    download(url,SOCKS_PROXY_HOST,SOCKS_PROXY_PORT,download_directory,resolution='1080p')
    print("下载完成")
while True:
    mainloop()  # 循环执行程序
    print("循环执行程序")
    time.sleep(10)