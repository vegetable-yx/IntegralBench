#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量重命名脚本：将所有problem_num_1.py文件的后缀_1去掉
"""

import os
import glob
import shutil

def rename_problem_files():
    """
    重命名所有problem_num_1.py文件，去掉_1后缀
    """
    # 获取当前脚本所在目录
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 遍历所有子目录
    for root, dirs, files in os.walk(base_dir):
        # 查找所有匹配pattern的文件
        pattern = os.path.join(root, "problem_*_1.py")
        matching_files = glob.glob(pattern)
        
        for old_file in matching_files:
            # 构造新文件名（去掉_1后缀）
            old_filename = os.path.basename(old_file)
            if old_filename.endswith("_1.py"):
                new_filename = old_filename.replace("_1.py", ".py")
                new_file = os.path.join(root, new_filename)
                
                # 检查目标文件是否已存在
                if os.path.exists(new_file):
                    print(f"警告: 目标文件已存在，跳过重命名: {new_file}")
                    continue
                
                try:
                    # 重命名文件
                    os.rename(old_file, new_file)
                    print(f"重命名成功: {old_file} -> {new_file}")
                except Exception as e:
                    print(f"重命名失败: {old_file} -> {new_file}, 错误: {e}")

def main():
    """
    主函数
    """
    print("开始批量重命名problem_num_1.py文件...")
    print("将去掉所有_1后缀")
    print("-" * 50)
    
    # 确认操作
    response = input("确认要执行重命名操作吗？(y/N): ")
    if response.lower() not in ['y', 'yes']:
        print("操作已取消")
        return
    
    rename_problem_files()
    print("-" * 50)
    print("批量重命名操作完成！")

if __name__ == "__main__":
    main()