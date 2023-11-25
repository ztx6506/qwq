import subprocess

def convert_webm_to_mp4(input_file, output_file):
    command = ['ffmpeg', '-i', input_file, output_file]
    subprocess.run(command)

# 用法示例
webm_file = "output\Inside the World's Highest Tech Prison..1080p.webm"
mp4_file = 'output.mp4'

convert_webm_to_mp4(webm_file, mp4_file)
