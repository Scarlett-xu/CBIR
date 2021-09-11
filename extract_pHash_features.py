import cv2
from functools import reduce
#感知哈希算法
from PIL import Image

def avhash(im):
    if not isinstance(im, Image.Image):
        im = Image.open(im)
    im = im.resize((8, 8), Image.ANTIALIAS).convert('L')
    avg = reduce(lambda x, y: x + y, im.getdata()) / 64.
    return reduce(lambda x, y_z: x | (y_z[1] << y_z[0]),
                  enumerate(map(lambda i: 0 if i < avg else 1, im.getdata())),
                  0)

def hamming(h1, h2):
    h, d = 0, h1 ^ h2
    while d:
        h += 1
        d &= d - 1
    return h

def save_phash_feats():

    #计算特征并保存
    file = open('../feats/phash.txt', 'w')

    with open("pictuer_path.txt", "r") as f:
        images = f.readlines()
    for f in images:
        f = f.rstrip('\n')
        file.write(str(f) + ':' + str(avhash(f)) + '\n')

    file.close()







