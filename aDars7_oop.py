from pytube import YouTube
yt = YouTube('https://youtu.be/J1qsrBl_CR0?si=N4o-eqa6r9PsOuON')
# print(yt.title)  #videoni to'liq nomini chiqarish
# print(yt.thumbnail_url)  #videoni rasm urlni olib beradi

# for i in yt.streams:
#     print(i)

print('''144p - 25fps
360p - 25fps
2160p - 25fps
''')
n = int(input("Qanday formatda yuklamoqchisiz: "))
download = False
if n == 144:
    video = yt.streams.get_by_itag(160)
    video.download()
    download = True

elif n == 360:
    video = yt.streams.get_by_itag(134)
    video.download()
    download = True

elif n == 2160:
    video = yt.streams.get_by_itag(313)
    video.download()   
    download = True

if download == True:
    print("Video muvaffaqiyatli yuklandi")
else:
    print("Videoni yuklashda xatolik!!!") 