import subprocess
import os

subprocess.call(["open", "-a", "Visual Studio Code", os.path.join(os.getcwd(), "scripts",'s1.py')])
