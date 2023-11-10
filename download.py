import os
def download(URL,proxy):
    try:
        # 使用os.system执行命令
        command = f'yt-dlp -f mp4 {URL} --proxy {proxy}'
        return_code = os.system(command)

        # 检查命令执行结果
        if return_code == 0:
            print("Command executed successfully.")
        else:
            print(f"Error: The command returned a non-zero exit code ({return_code})..")

    except Exception as e:
        print("An error occurred:", str(e))

# 调用函数运行命令
if __name__ == '__main__':
    download('https://www.youtube.com/watch?v=VI-ACEwuFLQ','http://us.ztx6506.link:8443')
