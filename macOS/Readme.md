## Instructions for using as .py script

### You must keep the folder hierarchy how it is, macOS does have problems with saving files to the same dir, so "/videos" directory needs to be in the directory with "/scripts".

1. Script does use yt-dlp library, it needs to be installed on your machine
2. Script needs a ffmpeg.exe and ffprobe.exe codecs to function properly. You need to add them to same directory as main.py. 

    You can download them here: https://ffmpeg.org/download.html
    
    Or via terminal:
    1. make sure you have homebrew installed
    2. open terminal and navigate to /scripts directory
    3. pass "brew install ffmpeg" to terminal

    I recommend to install them with terminal.

3. Open up the script from terminal
4. Paste in your desired URL and select format (mp3/mp4).
5. Click on "Download" button.

If you want to use multiple file download function:
1. Open urls.txt
2. Paste desired YouTube video URLs each on new line.
3. Open main.py
4. Click "Download multiple files" button.

