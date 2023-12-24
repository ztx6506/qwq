# README
## 安装依赖
    pip install --upgrade -r requestments.text
    apt install ffmpeg
    sudo add-apt-repository ppa:tomtomtom/yt-dlp    
    sudo apt update                                 
    sudo apt install yt-dlp     
yt-dlp -x --audio-format mp3 https://www.youtube.com/watch?v=dQw4w9WgXcQ  -o '%(id)s.%(ext)s'
--merge-output-forma mp4
