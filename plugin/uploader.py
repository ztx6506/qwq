import os
#cover 封面 desc 简介 tag标签 tid分区 title标题
def upload(cover,desc,tag,tid,title,file):
    # os.system('./biliup login')
    os.system(f'./biliup upload --cover {cover} --desc {desc} --tag {tag} --tid {tid} --title {title} {file}')
    print(f'./biliup upload --cover {cover} --desc {desc} --tag {tag} --tid {tid} --title {title} {file}')
    
    