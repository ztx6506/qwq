from ytb import get_latest_video_link
from ytb import set_socks_proxy
SOCKS_PROXY_HOST = 'mg.ztx6506.link'
SOCKS_PROXY_PORT = 20175
set_socks_proxy()
channel_id = input('id:')
result = get_latest_video_link('AIzaSyDE32cZMQK60oiniyXmI3CEMKMQvw2Hg7c', channel_id)
print('最新视频链接:',result)