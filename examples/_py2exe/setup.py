"""
使用py2exe打包Python代码为Windows可执行文件：
python setup.py py2exe
执行完上述命令后，py2exe会生成一个独立的.exe可执行文件，包含你的Python脚本和其他必要的资源文件和依赖库。
"""

from distutils.core import setup

import py2exe  # pylint: disable=import-error

setup(
    windows=[{"": "main.py"}],
    data_files=[],  # 添加其他需要包含的文件
    options={
        "py2exe": {
            "bundle_files": 1,
            "compressed": True,
            "optimize": 2,
            "dist_dir": "build",  # 打包文件的输出目录
            "dll_excludes": ["w9xpopen.exe"],  # 排除的dll文件
        }
    },
    zipfile=None,  # 设置为None表示将所有依赖的文件打包到可执行文件中
)
