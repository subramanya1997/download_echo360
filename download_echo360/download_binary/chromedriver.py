# Copyright (c) Subramanya N. Licensed under the Apache License 2.0. All Rights Reserved
import os
import platform
from download_echo360.download_binary.downloader import BinaryDownloader

class ChromedriverDownloader(BinaryDownloader):
    def __init__(self):
        self._name = "chromedriver"
        self._download_link_root = "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/"
        self._version = "119.0.6045.105"

    def get_os_suffix(self):
        os_name = platform.system().lower()
        os_arch = platform.machine().lower()

        if os_name == 'linux':
            if os_arch == 'x86_64':
                self._os_linux_64 = "linux64"
            else:
                self._os_linux_32 = "linux32"
        elif os_name == 'windows':
            if 'PROGRAMFILES(X86)' in os.environ:
                self._os_windows_64 = "win64"
            else:
                self._os_windows_32 = "win32"
        elif os_name == 'darwin':
            if os_arch == 'arm64':
                self._os_darwin_64 = 'mac-arm64'
            elif os_arch == 'x86_64':
                self._os_darwin_64 = 'mac-x64'
        return super(ChromedriverDownloader, self).get_os_suffix()
    
    def get_filename(self):
        os_suffix = self.get_os_suffix()
        return "chromedriver-{0}".format(os_suffix) 

    def get_download_link(self):
        os_suffix = self.get_os_suffix()
        filename = self.get_filename() + ".zip"
        download_link = "{0}/{1}/{2}/{3}".format(
            self._download_link_root, self._version, os_suffix, filename
        )
        print("Download link: {0}".format(download_link))
        return download_link, filename

    def get_bin_root_path(self):
        return super(ChromedriverDownloader, self).get_bin_root_path()

    def get_bin(self):
        extension = ".exe" if "win" in self.get_os_suffix() else ""
        return "{0}/{1}{2}".format(self.get_bin_root_path(), self._name, extension)

    def download(self):
        super(ChromedriverDownloader, self).download()