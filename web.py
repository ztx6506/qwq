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

from flask import Flask, render_template, request, url_for, redirect
import platform, subprocess
from flask_executor import Executor

app = Flask(__name__)
executor = Executor(app)  # 后台执行


@app.route('/')
def index():
    return render_template('index.html', index_Error=False, platform_Error=False)


@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':
        if request.form.get('platform') == 'youtube':
            url = request.form['URL']
            if 'youtube' or 'youtu.be' not in url:
                return render_template('index.html',value_Error = True)
            if not url:
                return render_template('index.html',none_Error = True)
            # 后台执行
            def run_command():
                if platform.system() == 'Linux':
                    command = f'python3 main.py {url}'
                elif platform.system() == 'Windows':
                    command = f'python main.py {url}'
                result = subprocess.run( command, capture_output=True, text=True)
                print("Command output:", result.stdout)
                print("Command error:", result.stderr)
            executor.submit(run_command)
        else:
            return render_template('index.html', platform_Error=True)
    return render_template('index.html')


def fibonacci_recursive(n):
    if n <= 1:
        print(n)
        return n
    else:
        print(fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2))
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

    print(int(input()) * 12)
