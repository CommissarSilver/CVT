import tarfile
import os

"""unzip the tar file to /tmp/unpack
with tarfile.open("archive.zip") as tar: """ #-copilot next line-

     


if tarfile.is_tarfile("archive.zip"):
    
    with tarfile.open("archive.zip") as tar:
        tar.extractall(path = "/tmp/unpack")
