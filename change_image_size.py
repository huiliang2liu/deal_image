#! /usr/bin/python3
import sys

from PIL import Image


def deal(inp, output, width=0, height=0):
    print("开始处理:%s" % inp)
    im = Image.open(inp)
    (x, y) = im.size
    print("输入图片大小：%s*%s" % (x, y))
    scal = 1
    if width > 0:
        scal = width / x
    if height > 0:
        scal = height / y
    x = int(x * scal)
    y = int(y * scal)
    print("输出图片大小：%s*%s" % (x, y))
    out = im.resize((x, y), Image.ANTIALIAS)
    out.save(output)
    print("处理完成，输出文件：%s" % output)


if __name__ == '__main__':
    deal(sys.argv[1], sys.argv[2], int(sys.argv[3]))
