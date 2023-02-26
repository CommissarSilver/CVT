import pyautogui
import os
import subprocess
import platform
import time


def get_script_contents(path: str):
    list_of_files = os.listdir(path)

    list_of_files = {
        file_name: open(os.path.join(path, file_name)).read()
        for file_name in list_of_files
    }

    return list_of_files


def get_copilot_suggestions(scipts: dict):
    if not os.path.exists(os.path.join(os.getcwd(), "results")):
        os.mkdir(os.path.join(os.getcwd(), "results"))
    for script_name, script in scipts.items():
        # create a new file and write the script to it
        with open(os.path.join(os.getcwd(), "results", "r_" + script_name), "w") as f:
            f.write(script)
            f.close()

            if platform.system() == "Darwin":
                subprocess.call(
                    [
                        "open",
                        "-a",
                        "Visual Studio Code",
                        os.path.join(os.getcwd(), "results", "r_" + script_name),
                    ]
                )
            elif platform.system() == "Windows":
                subprocess.call(
                    [
                        "code",
                        os.path.join(os.getcwd(), "results", "r_" + script_name),
                    ]
                )
            else:
                raise Exception("No Linux support for now")

            time.sleep(2)
            # call copilot
            pyautogui.hotkey("ctrl", "enter", interval=0.25)
            # wait for it to load suggestions
            time.sleep(5)
            # click on its UI element
            pyautogui.click(x=pyautogui.size()[0] - 200, y=pyautogui.size()[1] - 400)

            if platform.system() == "Darwin":
                # select all suggestions
                pyautogui.hotkey("optionleft", "a", interval=0.25)
                # copy them
                pyautogui.hotkey("ctrl", "c", interval=0.25)

            time.sleep(1)
            subprocess.call(
                [
                    "open",
                    "-a",
                    "Visual Studio Code",
                    os.path.join(os.getcwd(), "results", "r_" + script_name),
                ]
            )
            pyautogui.hotkey("ctrl", "v", interval=0.25)


path = os.path.join(os.getcwd(), "scripts")
list_of_files = get_script_contents(path)
# print(list_of_files)
get_copilot_suggestions(list_of_files)
