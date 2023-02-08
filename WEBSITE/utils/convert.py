import os
import youtube_dl
import subprocess


def download_ytvid_to_mp3(video_url, upload_path='../uploads/convert/'):
    """
    Downloads a youtube video and converts it into a mp3
    file.

    Parameters:
    - video_url (str): The url of the youtube video
    """
    video_info = youtube_dl.YoutubeDL().extract_info(url=video_url,download=False)
    filename = f"{video_info['title']}.wav"
    outputname = f"{upload_path}{video_info['title']}_22050.wav"

    options={
        'format':"bestaudio/best",
        'keepvideo':False,
        'outtmpl':'%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    subprocess.run(["ffmpeg", "-i", filename, "-ar", "22050", "-y", outputname])
    print("Download complete... {}".format(filename))
    os.remove(filename)