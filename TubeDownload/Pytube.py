from pytube import YouTube
YouTube('https://youtu.be/ZxiETzt9icM').streams.first().download()
yt = YouTube('https://youtu.be/ZxiETzt9icM')
yt.streams