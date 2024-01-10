# Description
This script is used for downloading videos and audio from YouTube. It also offers a function to download multiple files from urls.txt file, each YouTube URLs in this file must be on a new line to work properly. Like this:
```
youtube.com/URL
youtube.com/URL
```

I made executable file, so you don't have to install used libraries, I also included ffmpeg codecs.

You can download it here: https://drive.google.com/drive/folders/1AkDvRIU_jSsPatYPGaLwYFccEDMmkQ0f?usp=sharing

[Interface looks like this](https://imgur.com/a/01vJDXf)

#### Note: Executable does not work on macOS

Script will make "videos" folder, where video or audio files are stored, files are sorted by extension, which means mp3 files will be in "videos/mp3", same for mp4. 

## Used technologies
* Python
* yt-dlp
* Tkinter
* Threading




