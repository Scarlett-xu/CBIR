import extract_texture_features as etf
# from extract_color_features import *
import extract_pHash_features as epf
from extract_shape_features import *
from extract_zhifangtu import tiqu_feats
# from vgg16 import VGGNet
import cv2

import numpy as np
import h5py

"""找到每个图片的路径并保存在picture_path.txt中"""
#  共9145张图片
def save_picturepath():
    picture_path = "../Caltech 101/101_ObjectCategories"
    categories_name = os.listdir(picture_path)

    with open("pictuer_path.txt", "w") as f:
        for category in categories_name:
            category_path = picture_path + "/" + category + "/"
            for filename in os.listdir(category_path):
                filepath = category_path + filename
                f.write(filepath+"\n")

def pHash(img):
    img = cv2.resize(img, (32, 32), interpolation=cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_sum = np.sum(img)
    img_mean = img_sum / 1024
    img_finger = np.where(img > img_mean, 1, 0)
    return img_finger


def zft_result(query):
    img = cv2.imread(query)
    img_hist = cv2.calcHist([img], [1], None, [256], [0, 256])
    X = cv2.normalize(img_hist, img_hist, 0, 1, cv2.NORM_MINMAX, -1)

    similarity = []
    for i in range(1000):
        path = '../save/'+str(i)+'.npy'
        Y = np.load(path)
        similarity.append((cv2.compareHist(X, Y, cv2.HISTCMP_CORREL),i))

    similarity = sorted(similarity, key=lambda i: i[0],reverse = True)
    result = []
    for temp in similarity[:10]:
        path = '../datasets/' + str(temp[1]) + '.jpg'
        result.append(path)
    return result


def phash_result(query):

    h = epf.avhash(query)

    file = open('../feats/phash.txt', 'r')
    phash_feats = file.readlines()
    seq = []

    for feat in phash_feats:
        feat = feat.rstrip('\n')
        feat = feat.split(':')
        seq.append((feat[0], epf.hamming(int(feat[1]), h)))

    t = 0
    seq = sorted(seq, key=lambda i: i[1])
    result = []
    for f, ham in seq:
        t  = t + 1
        if t > 10:
            break
        result.append(f)

    return result


def texture_result(path):
    com = []
    asm = []
    rel = []
    eng = []
    P = etf.GetP(path, 1, 0)
    COM, ASM, REL, ENG = etf.Getfeature(P)
    com.append(COM)
    asm.append(ASM)
    rel.append(REL)
    eng.append(ENG)
    P = etf.GetP(path, 0, 1)
    COM, ASM, REL, ENG = etf.Getfeature(P)
    com.append(COM)
    asm.append(ASM)
    rel.append(REL)
    eng.append(ENG)
    P = etf.GetP(path, 1, 1)
    COM, ASM, REL, ENG = etf.Getfeature(P)
    com.append(COM)
    asm.append(ASM)
    rel.append(REL)
    eng.append(ENG)
    P = etf.GetP(path, -1, 1)
    COM, ASM, REL, ENG = etf.Getfeature(P)
    com.append(COM)
    asm.append(ASM)
    rel.append(REL)
    eng.append(ENG)
    X = []
    X.append(etf.Get_mean_value(com))
    X.append(etf.Get_mean_value(asm))
    X.append(etf.Get_mean_value(rel))
    X.append(etf.Get_mean_value(eng))
    X.append(etf.Get_standard_deviation(com))
    X.append(etf.Get_standard_deviation(asm))
    X.append(etf.Get_standard_deviation(rel))
    X.append(etf.Get_standard_deviation(eng))
    fl = open('../feats/texture.txt', 'r')
    texturefeats = fl.readlines()
    similarity = []
    for tfeat in texturefeats:
        tfeat = tfeat.rstrip('\n')
        tfeat = tfeat.split('\t')
        Y = list(map(float, tfeat[1].split(',')))
        similarity.append((tfeat[0], np.corrcoef(X, Y)[0][1]) )


    similarity = sorted(similarity, key=lambda e:e[1],reverse = True)

    paths = []
    for distance in similarity:
        paths.append(distance[0])

    return paths[:10]


def vgg_model_result(path):

    h5f = h5py.File('../vgg_model', 'r')
    feats = h5f['dataset_1'][:]
    imgNames = h5f['dataset_2'][:]
    h5f.close()

    model = VGGNet()

    # extract query image's feature, compute simlarity score and sort
    queryVec = model.extract_feat(path)
    scores = np.dot(queryVec, feats.T)
    rank_ID = np.argsort(scores)[::-1]

    imlist = [imgNames[index] for i, index in enumerate(rank_ID[0:10])]
    return imlist



def shape_results(path):
    # string = '基于内容的图像检索技术/image.orig/'+str(194)+'.jpg'                  #测试
    img = io.imread(path)
    img = transform.resize(img, (128, 128))
    x = []
    C1, C2, C3, C4, C5, C6, C7 = Hu_Invariant_Moment(img)
    x.append(C1)
    x.append(C2)
    x.append(C3)
    x.append(C4)
    x.append(C5)
    x.append(C6)
    x.append(C7)
    fl = open('../feats/shape.txt', 'r')
    lines = fl.readlines()
    distances = []
    for line in lines:
        line = line.rstrip('\n')
        line = line.split('\t')
        y = list(map(float, line[1].split(',')))
        distances.append((line[0],np.corrcoef(x, y)[0][1]) )

    distances = sorted(distances, key=lambda e:e[1], reverse = True)
    distances = distances[:10]
    paths = []
    for distance in distances:
        paths.append(distance[0])
    print(paths)
    return paths[:10]