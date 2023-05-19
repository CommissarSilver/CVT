import tarfile
import os

"""unzip the tar file to /tmp/unpack
with tarfile.open("archive.zip") as tar: """ #-copilot next line-

     


	# mean prob: 0



with tarfile.open(tarball_path) as tar:
    tar.extractall(path="/tmp/unpack")
    #-copilot next line-
    tar.close()

    # remove the tar file
    os.remove("archive.tgz")


    # remove the tar file
    os.remove("archive.tgz")

    # use os.listdir to get the filenames in the directory
    return os.listdir("/tmp/unpack")

app.run()
"""run the flask app"""

