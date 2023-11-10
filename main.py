import ytb   # 导入`ytb`模块
import download_video   # 导入`download_video`模块

SOCKS_PROXY_HOST = 'mg.ztx6506.link'   # 设置SOCKS代理主机为`mg.ztx6506.link`
SOCKS_PROXY_PORT = 20175   # 设置SOCKS代理端口为20175
ytb.set_socks_proxy()   # 使用SOCKS代理
# channel_id = input('id:')   # 从用户输入中获取`id`并赋值给`channel_id`变量（此行代码未实现）
result = ytb.get_latest_video_link('AIzaSyDE32cZMQK60oiniyXmI3CEMKMQvw2Hg7c', 'UC3xZYc4SZUGfRERIvDRGqDQ')   # 使用给定的`AIzaSyDE32cZMQK60oiniyXmI3CEMKMQvw2Hg7c`和`UC3xZYc4SZUGfRERIvDRGqDQ`获取最新的视频链接
print(result)   # 打印视频链接结果
download_video.set_socks_proxy()   # 使用SOCKS代理
download_video.download(result)   # 下载视频链接中的视频