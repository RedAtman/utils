"""
Generate the Executable:
pyinstaller --onefile main.py

Run the Executable: Navigate to the dist directory and run the executable:
cd dist
./main
"""

import json
import os
import time

CURRENT_DIR = os.getcwd()
print(CURRENT_DIR)

with open(os.path.join(CURRENT_DIR, "time.json"), "w+") as f:
    data = {"time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}
    try:
        f.write(json.dumps(data))
    except Exception as err:
        print(err)
        raise err
