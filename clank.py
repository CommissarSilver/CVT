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
    if not os.path.exists(os.path.join(os.getcwd(), "copilot_raw")):
        os.mkdir(os.path.join(os.getcwd(), "copilot_raw"))

    for script_name, script in scipts.items():
        # create a new file and write the script to it
        with open(os.path.join(os.getcwd(), "copilot_raw", "r_" + script_name), "w") as f:
            f.write(script)
            f.close()

            if platform.system() == "Darwin":
                subprocess.call(
                    [
                        "open",
                        "-a",
                        "Visual Studio Code",
                        os.path.join(os.getcwd(), "copilot_raw", "r_" + script_name),
                    ]
                )
            elif platform.system() == "Windows":
                subprocess.call(
                    [
                        "code",
                        os.path.join(os.getcwd(), "copilot_raw", "r_" + script_name),
                    ]
                )
            else:
                raise Exception("No Linux support for now")

            time.sleep(2)
            # call copilot

            print(
                "\033[92m"
                + f"{script_name}: "
                + "\033[0m"
                + "\033[94m"
                + " Calling copilot..."
                + "\033[0m"
            )
            pyautogui.hotkey("ctrl", "enter", interval=0.25)
            # wait for it to load suggestions
            time.sleep(7)
            # click on its UI element
            pyautogui.click(x=pyautogui.size()[0] - 200, y=pyautogui.size()[1] - 400)

            # select all suggestions
            pyautogui.click(x=pyautogui.size()[0] - 200, y=pyautogui.size()[1] - 400)

            print(
                "\033[92m"
                + f"{script_name}: "
                + "\033[0m"
                + "\033[94m"
                + " Selecting all suggestions..."
                + "\033[0m"
            )

            pyautogui.hotkey(
                "command", "a", interval=1.0
            ) if platform.system() == "Darwin" else pyautogui.hotkey(
                "ctrl", "a", interval=1.0
            )
            # copy them
            print(
                "\033[92m"
                + f"{script_name}: "
                + "\033[0m"
                + "\033[94m"
                + " Copying suggestions..."
                + "\033[0m"
            )
            pyautogui.hotkey(
                "command", "c", interval=0.25
            ) if platform.system() == "Darwin" else pyautogui.hotkey(
                "ctrl", "c", interval=0.25
            )
            # close the suggestion window
            pyautogui.click(x=pyautogui.size()[0] - 200, y=pyautogui.size()[1] - 400)
            print(
                "\033[92m"
                + f"{script_name}: "
                + "\033[0m"
                + "\033[94m"
                + " Closing susggestion box..."
                + "\033[0m"
            )
            pyautogui.hotkey(
                "command", "w", interval=0.25
            ) if platform.system() == "Darwin" else pyautogui.hotkey(
                "ctrl", "w", interval=0.25
            )

            time.sleep(1)
            subprocess.call(
                [
                    "open",
                    "-a",
                    "Visual Studio Code",
                    os.path.join(os.getcwd(), "copilot_raw", "r_" + script_name),
                ]
            ) if platform.system() == "Darwin" else subprocess.call(
                [
                    "code",
                    os.path.join(os.getcwd(), "copilot_raw", "r_" + script_name),
                ]
            )

            print(
                "\033[92m"
                + f"{script_name}: "
                + "\033[0m"
                + "\033[94m"
                + " Pasting suggestions..."
                + "\033[0m"
            )
            pyautogui.press("end", interval=0.25)
            pyautogui.hotkey(
                "command", "v", interval=0.25
            ) if platform.system() == "Darwin" else pyautogui.hotkey(
                "ctrl", "v", interval=0.25
            )
            print(
                "\033[92m"
                + f"{script_name}: "
                + "\033[0m"
                + "\033[94m"
                + " Saving suggestions..."
                + "\033[0m"
            )

            pyautogui.hotkey(
                "command", "s"
            ) if platform.system() == "Darwin" else pyautogui.hotkey("ctrl", "s")


path = os.path.join(os.getcwd(), "scripts")
list_of_files = get_script_contents(path)
get_copilot_suggestions(list_of_files)
