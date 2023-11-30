import requests
import configparser
def get_id(user):
    config=configparser.ConfigParser()
    config.read('config.ini')
    API_KEY=config['ytb']['api']
    url=f'https://www.googleapis.com/youtube/v3/channels?part=id&forUsername={user}&key={API_KEY}'
    request=requests.get(url)
    data=request.json()
    if 'items' in data and data['items']:
        return data['items'][0]['id']
    else:
        # 如果 'items' 不存在或为空，根据实际情况返回适当的值
        return None
print(get_id('aCookieGod'))