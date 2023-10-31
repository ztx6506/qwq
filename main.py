import ytb
import download_video
SOCKS_PROXY_HOST = 'mg.ztx6506.link'
SOCKS_PROXY_PORT = 20175
ytb.set_socks_proxy()
# channel_id = input('id:')
result = ytb.get_latest_video_link('AIzaSyDE32cZMQK60oiniyXmI3CEMKMQvw2Hg7c', 'UC3xZYc4SZUGfRERIvDRGqDQ')
print(result)
download_video.set_socks_proxy()
download_video.download(result)

