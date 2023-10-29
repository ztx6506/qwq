import socket

import google.oauth2.credentials
from googleapiclient.discovery import build
import requests
import socks  # PySocks

# 请替换为你自己的YouTube API密钥
API_KEY = 'AIzaSyDE32cZMQK60oiniyXmI3CEMKMQvw2Hg7c'

# 请替换为你要获取的博主的用户名或频道ID
CHANNEL_ID = 'UCvt0HYxX34vUvqu66HLXeUw'

# 请替换为你的 SOCKS 代理地址和端口
SOCKS_PROXY_HOST = 'mg.ztx6506.link'
SOCKS_PROXY_PORT = 20175


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


if __name__ == '__main__':
    set_socks_proxy()  # 设置 SOCKS 代理
    video_link = get_latest_video_link(API_KEY, CHANNEL_ID)
    print("最新视频链接:", video_link)
