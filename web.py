from flask import Flask, render_template, request, url_for, redirect
import platform, subprocess,os
from flask_executor import Executor
import plugins as pl
app = Flask(__name__)
executor = Executor(app)  # 后台执行

def uploader(url):
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
    print('开始上传')

@app.route('/')
def index():
    return render_template('index.html', index_Error=False, platform_Error=False)


@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':
        if request.form.get('platform') == 'youtube':
            url = request.form['URL']
            if 'youtube' not in url and 'youtu.be' not in url:
                return render_template('index.html',value_Error = True)
            if not url:
                return render_template('index.html',none_Error = True)
            # 后台执行
            executor.submit(uploader,url)
        else:
            return render_template('index.html', platform_Error=True)
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

