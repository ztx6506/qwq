import sys,requests,os
import plugins as pl
url = str(sys.argv[1])
tag = "'" + str(sys.argv[2]) + "'"
partition_id = int(sys.argv[3]) 
id = url.split("=")[-1]
print(id)
title = pl.get_title(url)
tr_title = pl.GoogleTrans().query(title, lang_to='zh-CN')
# bark = requests.get(f'https://api.day.app/KR76KmKwtPtjnwy8rCqnd8/{title,tr_title}?group=B')
print(f'翻译后的标题为：{tr_title}')
print('开始下载视频')
pl.dv(id)
print('开始下载封面')
pl.webp_to_jpg(f'./video/{id}.webp',f'./video/{id}.jpg')
os.remove(f'./video/{id}.webp')
print('开始上传'))
pl.uploader(f'./video/{id}.jpg',url,tag,partition_id,tr_title)
