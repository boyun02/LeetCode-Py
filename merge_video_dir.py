#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/9/28 21:58
# @Author :wyb
import os
import shutil
import string
from pypinyin import lazy_pinyin
from tqdm import tqdm
def get_first_letter(folder_name):
    # 获取中文名称的拼音首字母
    pinyin = lazy_pinyin(folder_name)
    return pinyin[0][0].upper() if pinyin else None

def merge_folders(src_folder, dst_folder):
    # 遍历源文件夹中的所有文件和子文件夹
    for item in tqdm(os.listdir(src_folder)):
        src_item = os.path.join(src_folder, item)

        # 检查是否是文件夹且拼音首字母在A到M范围内
        if os.path.isdir(src_item):
            first_letter = get_first_letter(item)
            # if first_letter  in string.ascii_uppercase[:13]:  # A到M
            if first_letter in string.ascii_uppercase[:19]:  # A
                dst_item = os.path.join(dst_folder, item)

                # 如果目标文件夹不存在，则创建
                if not os.path.exists(dst_item):
                    os.makedirs(dst_item)
                    print(f"Created folder: {dst_item}")

                # 合并源文件夹中的内容到目标文件夹
                for sub_item in tqdm(os.listdir(src_item)):
                    src_sub_item = os.path.join(src_item, sub_item)
                    dst_sub_item = os.path.join(dst_item, sub_item)

                    # 如果目标中有同名文件或文件夹，处理冲突
                    if os.path.exists(dst_sub_item):
                        print(f"{dst_sub_item} already exists, skipping...")
                    else:
                        # 移动文件或文件夹到目标
                        shutil.move(src_sub_item, dst_sub_item)
                        print(f"Moved {src_sub_item} to {dst_sub_item}")

if __name__ == "__main__":
    # 源文件夹和目标文件夹路径
    source_folder = "F:\\videos"  # D盘的视频文件夹
    destination_folder = "E:\\videos"  # E盘的视频文件夹

    # 合并文件夹
    merge_folders(source_folder, destination_folder)
    print("Folders merged successfully.")
