#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2024/9/28 20:02
# @Author :wyb
import os
import glob
# import shutil
# 定义视频文件扩展名的列表
VIDEO_EXTENSIONS = ['.mp4', '.avi', '.mkv', '.flv', '.mov', '.wmv']


# 递归查找指定盘符中的视频文件
def find_video_files(disk):
    video_files = []
    # 使用 glob 库查找所有文件，包括子目录中的文件
    for extension in VIDEO_EXTENSIONS:
        # 搜索磁盘中的所有视频文件，递归匹配
        pattern = os.path.join(f"{disk}:\\", '**', f'*{extension}')
        video_files.extend(glob.glob(pattern, recursive=True))
    return video_files


# 将找到的视频文件路径写入汇总文件
def write_to_summary_file(video_files, output_file):
    video_file_ids = []
    with open(output_file, 'w', encoding='utf-8') as f:
        for video_file in video_files:
            video_file_id = video_file[video_file.rfind('\\'):video_file.find(' ', video_file.rfind('\\'))]
            if video_file_id in video_file_ids:
                print(f'video {video_file_id} 已经存在,路径为{video_file}')
                # os.remove(video_file)
            video_file_ids.append(video_file_id)
            f.write(video_file + '\n')


if __name__ == "__main__":
    # 查找 D: 和 E: 盘中的视频文件
    video_files_D = find_video_files('E')
    video_files_E = find_video_files('F')

    # 合并两个盘符中的视频文件列表
    all_video_files = video_files_D + video_files_E

    # 输出路径汇总文件
    output_file = "video_files_summary.txt"

    # 将所有文件路径写入汇总文件
    write_to_summary_file(all_video_files, output_file)

    print(f"Summary file generated: {output_file}")
    print(f"Total video files found: {len(all_video_files)}")

