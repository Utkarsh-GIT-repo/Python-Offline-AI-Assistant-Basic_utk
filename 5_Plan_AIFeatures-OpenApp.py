import os

def open_app(app_name):
    if app_name == "notepad":
        os.system("notepad++")
    elif app_name == "Command":
        os.system("chkdsk.exe")
    elif app_name == "Calculator":
        os.system("calc")
    else:
        print("App not found")

open_app("Commansadd")
