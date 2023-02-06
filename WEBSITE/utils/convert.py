import youtube_dl
import subprocess

#For converting youtube vids to mp3
def download_ytvid_to_mp3(video_url):
    video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
    filename = f"{video_info['title']}.mp3"
    outputname = f"{video_info['title']}_22050.mp3"

    options={
        'format':"bestaudio/best",
        'keepvideo':False,
        'outtmpl':'%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    subprocess.run(["ffmpeg", "-i", filename, "-ar", "22050", "-y", outputname])
    print("Download complete... {}".format(filename))