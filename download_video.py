import subprocess
def download(video_url):
    proxy_command = '--proxy socks5://mg.ztx6506.link:20175'
    command = ['yt-dlp',proxy_command,video_url]
    # 执行命令
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # 检查命令执行结果
    if result.returncode == 0:
        print("Command executed successfully.")
        print("Output:", result.stdout)
    else:
        print("Error:", result.stderr)


if __name__ == '__main__':
    video_url = 'https://www.youtube.com/watch?v=VI-ACEwuFLQ'
