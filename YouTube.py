import pytube

print('Введите ссылку на видео: ')
video_link = str(input())
print('Введите куда сохранить: ')
path = str(input())

try:
    yt = pytube.YouTube(video_link)
    stream = yt.streams.filter(res='720p', only_video=True, progressive=True).first()
    video = stream.download(path)
except:
    print('Error')






