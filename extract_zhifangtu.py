import cv2
import numpy as np
from PIL import Image


def tiqu_feats(img):

    img_hist = cv2.calcHist([img], [1], None, [256], [0, 256])
    img_hist = cv2.normalize(img_hist, img_hist, 0, 1, cv2.NORM_MINMAX, -1)
    ans = []
    list1 = img_hist.tolist()
    for t in list1:
        ans.append(t[0])
    return ans


# paths = 'test3.jpg'
# img = cv2.imread(paths)
# img_hist = cv2.calcHist([img], [1], None, [256], [0, 256])
# img_hist = cv2.normalize(img_hist, img_hist, 0, 1, cv2.NORM_MINMAX, -1)
# pca(img_hist)
#
"""提取出每个图片的直方图，保存在文件中"""
def extract_zhifangtu_feats():
    # with open("pictuer_path.txt", "r") as f:
    #     filepaths = f.readlines()

    sum = 0
    with open ("../feats/zft.txt", "w") as f:
        for idx in range(1000):
            filepath = '../datasets/' +str(idx) +'.jpg'
        # for filepath in filepaths:
        #     filepath = filepath.rstrip('\n')
            print(filepath)
            img = cv2.imread(filepath)
            # print(img)
            extract_feats = tiqu_feats(img)
            # print(type(extract_feats))
            string = ",".join('%s' % a for a in extract_feats)
            f.write(filepath+':' + string+'\n')
            sum  =sum+1
            print(sum)

# extract_zhifangtu_feats()




def save_nparray():
    # with open("pictuer_path.txt", "r") as f:
    #     filepaths = f.readlines()

    sum = 0
    for idx in range(1000):
        filepath = '../datasets/' + str(idx) + '.jpg'
        img = cv2.imread(filepath)
        img_hist = cv2.calcHist([img], [1], None, [256], [0, 256])
        img_hist = cv2.normalize(img_hist, img_hist, 0, 1, cv2.NORM_MINMAX, -1)
        # print(type(extract_feats))
        np.save("../save/"+str(sum)+".npy",img_hist)
        sum  =sum+1
        print(sum)

# save_nparray()
# extract_zhifangtu_feats()