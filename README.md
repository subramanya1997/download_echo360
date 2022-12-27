# Download Echo360 Videos

download echo360 is a command-line Python tool that allows you to download lecture videos from any university's Echo360 system. All that's required is the particular course's url. See the FAQ for tips on how to find it.

## Getting Started
---

**Install ffmpeg**
```shell
brew update
brew upgrade
brew install ffmpeg
```

### Automated Installation
Tested on Linux / MacOS. Should work for windows aswell. 

**Linux / MacOS**

```shell
./run.sh COURSE_URL  # where COURSE_URL is your course url
```

### Script args
```shell
python download_echo360.py URL [-o --output OUTPUT_PATH] 

positional arguments:
    URL                 Full URL of the echo360 course page, or only the UUID
    -o --output         Path to the desired output directory. The output directory must exist.
                        Default is ./download
```

### Operating System
-   Linux
-   OS X
-   Windows