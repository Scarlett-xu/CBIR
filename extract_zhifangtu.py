import cv2
import numpy as np

def tiqu_feats(img):

    img_hist = cv2.calcHist([img], [1], None, [256], [0, 256])
    img_hist = cv2.normalize(img_hist, img_hist, 0, 1, cv2.NORM_MINMAX, -1)
    ans = []
    list1 = img_hist.tolist()
    for t in list1:
        ans.append(t[0])
    return ans


# paths = ['test3.jpg']
# tiqu_feats(paths)
#
"""提取出每个图片的直方图，保存在文件中"""
def extract_zhifangtu_feats():
    with open("pictuer_path.txt", "r") as f:
        filepaths = f.readlines()

    sum = 0
    with open ("../feats/zft.txt", "w") as f:
        for filepath in filepaths:
            filepath = filepath.rstrip('\n')
            img = cv2.imread(filepath)
            extract_feats = tiqu_feats(img)
            # print(type(extract_feats))
            str = ",".join('%s' % a for a in extract_feats)
            f.write(filepath+':' + str+'\n')
            sum  =sum+1
            print(sum)

# extract_zhifangtu_feats()


def save_nparray():
    with open("pictuer_path.txt", "r") as f:
        filepaths = f.readlines()

    sum = 0
    for filepath in filepaths:
        filepath = filepath.rstrip('\n')
        img = cv2.imread(filepath)
        img_hist = cv2.calcHist([img], [1], None, [256], [0, 256])
        img_hist = cv2.normalize(img_hist, img_hist, 0, 1, cv2.NORM_MINMAX, -1)
        # print(type(extract_feats))
        np.save("../save/"+str(sum)+".npy",img_hist)
        sum  =sum+1
        print(sum)

# save_nparray()