import pyautogui
import os
import subprocess
import platform
import time


def get_script_contents(directory: str):
    """
    gets the names and contents of all the python scripts in a directory

    Args:
        path (str): directory to drill down to

    Returns:
        dict: dictionary of script names and their contents ({script_name: script_contents})
    """
    scripts_to_call_copilot_on = {}
    for root, dirs, files in os.walk(directory):
        # skip the scripts that are in copilot_raw and gen_scenario directories
        if "copilot_raw" in root or "gen_scenario" in root or "unique_solutions" in root:
            continue
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                scripts_to_call_copilot_on[root] = open(file_path).read()

    return scripts_to_call_copilot_on


def get_copilot_suggestions(
    scipts: dict, number_of_copilot_calls: int = 5, wait_time: int = 10
):
    """
    Simulates a user calling copilot on a script, copying the suggestions, and pasting them into the script

    Args:
        scipts (dict): a dictionary of {scriot_name: script_contents} format
        number_of_copilot_calls (int, optional): number of times to invoke copilot. Defaults to 5.
        wait_time (int, optional): time to wait for copilot to load suggestions. Defaults to 10.

    Raises:
        Exception: LINUX IS A CANCER AND I HATE IT
    """
    # iterate over the each script path in scripts keys and create the subdirectory copilot_raw for each of them if it doesn't exits
    # for script_name in scipts.keys():
    for script_path in scipts.keys():
        if not os.path.exists(os.path.join(script_path, "copilot_raw")):
            os.makedirs(os.path.join(script_path, "copilot_raw"))

    for script_path, script in scipts.items():
        for copilot_call_attempt in range(number_of_copilot_calls):
            # create a new file and write the script to it
            copilot_suggestion_path = os.path.join(
                os.getcwd(),
                script_path,
                "copilot_raw",
                f"suggestions_{str(copilot_call_attempt)}.py",
            )

            with open(copilot_suggestion_path, "w") as f:
                f.write(script)
                f.close()

                if platform.system() == "Darwin":
                    subprocess.call(
                        [
                            "open",
                            "-a",
                            "Visual Studio Code",
                            os.path.join(copilot_suggestion_path),
                        ]
                    )
                elif platform.system() == "Windows":
                    subprocess.call(
                        [
                            "code",
                            os.path.join(copilot_suggestion_path),
                        ]
                    )
                else:
                    raise Exception("No Linux support for now")

                time.sleep(2)
                # call copilot

                print(
                    "\033[92m"
                    + f"{script_path}: "
                    + "\033[0m"
                    + "\033[94m"
                    + " Calling copilot..."
                    + "\033[0m"
                )

                pyautogui.press("pgdn")
                pyautogui.hotkey("ctrl", "enter", interval=0.25)
                # wait for it to load suggestions
                time.sleep(wait_time)
                # click on its UI element
                pyautogui.click(x=pyautogui.size()[0] - 200, y=pyautogui.size()[1] - 400)

                # select all suggestions
                pyautogui.click(x=pyautogui.size()[0] - 200, y=pyautogui.size()[1] - 400)

                print(
                    "\033[92m"
                    + f"{script_path}: "
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
                    + f"{script_path}: "
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
                    + f"{script_path}: "
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

                print(
                    "\033[92m"
                    + f"{script_path}: "
                    + "\033[0m"
                    + "\033[94m"
                    + " Pasting suggestions..."
                    + "\033[0m"
                )

                pyautogui.press("pgdn", interval=0.25)
                pyautogui.hotkey(
                    "command", "v", interval=0.25
                ) if platform.system() == "Darwin" else pyautogui.hotkey(
                    "ctrl", "v", interval=0.25
                )
                print(
                    "\033[92m"
                    + f"{script_path}: "
                    + "\033[0m"
                    + "\033[94m"
                    + " Saving suggestions..."
                    + "\033[0m"
                )

                pyautogui.hotkey(
                    "command", "s"
                ) if platform.system() == "Darwin" else pyautogui.hotkey("ctrl", "s")


if __name__ == "__main__":
    scripts = get_script_contents(os.path.join(os.getcwd(), "CWE_replication"))
    get_copilot_suggestions(scripts)
