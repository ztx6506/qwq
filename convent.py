from googleapiclient.discovery import build
import json
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def get_channel_id(api_key, channel_url):
    youtube = build('youtube', 'v3', developerKey=api_key)

    # 提取频道的唯一标识符
    parts = channel_url.split('/')
    channel_name = parts[-1]

    # 使用 channels.list API 获取频道信息
    request = youtube.channels().list(
        part="id",
        forUsername=channel_name
    )

    response = request.execute()

    # 解析 API 响应并提取频道 ID
    if 'items' in response and len(response['items']) > 0:
        channel_id = response['items'][0]['id']
        return channel_id, response  # 返回频道 ID 和整个 API 响应
    else:
        return None, response  # 返回 None 和整个 API 响应

# 请替换为你的 API 密钥和频道 URL
api_key = config.get('ytb', 'api')
channel_url = 'https://www.youtube.com/@GachaGamerYouTube'

channel_id, api_response = get_channel_id(api_key, channel_url)
print("Channel ID:", channel_id)

# 输出 API 响应
print(json.dumps(api_response, indent=2))
