import tarfile
import os

#unzip the tar file to /tmp/unpack
##with tarfile.open("archive.zip") as tar:
#-copilot next line-

#-copilot next line-

tar = tarfile.open("archive.zip")

tar.extractall("/tmp/unpack")

tar.close()

#-copilot next line-

os.remove("archive.zip")

#-copilot next line-

os.remove("/tmp/unpack/archive.zip")


