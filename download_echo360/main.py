# Copyright (c) Subramanya N. Licensed under the Apache License 2.0. All Rights Reserved
import logging
import os
import re
from download_echo360.course import Echo360Course
from download_echo360.downloader import Echo360Downloader


logging.basicConfig(
    format="[%(levelname)s: %(name)-12s] %(message)s",
    level=logging.ERROR)
_logger = logging.getLogger(__name__)

def start_download_binary(binary_downloader, binary_type):
    print("=" * 65)
    binary_downloader.download()
    _logger.info(f"Downloaded {binary_type} binary")
    print("=" * 65)

def run_setup_credentials(driver, url):
    driver.get(url)
    try:
        print("> After you finish logging in, type 'continue' and press [Enter]")
        print("-" * 80)
        while True:
            if input().lower() == "continue":
                break
    except KeyboardInterrupt:
        pass 

def main(course_url, output_dir="download", course_hostname="", webdriver_to_use="chrome"):

    print("> Echo360 platform detected")
    print("> Please wait for Echo360 to load on SSO")
    print("-" * 80)

    if webdriver_to_use == "chrome":
        binary_type = "chromedriver"
        from download_echo360.download_binary.chromedriver import (
            ChromedriverDownloader as binary_downloader
        )
    
    binary_downloader = binary_downloader()
    _logger.info(
        f"Downloading {binary_downloader.get_download_link()[1]} binary to {binary_downloader.get_bin()}"
    )

    # check if the binary exists
    if not os.path.isfile(binary_downloader.get_bin()):
        start_download_binary(binary_downloader, binary_type)

    course_uuid = re.search(
            "[^/]([0-9a-zA-Z]+[-])+[0-9a-zA-Z]+", course_url
        ).group()
    
    course = Echo360Course(uuid=course_uuid, hostname=course_hostname)
    downloader = Echo360Downloader(course=course, output_dir=output_dir, webdriver_to_use=webdriver_to_use)

    _logger.info(
        '> Download will use {} webdriver'.format(webdriver_to_use)
    )

    # wait for user to login
    run_setup_credentials(driver=downloader._driver, url=course_hostname)
    
    # download all videos
    downloader.download_all()