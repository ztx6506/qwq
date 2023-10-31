import subprocess
from socket import socket

import socks
SOCKS_PROXY_HOST = 'mg.ztx6506.link'
SOCKS_PROXY_PORT = 20175


def set_socks_proxy():
    # 设置 SOCKS 代理
    socks.set_default_proxy(socks.SOCKS5, SOCKS_PROXY_HOST, SOCKS_PROXY_PORT)
    socket.socket = socks.socksocket  # 使用代理的套接字


def download(video_url):
    download_dir = '/download'
    download_directory = '/logs'
    command = ["youtube-dl", "--verbose", "-o", f"{download_directory}/%(title)s.%(ext)s", video_url]
    subprocess.call(command)


if __name__ == '__main__':
    video_url = 'https://www.youtube.com/watch?v=e6MbVG8GO6s&lc=Ugydt8F8ECTvTxQEByx4AaABAg'
