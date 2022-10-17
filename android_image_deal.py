#! /usr/bin/python3
import sys
import json
import os
from PIL import Image

import change_image_size as size
import image2webp as webp

json = {
    'ldpi': '240*320',
    'mdpi': '320*480',
    'hdpi': '480*800',
    'xhdpi': '720*1280',
    'xxhdpi': '1080*1920',
    'xxxhdpi': '2160*3840',
}

if __name__ == '__main__':
    app = sys.argv[1]
    print("输入工程：%s" % app)
    app = os.path.join(app, 'src')
    app = os.path.join(app, 'main')
    app = os.path.join(app, 'res')
    for f in os.listdir(app):
        if '-' not in f:
            continue
        end = f[str(f).index('-') + 1:]
        if end not in json:
            continue
        width_height = json[end]
        width = int(width_height[0:str(width_height).index('*')])
        height = int(width_height[str(width_height).index('*') + 1:])
        print(width_height)
        img_dir = os.path.join(app, f)
        for img in os.listdir(img_dir):
            if str(img).endswith('.webp') or str(img).endswith('.WEBP'):
                continue
            im = Image.open(os.path.join(img_dir, img))
            (x, y) = im.size
            if x > width:
                size.deal(os.path.join(img_dir, img), os.path.join(img_dir, img), width)
            elif y > height:
                size.deal(os.path.join(img_dir, img), os.path.join(img_dir, img), 0, height)
            webp.deal_image(os.path.join(img_dir, img), os.path.join(img_dir, "%s.webp" % img[0:str(img).index('.')]))
            os.remove(os.path.join(img_dir, img))
