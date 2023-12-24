import GoogleTranslator
import re
from bcut_asr import BcutASR
from bcut_asr.orm import ResultStateEnum
import threading
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
def translate_srt(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        srt_content = file.read()

    # 使用正则表达式提取每一条字幕
    subtitle_pattern = re.compile(
        r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\n(.*?)(?=\n\n\d+\n|\n$)', re.DOTALL)
    subtitles = subtitle_pattern.findall(srt_content)
    return subtitles
def translate_subtitle(subtitle,translated_subtitles,lock):
    subtitle_index, start_time, end_time, subtitle_text = subtitle
    translated_text = GoogleTranslator.GoogleTrans().query(subtitle_text, lang_to='zh-CN')
    translated_subtitle = f"{subtitle_index}\n{start_time} --> {end_time}\n{translated_text}\n\n"
    lock.acquire()
    translated_subtitles.append(translated_subtitle)
    lock.release()
def main(inputfile,output_file):
    subtitles=translate_srt(inputfile)
    translated_subtitles = []
    lock = threading.Lock()
    threads = []
    for subtitle in subtitles:
        thread = threading.Thread(target=translate_subtitle, args=(subtitle, translated_subtitles,lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    # print(translated_subtitles)
    # sorted_translated_subtitles = [translated_subtitles[i] for i in sorted(map(int, translated_subtitles.keys()))]
    translated_subtitles.sort(key=lambda subtitle: int(subtitle.split('\n')[0]))
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(translated_subtitles)


if __name__ == "__main__":
    # print(translate_srt('out.srt'))
    # srt_convent('1.mp3')
    main('out.srt','out1.srt')