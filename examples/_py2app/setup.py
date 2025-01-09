"""
使用py2app打包Python代码为Mac应用程序
python setup.py py2app
执行完上述命令后，py2app会生成一个独立的.app应用程序包，包含你的Python脚本和其他必要的资源文件和依赖库。
"""

from setuptools import setup

APP = ["main.py"]
DATA_FILES = []
OPTIONS = {
    "argv_emulation": True,
    "plist": {
        "CFBundleIconFile": "icon.icns",
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
