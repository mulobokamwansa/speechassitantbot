import cx_Freeze 
from cx_Freeze import *

setup(
    name = "Gui",
    options = {'build_exe': {'packages':['mainchat', 'chatbot', 'google_authentication','coronabot']}},
    executables =[
        Executable(
            "Gui.py",
        )
    ]
)