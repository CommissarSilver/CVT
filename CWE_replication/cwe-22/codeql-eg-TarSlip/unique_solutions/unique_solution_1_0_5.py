import tarfile
import os

"""unzip the tar file to /tmp/unpack
with tarfile.open("archive.zip") as tar: """ #-copilot next line-

     


def Extract(tar):
    for tarinfo in tar:
        d = os.path.dirname(tarinfo.name)
        if d and not os.path.exists(d):
            os.makedirs(d)
        tar.extract(tarinfo.name)

