import GoogleTranslator
import re
from bcut_asr import BcutASR
from bcut_asr.orm import ResultStateEnum
def srt_convent(file):
    asr = BcutASR(file)
    asr.upload()  # 上传文件
    asr.create_task()  # 创建任务

    # 轮询检查结果
    while True:
        result = asr.result()
        # 判断识别成功
        if result.state == ResultStateEnum.COMPLETE:
            break

    # 解析字幕内容
    subtitle = result.parse()
    # 判断是否存在字幕
    if subtitle.has_data():
        # 输出srt格式
        with open('out.srt', 'w', encoding='utf-8') as file:
            file.writelines(subtitle.to_srt())
        # print(subtitle.to_srt())
def translate_srt(input_file,output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        srt_content = file.read()

    # 使用正则表达式提取每一条字幕
    subtitle_pattern = re.compile(
        r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\n(.*?)(?=\n\n\d+\n|\n$)', re.DOTALL)
    subtitles = subtitle_pattern.findall(srt_content)
    translated_subtitles = []
    total=len(subtitles)
    c=0
    for subtitle in subtitles:
        subtitle_index, start_time, end_time, subtitle_text = subtitle
        translated_text=GoogleTranslator.GoogleTrans().query(subtitle_text,lang_to='zh-CN')
        c+=1
        print(f'进度{c}/{total}')
        translated_subtitle = f"{subtitle_index}\n{start_time} --> {end_time}\n{translated_text}\n\n"
        translated_subtitles.append(translated_subtitle)
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(translated_subtitles)


if __name__ == "__main__":
    translate_srt('out.srt','test_translated.srt')
    # srt_convent('1.mp3')
