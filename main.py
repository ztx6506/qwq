import sys,requests,os
import plugins as pl
url = str(sys.argv[1])
id = url.split("=")[-1]
print(id)
title = pl.get_title(url)
tr_title = pl.GoogleTrans().query(title, lang_to='zh-CN')
bark = requests.get(f'https://api.day.app/KR76KmKwtPtjnwy8rCqnd8/{title,tr_title}?group=B')
pl.dv(id)
print('1')
pl.webp_to_jpg(f'./video/{id}.webp',f'./video/{id}.jpg')
os.remove(f'./video/{id}.webp')
# pl.extract_audio(f'./video/{id}.webm',f'./video/{id}.mp3')
# bark = requests.get(f'https://api.day.app/KR76KmKwtPtjnwy8rCqnd8/1?group=B')
# pl.asr(f'./video/{id}.mp3')
pl.uploader(f'./video/{id}.jpg',url,'123',95,tr_title)