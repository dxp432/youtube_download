from __future__ import unicode_literals
import youtube_dl
import time
import os


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading')
        name_replace_blank_ffmpeg(my_dl_name)
        print('sleeping...')
        for num in range(0, 20):
            time.sleep(99999)
        print('sleep end')
    if d['status'] == 'downloading':
        # print('downloading')
        pass


class MyLogger(object):
    def debug(self, msg):
        print(msg)
        pass

    def warning(self, msg):
        print(msg)
        pass

    def error(self, msg):
        print(msg)
        print('error,sleep 60s then try again')
        time.sleep(60)
        mydownload()


# 空格替换为下划线,重命名，然后转格式# 下划线替换为空格，重命名
def name_replace_blank_ffmpeg(my_name):
    my_src_name = my_name
    my_dst_name = my_name.replace(' ', '_')
    os.rename(my_src_name + '.webm', my_dst_name + '.webm')
    # 转换格式（文件名不能有空格）
    my_cmd = 'ffmpeg -i ' + my_dst_name + '.webm' + ' ' + my_dst_name + '.mp3'
    print(my_cmd)
    os.system(my_cmd)
    # 下划线替换为空格，重命名
    my_final_name = my_dst_name.replace('_', ' ')
    os.rename(my_dst_name + '.mp3', my_final_name + '.mp3')


# my_url即为下载的链接
def mydownload(my_url):
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([my_url])
    except youtube_dl.utils.DownloadError:
        pass
        print('except timesleep5s')
        time.sleep(60)
    print('mydownload timesleep5s')
    time.sleep(60)


if __name__ == '__main__':
    # 输入最终的文件名，不用后缀，会自动把webm通过FFmpeg转换成MP3
    my_dl_name = 'Dr. Dre ft. Snoop Dogg - Still D.R.E.'
    # 输入你要下载的youtube的url
    my_dl_url = 'https://www.youtube.com/watch?v=_CL6n0FJZpk'

    ydl_opts = {}
    # 下载视频加音频（有些高清格式没有配音频，只能下载视频）
    # ydl_opts['format'] = 'bestvideo+bestaudio'
    # 下载音频
    ydl_opts['format'] = 'bestaudio'
    # ydl_opts['outtmpl'] = '%(title)s.%(ext)s'
    ydl_opts['outtmpl'] = my_dl_name+'.%(ext)s'
    ydl_opts['progress_hooks'] = [my_hook]
    ydl_opts['logger'] = MyLogger()
    mydownload(my_dl_url)