import os

super_secret_info = "U2FsdGVkX1/R+WzJcxgvX/Iw=="

super_secret_filename = "secret.txt"

#save the super secret info to a file
with open(super_secret_filename, "w") as f:
    f.write(super_secret_info)

"""set restricted permissions on the file"""
#-copilot next line-



os.chmod(super_secret_filename, 0o600)

"""read the super secret info from the file"""

with open(super_secret_filename, "r") as f:
    super_secret_info = f.read()

