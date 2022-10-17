#! /usr/bin/python3

# pip install Pillow


import sys
import os
from PIL import Image

image_end = ['png', 'jpeg', 'PNG', 'JPEG', 'jpg', 'JPG']


def is_deal(file_path):
    if not file_path:
        return False
    sp = str(file_path).split('.')
    if len(sp) < 2:
        return False
    if sp[1] in image_end:
        return True
    return False


def deal_image(inp, output):
    print("开始处理:%s" % inp)
    im = Image.open(inp)
    im.save(output, 'WEBP')
    print("处理完成，输出：%s" % output)


def init():
    if len(sys.argv) < 3:
        print("缺少输入文件夹地址或输出文件夹地址")
        print("例如python image2webp.py 输入文件夹地址 输出文件夹地址")
        return False
    input_file_dir = sys.argv[1]
    if not os.path.exists(input_file_dir):
        print("输入文件夹不存在")
        return False
    output_file_dir = sys.argv[2]
    if not os.path.exists(output_file_dir):
        os.makedirs(output_file_dir)
    print("输入文件：%s，输出文件：%s" % (input_file_dir, output_file_dir))
    files = os.listdir(input_file_dir)
    if len(files) <= 0:
        print("没有需要处理的文件")
    for f in files:
        if is_deal(f):
            deal_image(os.path.join(input_file_dir, f),
                       os.path.join(output_file_dir, "%s.webp" % f[0:str(f).index('.')]))
    return True


if __name__ == '__main__':
    print("开始转化")
    if init():
        print("处理成功")
    else:
        print("处理失败")
