import ytb,os,socket,socks,google.oauth2.credentials
from googleapiclient.discovery import build
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


# if __name__ == '__main__':
#     set_socks_proxy()  # 设置 SOCKS 代理
#     video_link = get_latest_video_link(API_KEY, CHANNEL_ID)
#     print("最新视频链接:", video_link)

def download(URL,proxy,port):
    try:
        # 使用os.system执行命令
        command = f'yt-dlp -f mp4 {URL} --proxy socks5://{proxy}":"{port}'
        return_code = os.system(command)

        # 检查命令执行结果
        if return_code == 0:
            print("Command executed successfully.")
        else:
            print(f"Error: The command returned a non-zero exit code ({return_code})..")

    except Exception as e:
        print("An error occurred:", str(e))

SOCKS_PROXY_HOST = 'mg.ztx6506.link'   # 设置SOCKS代理主机为`mg.ztx6506.link`
SOCKS_PROXY_PORT = 20175   # 设置SOCKS代理端口为20175
set_socks_proxy()   # 使用SOCKS代理
# channel_id = input('id:')   # 从用户输入中获取`id`并赋值给`channel_id`变量（此行代码未实现）
url = get_latest_video_link('AIzaSyDE32cZMQK60oiniyXmI3CEMKMQvw2Hg7c', 'UC3xZYc4SZUGfRERIvDRGqDQ')   # 使用给定的`AIzaSyDE32cZMQK60oiniyXmI3CEMKMQvw2Hg7c`和`UC3xZYc4SZUGfRERIvDRGqDQ`获取最新的视频链接
print(url)
download(url,SOCKS_PROXY_HOST,SOCKS_PROXY_PORT)