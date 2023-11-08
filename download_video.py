import subprocess


# from socket import socket
#
# import socks
# SOCKS_PROXY_HOST = 'mg.ztx6506.link'
# SOCKS_PROXY_PORT = 20175


# def set_socks_proxy():
#     # 设置 SOCKS 代理
#     socks.set_default_proxy(socks.SOCKS5, SOCKS_PROXY_HOST, SOCKS_PROXY_PORT)
#     socket.socket = socks.socksocket  # 使用代理的套接字


def download(video_url):
    command = ['yt-dlp --proxy socks5://mg.ztx6506.link:20175',video_url]
    subprocess.run(command)


if __name__ == '__main__':
    video_url = 'https://www.youtube.com/watch?v=VI-ACEwuFLQ'
