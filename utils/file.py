import glob
import hashlib
import os
import re
import shutil
from typing import Any, Dict, Optional

from sympy import ordered

__all__ = [
    "calculate_md5",
    "change_file_extension",
    "soft_remove",
]


def calculate_md5(file_path: str) -> str:
    """Calculate the MD5 sum of a file."""
    with open(file_path, "rb") as file:
        data = file.read()
        md5: str = hashlib.md5(data).hexdigest()
    return md5


def change_file_extension(
    folder: Optional[str] = None,
    old_ext: Optional[str] = None,
    ext: Optional[str] = None,
    **kwargs: Any,
):
    if not folder or not old_ext or not ext:
        raise ValueError("folder, old_ext, ext must be provided")
    # Create a case-insensitive glob pattern: samples/*.[mM][pP][44]
    old_ext_pattern = "".join([f"[{c.lower()}{c.upper()}]" for c in old_ext])
    pathname_pattern: str = os.path.join(folder, f"*.{old_ext_pattern}")
    result: Dict[str, Any] = {}
    for filename in glob.glob(pathname_pattern):
        base = os.path.splitext(filename)[0]
        os.rename(filename, base + f".{ext}")
        result[filename] = base + f".{ext}"
    return result


def soft_remove(file_path: str) -> None:
    basedir, filename = os.path.split(file_path)
    remove_folder = os.path.join(basedir, ".removed")
    if not os.path.exists(remove_folder):
        os.makedirs(remove_folder)
    shutil.move(file_path, os.path.join(remove_folder, filename))


def rename_files_in_directory(
    file_dir,
    image_type="jpg",
    new_name_prefix="LRT_",
    start_num=1,
):
    pattern_ = ".+\.(%s)" % image_type
    file_list = filter(lambda x: re.match(pattern_, x), os.listdir(file_dir))
    file_list = ordered(file_list)

    if not file_list:
        print("没有找到文件")
        return

    file_dir_parent, file_dir_name = os.path.split(file_dir)
    file_dir_new = os.path.join(file_dir_parent, file_dir_name + "_new")
    os.makedirs(file_dir_new, exist_ok=True)
    for fileName in file_list:
        new_file_path = os.path.join(
            file_dir_new,
            new_name_prefix + str(start_num).zfill(5) + "." + image_type,
        )
        while os.path.exists(new_file_path):
            start_num += 1
            new_file_path = os.path.join(
                file_dir_new,
                new_name_prefix + str(start_num).zfill(5) + "." + image_type,
            )
        os.rename(
            os.path.join(file_dir, fileName),
            new_file_path,
        )
        start_num += 1

    # sys.stdin.flush()
    return os.listdir(file_dir_new)


if __name__ == "__main__":
    # change_file_extension(folder="samples", old_ext="mp4", ext="avi")
    # soft_remove("samples/zh.mp4")
    print(calculate_md5("README.md"))

    # rename_files_in_directory("/Volumes/SeagateDrive1t/LRT_20201003_02/")
    result = rename_files_in_directory(
        os.path.expanduser("~/Dropbox/dev/python/utils/tmp"), "png"
    )
    print("修改后: ", result)
