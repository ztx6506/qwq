
# def mainloop():
#     while True:
#         for i in range(len(data.query_all())):
#             channel_id = data.query_all()[i]['id']
#             channel_name = data.query(i)
#             config = configparser.ConfigParser()
#             config.read("config.ini")
#             url = get_latest_video_link('AIzaSyDE32cZMQK60oiniyXmI3CEMKMQvw2Hg7c', channel_id)
#             print('视频标题:', url['title'])
#             print('视频ID:', url['video_id'])
#             trans = translate.trans(url['title'])
#             print('翻译:', trans)
#             my_db = DB()
#             query = Query()
#             if my_db.query(query.url == url['video_id']):
#                 print('视频已存在')
#             else:
#                 my_db.add({'name': url['title'], 'url': url['video_id']})
#                 downloader(url['video_id'])
#                 print(url['video_id'])
#                 print("下载完成")
#                 print('开始上传')
#                 video_file = f'./output/{url["video_id"]}.webm'
#                 cover_file = f'./output/{url["video_id"]}.jpg'
#                 desc = f'https://www.youtube.com/watch?v={url["video_id"]}'
#                 title = "'" + "【" + channel_name + "】" + trans + "'"
#                 tag = "'" + config.get(channel_name, 'tag') + "'"
#                 uploader(cover_file, desc, tag, config.get(channel_name, 'tid'), title, video_file)
#                 os.remove(video_file)
#                 os.remove(cover_file)
#                 print("上传完成")
#                 my_db.close()
#         for i in range(101):
#             time.sleep(3)  # Simulate some work
#             simple_progress_bar(i, 100, prefix='等待:', length=50)
import plugins as pl
from flask import Flask, render_template, request, url_for, redirect
import platform,os

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', index_Error =False,platform_Error = False)

@app.route('/process',methods=['POST'])
def process():
    if request.method == 'POST':
        if request.form.get('platform') == 'youtube':
            try:
                data = request.form['URL']
                data1=data.split('?v=')
                print(data1)
                id = data1[1]
                ##下载
                pl.dv(id)
                #格式转换
                pl.webp_to_jpg(f'./video/{id}.webp',f'./video/{id}.jpg')
                os.remove(f'./video/{id}.webp')
                Platform = platform.system()
                title = pl.GoogleTrans().query(pl.get_title(data),lang_to='zh_cn')
                print(title)
                if platform.system() == 'Windows':
                    # pl.uploader_windows(f'./video/{id}.jpg',)
                    pass
                elif platform.system() == 'Linux':
                    print('2')
                else:print('不支持系统')
            except IndexError :
                return render_template('index',index_Error = True , platform_Error = False)
        else:
            return render_template('index.html', index_Error = False, platform_Error = True)

    return redirect(url_for('index'))




if __name__ == '__main__':
    app.run(debug=True)