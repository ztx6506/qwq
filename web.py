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
                command = f'python3 main.py {url}'
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
