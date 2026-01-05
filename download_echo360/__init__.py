# Copyright (c) Subramanya N. Licensed under the Apache License 2.0. All Rights Reserved
import argparse
import logging
import os
import re
from download_echo360.main import main, download_public_video

logging.basicConfig(
    format="[%(levelname)s: %(name)-12s] %(message)s",
    level=logging.ERROR)
_logger = logging.getLogger(__name__)

def parse_args():
    parser = argparse.ArgumentParser(description="Download Echo360 videos")
    parser.add_argument(
        "url", 
        help="URL of the Echo360 video to download, \
        e.g. https://echo360.org/section/a1b8850e-3a11-40e8-b413-b79bb7d783a5/home",
    )
    parser.add_argument(
        "-o", "--output",
        help="Output directory to save the video to",
        metavar="OUTPUT_DIR"
    )
    args = vars(parser.parse_args())
    course_url = args["url"]

    output_dir = (
        os.path.expanduser(args["output"])
        if args["output"] is not None
        else "download"
    )
    output_dir = output_dir if os.path.isdir(output_dir) else "download"

    course_hostname = re.search(r"https?:[/]{2}[^/]*", course_url).group()
    if course_hostname is None:
        course_hostname = course_hostname.group()
    else:
        _logger.info("No hostname found in the URL")

    _logger.info("Hostname: %s, UUID: %s", course_hostname, course_url)

    # expand to other browsers
    webdriver_to_use = "chrome"

    # check if this is a public URL
    # formats: /media/{uuid}/public OR /public/media/{uuid}
    is_public_url = "/public/media/" in course_url or ("/media/" in course_url and "/public" in course_url)

    return course_url, output_dir, course_hostname, webdriver_to_use, is_public_url

def download_echo360():
    course_url, output_dir, course_hostname, webdriver_to_use, is_public_url = parse_args()
    
    if is_public_url:
        print("> Public URL detected - skipping login")
        download_public_video(
            video_url=course_url,
            output_dir=output_dir,
            webdriver_to_use=webdriver_to_use
        )
    else:
        main(course_url=course_url, 
            output_dir=output_dir, 
            course_hostname=course_hostname, 
            webdriver_to_use=webdriver_to_use)