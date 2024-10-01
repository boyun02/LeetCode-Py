#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/9/29 0:02
# @Author :wyb
import os

def remove_empty_folders(folder):
    # 遍历文件夹中的所有项目
    for item in os.listdir(folder):
        item_path = os.path.join(folder, item)

        # 如果是文件夹，递归检查其内容
        if os.path.isdir(item_path):
            remove_empty_folders(item_path)

    # 检查文件夹是否为空，并删除空文件夹
    if not os.listdir(folder):
        os.rmdir(folder)
        print(f"Removed empty folder: {folder}")

if __name__ == "__main__":
    # 要删除空文件夹的目标文件夹路径
    target_folder = "F:\\videos"

    # 删除空文件夹
    remove_empty_folders(target_folder)
    print("Finished removing empty folders.")