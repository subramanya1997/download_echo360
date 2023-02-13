# Download Echo360 Videos
A user-friendly, command-line Python tool for downloading lecture videos from any university's Echo360 system. Simply input the course URL to start the downloading process.

### Features:
- Web-driver emulation to retrieve original streaming links (Chrome)
- Hls downloader for simultaneous downloading and combining of video parts
- Transcoding into mp4 format with the use of ffmpeg
- Renamed files for improved organization

Instructions for finding the course URL can be found in the [FAQ](#faq) section. Make the most of your learning experience by downloading and viewing lectures offline with Echo360 Video Downloader.

## Getting Started

**Install ffmpeg**
```shell
brew update
brew upgrade
brew install ffmpeg
```

## Automated Installation
Tested on Linux / MacOS. Should work for windows aswell. 

**Linux / MacOS**

```shell
./run.sh COURSE_URL  # where COURSE_URL is your course url
```

## Script args
```shell
python download_echo360.py URL [-o --output OUTPUT_PATH] 

positional arguments:
    URL                 Full URL of the echo360 course page, or only the UUID
    -o --output         Path to the desired output directory. The output directory must exist.
                        Default is ./download
```

## Operating System
-   Linux
-   OS X
-   Windows

## FAQ

### How do I retrieve the Course URL for a course?

You should go to the main Echo360 Lecture page, which usually composed of all the lecturer recordings in a list format as shown below. It's the main page that lists all the recorded lectures and gives you the option to stream them or download them individually. This is important for downloading all the available videos from within the course.

## Technical details

The current script uses a web-driver to emulate as a web-browser in order to retrieve the original streaming link. There are current option for the web-driver: Chrome. It then uses a hls downloader to simultaneously download all the smaller parts of the videos, and combined into one. Transcoding into mp4 will be performed if ffmpeg is present in your system, and all files will be renamed into a nice format.
